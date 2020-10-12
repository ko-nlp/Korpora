import json
import os
import re
from dataclasses import dataclass
from glob import glob
from tqdm import tqdm
from typing import List, Tuple
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


class ModuMorphemeKorpus(Korpus):
    def __init__(self, root_dir_or_paths, force_download=False):
        super().__init__(description, license)
        paths = find_corpus_paths(root_dir_or_paths)
        self.train = KorpusData('모두의_형태분석_말뭉치.train', load_modu_morpheme(paths))
        self.tagmap = {
            'JKS': '주격조사',
            'JKC': '보격조사',
            'JKG': '관형격조사',
            'JKO': '목적격조사',
            'JKB': '부사격조사',
            'JKV': '호격조사',
            'JKQ': '인용격조사',
            'JX': '보조사',
            'JC': '접속조사',
            'EP': '선어말어미',
            'EF': '종결어미',
            'EC': '연결어미',
            'ETN': '명사형전성어미',
            'ETM': '관형형전성어미',
            'XPN': '체언접두사',
            'XSN': '명사파생접미사',
            'XSV': '동사파생접미사',
            'XSA': '형용사파생접미사',
            'XR': '어근',
            'SF': '마침표, 물음표, 느낌표',
            'SP': '쉼표, 가운뎃점, 콜론, 빗금',
            'SS': '따옴표, 괄호표, 줄표',
            'SE': '줄임표',
            'SO': '붙임표(물결)',
            'SW': '기타 기호',
            'SL': '외국어',
            'SH': '한자',
            'SN': '숫자',
            'NA': '분석불능범주',
            'NF': '명사추정범주',
            'NV': '용언추정범주',
            'NNG': '일반명사',
            'NNP': '고유명사',
            'NNB': '의존명사',
            'NP': '대명사',
            'NR': '수사',
            'VV': '동사',
            'VA': '형용사',
            'VX': '보조용언',
            'VCP': '긍정지정사',
            'VCN': '부정지정사',
            'MMA': '성상 관형사',
            'MMD': '지시 관형사',
            'MMN': '수 관형사',
            'MAG': '일반부사',
            'MAJ': '접속부사',
            'IC': '감탄사',
            'NAP': '이름과 같은 개인정보'
        }


def find_corpus_paths(root_dir_or_paths):
    prefix_pattern = re.compile('[NS]XMP')
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


@dataclass
class MorphemesExample:
    sentence_id: str
    sentence: str
    morphemes: List[str]
    tags: List[str]
    eojeol_ids: List[int]

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"""Morphemes(
    id={self.sentence_id},
    sentence={self.sentence},
    tags={self.morphemes},
    positions={self.tags},
    eojeol_id={self.eojeol_ids}
)"""


def document_to_examples(document):
    examples = []
    sentence = document['sentence']
    for example in sentence:
        example_id = example['id']
        try:
            form = example['form']
            columns = [(m['form'], m['label'], m['word_id']) for m in example['morpheme']]
            morphemes, tags, eojeol_ids = zip(*columns)
            eojeol_ids = tuple(idx - 1 for idx in eojeol_ids)
            examples.append(MorphemesExample(example_id, form, morphemes, tags, eojeol_ids))
        except:
            continue
    return examples


def load_modu_morpheme(paths):
    examples = []
    for path in paths:
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        documents = data['document']
        desc = f'Loading ModuMorpheme ({os.path.basename(path)})'
        documents_iterator = tqdm(documents, desc=desc, total=len(documents))
        examples += [example for doc in documents_iterator for example in document_to_examples(doc)]
    return examples


def fetch_modu():
    raise NotImplementedError(
        "국립국어원에서 API 기능을 제공해 줄 수 없음을 확인하였습니다."
        "\n이에 따라 모두의 말뭉치는 fetch 기능을 제공하지 않습니다"
    )