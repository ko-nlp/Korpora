import json
import os
import re
from dataclasses import dataclass
from glob import glob
from tqdm import tqdm
from typing import List

from .korpora import Korpus, KorpusData
from .utils import default_korpora_path

description = """    모두의 말뭉치는 문화체육관광부 산하 국립국어원에서 제공하는 말뭉치로
    총 13 개의 말뭉치로 이뤄져 있습니다.

    해당 말뭉치를 이용하기 위해서는 국립국어원 홈페이지에 가셔서 "회원가입 > 말뭉치 신청 > 승인"의
    과정을 거치셔야 합니다.

    https://corpus.korean.go.kr/#none

    모두의 말뭉치는 승인 후 다운로드 가능 기간 및 횟수 (3회) 에 제한이 있습니다.

    로그인 기능 및 Korpora 패키지에서의 다운로드 기능을 제공하려 하였지만,
    국립국어원에서 위의 이유로 이에 대한 기능은 제공이 불가함을 확인하였습니다.

    Korpora==0.2.0 에서는 "개별 말뭉치 신청 > 승인"이 완료되었다고 가정,
    로컬에 다운로드 된 말뭉치를 손쉽게 로딩하는 기능만 제공합니다

    (Korpora 개발진 lovit@github, ratsgo@github)"""

license = """    모두의 말뭉치의 모든 저작권은 `문화체육관광부 국립국어원
    (National Institute of Korean Language)` 에 귀속됩니다.

    소유권을 포함한 전문은 다음의 주소에서 확인하실 수 있습니다.

    https://corpus.korean.go.kr/boards/termsInfo.do

    제13조 (소유권)
    ① 누리집이 제공하는 서비스, 그에 필요한 소프트웨어, 이미지, 마크, 로고, 디자인, 서비스 명칭,
      정보 및 상표 등과 관련된 지식 재산권 및 기타 권리는 국어원에게 있습니다.
    ② 이용자는 누리집에서 명시적으로 승인한 경우를 제외하고는 제1항의 소정의 각 재산에 대한 전부 또는
      일부의 복사, 복제, 전송, 송신, 수정, 대여, 대출, 판매, 배포, 제작, 이용 허락, 양도, 재라이선스,
      담보권 설정 행위, 상업적 이용 행위를 할 수 없으며, 제3자로 하여금 이와 같은 행위를 하도록 허락할 수 없습니다."""


class ModuKorpus(Korpus):
    def __init__(self, force_download=False):
        if force_download:
            fetch_modu()
        super().__init__(description, license)


class ModuNewsKorpus(ModuKorpus):
    def __init__(self, root_dir=None, force_download=False, load_light=True):
        super().__init__(force_download)
        if root_dir is None:
            root_dir = os.path.join(default_korpora_path, 'NIKL_NEWSPAPER')
        alternative_root_dir = os.path.join(root_dir, 'NIKL_NEWSPAPER')
        if os.path.exists(alternative_root_dir):
            root_dir = alternative_root_dir
        paths = find_corpus_paths(root_dir)
        if load_light:
            self.train = ModuNewsDataLight('모두의_뉴스_말뭉치(light).train', load_modu_news(paths, load_light))
        else:
            self.train = ModuNewsData('모두의_뉴스_말뭉치.train', load_modu_news(paths, load_light))
        self.row_to_documentid = [news.document_id for news in self.train]
        self.documentid_to_row = {document_id: idx for idx, document_id in enumerate(self.row_to_documentid)}


class ModuNewsData(KorpusData):
    def __init__(self, name, news):
        super().__init__(name, news)
        self.document_ids = [doc.document_id for doc in news]
        self.titles = [doc.title for doc in news]
        self.authors = [doc.author for doc in news]
        self.publishers = [doc.publisher for doc in news]
        self.dates = [doc.date for doc in news]
        self.topics = [doc.topic for doc in news]
        self.original_topics = [doc.original_topic for doc in news]
        self.texts = [doc.paragraph for doc in news]

    def __getitem__(self, index):
        news = ModuNews(
            self.document_ids[index],
            self.titles[index],
            self.authors[index],
            self.publishers[index],
            self.dates[index],
            self.topics[index],
            self.original_topics[index],
            self.texts[index].split('\n'))
        return news


class ModuNewsDataLight(KorpusData):
    def __init__(self, name, news):
        super().__init__(name, news)
        self.texts = [doc.paragraph for doc in news]
        self.titles = [doc.title for doc in news]
        self.document_ids = [doc.document_id for doc in news]

    def __getitem__(self, index):
        news = ModuNewsLight(
            self.document_ids[index],
            self.titles[index],
            self.texts[index])
        return news


@dataclass
class ModuNews:
    document_id: str
    title: str
    author: str
    publisher: str
    date: str
    topic: str
    original_topic: str
    paragraph: List[str]


@dataclass
class ModuNewsLight:
    document_id: str
    title: str
    paragraph: str


def document_to_a_news(document):
    document_id = document['id']
    meta = document['metadata']
    title = meta['title']
    author = meta['author']
    publisher = meta['publisher']
    date = meta['date']
    topic = meta['topic']
    original_topic = meta['original_topic']
    paragraph = '\n'.join([p['form'] for p in document['paragraph']])
    return ModuNews(document_id, title, author, publisher, date, topic, original_topic, paragraph)


def document_to_a_news_light(document):
    document_id = document['id']
    meta = document['metadata']
    title = meta['title']
    paragraph = '\n'.join([p['form'] for p in document['paragraph']])
    return ModuNewsLight(document_id, title, paragraph)


def find_corpus_paths(root_dir_or_paths):
    prefix_pattern = re.compile('N[WLPIZ]RW')
    def match(path):
        prefix = path.split(os.path.sep)[-1][:4]
        return prefix_pattern.match(prefix)

    # directory + wildcard
    if isinstance(root_dir_or_paths, str):
        paths = sorted(glob(f'{root_dir_or_paths}/*.json') + glob(root_dir_or_paths))
    else:
        paths = root_dir_or_paths

    paths = [path for path in paths if match(path)]
    if not paths:
        raise ValueError('Not found corpus files. Check `root_dir_or_paths`')
    return paths


def load_modu_news(paths, load_light):
    transform = document_to_a_news_light if load_light else document_to_a_news
    news = []
    for i_path, path in enumerate(tqdm(paths, desc='Loading ModuNews', total=len(paths))):
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        documents = data['document']
        news += [transform(document) for document in documents]
    return news


def fetch_modu(root_dir=None, force_download=False):
    raise NotImplementedError(
        "국립국어원에서 API 기능을 제공해 줄 수 없음을 확인하였습니다."
        "\n이에 따라 모두의 말뭉치는 fetch 기능을 제공하지 않습니다"
    )
