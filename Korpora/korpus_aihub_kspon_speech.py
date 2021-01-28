import os
import re
from glob import glob
from dataclasses import dataclass
from typing import Dict

from .korpora import Korpus, KorpusData
from .utils import default_korpora_path


description = """    AI Hub 에서는 학습용 데이터를 제공합니다.

    데이터를 활용하기 위해서는 아래 주소의 홈페이지에서 "AI데이터" 클릭 후,
    이용하려는 데이터마다 직접 신청을 하셔야 합니다.

    https://www.aihub.or.kr/
    
    한국어 음성 데이터는 `AI 데이터` > `교육/문화/스포츠/` > `한국어음성` 혹은 아래의 주소에서
    다운받으실 수 있으며, AI Hub에서는 1000시간 분량의 전체 음원데이터 뿐 아니라, 전사 스크립트(Text only)만을
    따로 평문 텍스트(확장자: trn) 형식으로도 제공하고 있습니다.

    https://www.aihub.or.kr/aidata/105  (2021.01.27 기준)

    AI Hub 학습데이터는 신청 즉시 자동 승인됩니다.
    Korpora>=0.3.0 에서는 로컬에 다운로드 된 말뭉치를 손쉽게 로딩하는 기능만 제공합니다.

    이 스크립트는 전사스크립트 묶음 파일(KsponSpeech_scripts.zip)을 사용합니다. 이 파일을 압축 풀면
    아래와 같은 파일들이 나옵니다.

    train.trn
    dev.trn
    eval_clean.trn
    eval_other.trn

    위 파일들은 `~/Korpora/AIHub_KsponSpeech_scripts/` 혹은 `path/to/AIHub_KsponSpeech_scripts/` 에
    저장되었다고 가정합니다.

    (Korpora 개발진 lovit@github, ratsgo@github)"""

license = """    AI Hub 에서 제공하는 데이터의 소유권 및 전문은 다음의 주소에서 확인할 수 있습니다.

    https://aihub.or.kr/form/iyongyaggwan

    제16조 포털의 소유권
    1. AI 허브가 제공하는 서비스, 그에 필요한 소프트웨어, 이미지, 마크, 로고, 디자인, 서비스명칭, 정보 및
       상표 등과 관련된 지식재산권 및 기타 권리는 운영기관(및 AI허브 서비스 제공과 관련하여 운영기관과 계약을
       체결한 기관)에 소유권이 있습니다.
    2. 귀하는 AI 허브에서 명시적으로 승인한 경우를 제외하고는 전항의 소정의 각 재산에 대한 전부 또는 일부의 수정,
       대여, 대출, 판매, 배포, 제작, 양도, 재라이센스, 담보권 설정 행위, 상업적 이용 행위를 할 수 없으며,
       제3자로 하여금 이와 같은 행위를 하도록 허락할 수 없습니다"""


class AIHubKsponSpeechKorpus(Korpus):
    def __init__(self, root_dir=None, force_download=False, prefix='', name='AIHub_KsponSpeech'):
        super().__init__(description, license)
        if root_dir is None:
            root_dir = os.path.join(
                default_korpora_path, 'AIHub_KsponSpeech_scripts', prefix)
        elif isinstance(root_dir, str) and os.path.isdir(root_dir):
            root_dir = os.path.join(
                root_dir, 'AIHub_KsponSpeech_scripts', prefix)
        paths = find_corpus_paths(root_dir)
        self.train = KorpusData(
            f'{name}.train', load_aihub_kspon_speech_scripts(paths))


@dataclass
class KsponSpeech:
    sentence_id: str
    sentence: str
    pronounce_sentence: str
    original_sentence: str
    pronounces: Dict[str, str]

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"""KsponSpeech(
    id={self.sentence_id},
    sentence={self.sentence},
    pronounce_sentence={self.pronounce_sentence},
    original_sentence={self.original_sentence},
    pronounces={self.pronounces},
    )"""


def find_corpus_paths(root_dir, suffix='.trn'):
    def match(path):
        return path[-4:] == suffix

    # directory + wildcard
    if isinstance(root_dir, str):
        paths = sorted(glob(f'{root_dir}/*{suffix}') + glob(root_dir))
    else:
        paths = root_dir
    paths = [path for path in paths if match(path)]
    if not paths:
        raise ValueError('Not found corpus files. Check `root_dir`')
    return paths


def parse_kspon_speech(line):
    sentence_id, original_sentence = line.split(' :: ')

    # Cleaning - remove unknown/noise labels
    sentence = re.sub(r'\s*[ublon]/\s*', r' ', original_sentence)

    # Cleaning - remove meaningless character(maybe typo in original transcription)
    sentence = re.sub(r'^/ ', r' ', sentence)

    # Cleaning - remove repetition characters
    sentence = re.sub(r'[\+\*]', r'', sentence)

    pronounces = dict(re.findall(r'\(([^\)]+)\)/\(([^\)]+)\)', sentence))
    pron_sentence = re.sub(r'\(([^\)]+)\)/\(([^\)]+)\)', r'\2', sentence)
    sentence = re.sub(r'\(([^\)]+)\)/\(([^\)]+)\)', r'\1', sentence)

    # Cleaning - remove filler characters
    sentence = re.sub(r'(?<=[^\)])/\s*', r' ', sentence)
    pron_sentence = re.sub(r'(?<=[^\)])/\s*', r' ', pron_sentence)

    # Cleaning - remove space+
    sentence = re.sub(r'  +', r' ', sentence)
    pron_sentence = re.sub(r'  +', r' ', pron_sentence)

    original_sentence = original_sentence.strip()
    pron_sentence = pron_sentence.strip()
    sentence = sentence.strip()
    return sentence_id, sentence, pron_sentence, original_sentence, pronounces


def load_aihub_kspon_speech_scripts(paths):
    examples = []
    for path in paths:
        with open(path, encoding='utf-8') as f:
            examples += [KsponSpeech(*parse_kspon_speech(line))
                         for line in f.readlines()]

    return examples
