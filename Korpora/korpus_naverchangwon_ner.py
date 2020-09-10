import os
from typing import List

from .korpora import Korpus, WordTagKorpusData
from .utils import fetch, default_korpora_path, load_text


NAVER_CHANGWON_NER_FETCH_INFORMATION = [
        {
            'url': 'https://raw.githubusercontent.com/naver/nlp-challenge/master/missions/ner/data/train/train_data',
            'destination': 'naver_changwon_ner/train_data',
            'method': 'download'
        },
]

description = """    Author : 네이버 + 창원대
    Repository : https://github.com/naver/nlp-challenge/tree/master/missions/ner
    References : http://air.changwon.ac.kr/?page_id=10

    개체명(Named Entity)은 인명, 기관명, 지명 등과 같이 문장 또는 문서에서 특정한 의미를 가지고 있는 단어 또는 어구를 말합니다.
    이 때문에 개체명은 정보 검색 및 언어 이해를 위한 분석에서 주요한 대상으로 다루어지고 있습니다.
    Data.ly에서는 개체명 코퍼스를 제공하여 연구에 도움을 드리고자 하며, 공개적인 리더보드를 통해 많은 분들의 연구 동향을 논의/공유하고자 합니다.
    제공되는 코퍼스는 Data.ly에서 제작한 것으로, 연구 및 리더보드를 위한 학습으로 사용 가능하며 상업적인 목적으로 사용될 수 없습니다."""

license = """    연구 및 리더보드를 위한 학습으로 사용 가능하며 상업적인 목적으로 사용될 수 없습니다."""


class NaverChangwonNERData(WordTagKorpusData):
    def __init__(self, description, texts, words, tags):
        super().__init__(description, texts, words, tags)


class NaverChangwonNERKorpus(Korpus):
    def __init__(self, root_dir=None, force_download=False):
        super().__init__(description, license)

        if root_dir is None:
            root_dir = default_korpora_path
        fetch_nc_ner(root_dir, force_download)

        info = NAVER_CHANGWON_NER_FETCH_INFORMATION[0]
        local_path = os.path.join(os.path.abspath(root_dir), info['destination'])
        self.train = NaverChangwonNERData(
            self.description,
            *self.cleaning(load_text(local_path, num_heads=0))
        )

    def cleaning(self, raw_lines: List[str]):
        separated_lines = [line.split('\t') for line in raw_lines]
        all_texts, all_words, all_tags, text, words, tags, = [], [], [], "", [], []
        for separated_line in separated_lines:
            if len(separated_line) == 3:
                _, word, tag = separated_line
                text += word + " "
                words.append(word)
                tags.append(tag)
            else:
                all_texts.append(text)
                all_words.append(words)
                all_tags.append(tags)
                text, words, tags = "", [], []
        return all_texts, all_words, all_tags

    def get_all_words(self):
        return self.train.get_all_words()

    def get_all_tags(self):
        return self.train.get_all_tags()

    def get_all_words_and_tags(self):
        return [item for item in self.train]


def fetch_nc_ner(root_dir, force_download):
    for info in NAVER_CHANGWON_NER_FETCH_INFORMATION:
        local_path = os.path.join(os.path.abspath(root_dir), info['destination'])
        fetch(info['url'], local_path, 'naver_changwon_ner', force_download)
