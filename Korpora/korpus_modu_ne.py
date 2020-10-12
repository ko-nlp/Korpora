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


class ModuNEKorpus(Korpus):
    def __init__(self, root_dir_or_paths, force_download=False):
        super().__init__(description, license)
        paths = find_corpus_paths(root_dir_or_paths)
        self.train = KorpusData('모두의_개체명_말뭉치.train', load_modu_ne(paths))
        self.tagmap = {
            'PS': 'PERSON',
            'LC': 'LOCATION',
            'OG': 'ORGANIZATION',
            'AF': 'ARTIFACT',
            'DT': 'DATE',
            'TI': 'TIME',
            'CV': 'CIVILIZATION',
            'AM': 'ANIMAL',
            'PT': 'PLANT',
            'QT': 'QUANTITY',
            'FD': 'STUDY_FIELD',
            'TR': 'THEORY',
            'EV': 'EVENT',
            'MT': 'MATERIAL',
            'TM': 'TERM'
        }


def find_corpus_paths(root_dir_or_paths):
    prefix_pattern = re.compile('[NS]XNE')
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
class NamedEntityExample:
    sentence_id: str
    sentence: str
    tags: List[str]
    positions: List[Tuple]

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"""NamedEntityExample(
    id={self.sentence_id},
    sentence={self.sentence},
    tags={self.tags},
    positions={self.positions}
)"""


def document_to_examples(document):
    examples = []
    sentence = document['sentence']
    for example in sentence:
        example_id = example['id']
        form = example['form']
        tags = [ne['label'] for ne in example['NE']]
        positions = [(ne['begin'], ne['end']) for ne in example['NE']]
        examples.append(NamedEntityExample(example_id, form, tags, positions))
    return examples


def load_modu_ne(paths):
    examples = []
    for path in paths:
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        documents = data['document']
        desc = f'Loading ModuNE ({os.path.basename(path)})'
        documents_iterator = tqdm(documents, desc=desc, total=len(documents))
        examples += [example for doc in documents_iterator for example in document_to_examples(doc)]
    return examples


def fetch_modu():
    raise NotImplementedError(
        "국립국어원에서 API 기능을 제공해 줄 수 없음을 확인하였습니다."
        "\n이에 따라 모두의 말뭉치는 fetch 기능을 제공하지 않습니다"
    )