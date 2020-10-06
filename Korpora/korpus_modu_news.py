import json
import os
from dataclasses import dataclass
from glob import glob
from tqdm import tqdm
from typing import List
from Korpora.korpora import Korpus, KorpusData


description = """    모두의 말뭉치는 문화체육관광부 산하 국립국어원에서 제공하는 말뭉치로
    총 13 개의 말뭉치로 이뤄져 있습니다.

    해당 말뭉치를 이용하기 위해서는 국립국어원 홈페이지에 가셔서 "회원가입 > 말뭉치 신청 > 승인"의
    과정을 거치셔야 합니다.

    https://corpus.korean.go.kr/#none

    모두의 말뭉치는 승인 후 다운로드 가능 기간 및 횟수 (3회) 에 제한이 있습니다.

    로그인 기능 및 Korpora 패키지에서의 다운로드 기능을 제공하려 하였지만,
    국립국어원에서 위의 이유로 이에 대한 기능은 제공이 불가함을 확인하였습니다.

    Korpora==0.2.0 에서는 "개별 말뭉치 신청 > 승인"이 완료되었다고 가정,
    로컬에 다운로드 된 말뭉치를 손쉽게 로딩하는 기능만 제공할 예정입니다

    (Korpora 개발진 lovit@github, ratsgo@github)"""

license = """    모두의 말뭉치의 모든 저작권은 `문화체육관광부 국립국어원
    (National Institute of Korean Language)` 에 귀속됩니다.
    정확한 라이센스는 확인 중 입니다."""


class ModuNewsKorpus(Korpus):
    def __init__(self, root_dir_or_paths, load_light=True, force_download=False):
        super().__init__(description, license)
        if isinstance(root_dir_or_paths, str):
            if os.path.isdir(root_dir_or_paths):
                paths = sorted(glob(f'{root_dir_or_paths}/N*RW*.json'))
            else:
                # wildcard
                paths = sorted(glob(root_dir_or_paths))
        else:
            paths = root_dir_or_paths
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


def load_modu_news(paths, load_light):
    transform = document_to_a_news_light if load_light else document_to_a_news
    news = []
    for i_path, path in enumerate(paths):
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        documents = data['document']
        desc = f'Transform to ModuNews {i_path + 1}/{len(paths)} files'
        document_iterator = tqdm(documents, desc=desc, total=len(documents))
        news += [transform(document) for document in document_iterator]
    return news


def fetch_modu():
    raise NotImplementedError(
        "국립국어원에서 API 기능을 제공해 줄 수 없음을 확인하였습니다."
        "\n이에 따라 모두의 말뭉치는 fetch 기능을 제공하지 않습니다"
    )
