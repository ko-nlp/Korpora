import os
from typing import List

from .korpora import Korpus, KorpusData, LabeledSentence
from .utils import fetch, load_text, default_korpora_path


NSMC_FETCH_INFORMATION = [
    {
        'url': 'https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt',
        'destination': 'nsmc/ratings_train.txt',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt',
        'destination': 'nsmc/ratings_test.txt',
        'method': 'download'
    },
]

description = """     Author : e9t@github
    Repository : https://github.com/e9t/nsmc
    References : www.lucypark.kr/docs/2015-pyconkr/#39

    Naver sentiment movie corpus v1.0
    This is a movie review dataset in the Korean language.
    Reviews were scraped from Naver Movies.

    The dataset construction is based on the method noted in
    [Large movie review dataset][^1] from Maas et al., 2011.

    [^1]: http://ai.stanford.edu/~amaas/data/sentiment/"""

license = """    CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
    Details in https://creativecommons.org/publicdomain/zero/1.0/"""


class NSMCData(KorpusData):
    labels: List[str]

    def __init__(self, texts, labels):
        if len(texts) != len(labels):
            raise ValueError('`texts` and `labels` must be same length')
        self.description = f"    Naver sentiment movie corpus v1.0. size of data={len(texts)}"
        self.texts = texts
        self.labels = labels

    def __getitem__(self, index):
        return LabeledSentence(self.texts[index], self.labels[index])


class NSMCKorpus(Korpus):
    def __init__(self, root_dir=None, force_download=False):
        super().__init__(description, license)

        if root_dir is None:
            root_dir = default_korpora_path
        fetch_nsmc(root_dir, force_download)

        for info in NSMC_FETCH_INFORMATION:
            local_path = os.path.join(os.path.abspath(root_dir), info['destination'])
            text, labels = self.cleaning(load_text(local_path, num_heads=1))
            if 'train' in info['destination']:
                self.train = NSMCData(text, labels)
            else:
                self.test = NSMCData(text, labels)

    def cleaning(self, raw_lines: List[str]):
        separated_lines = [line.split('\t') for line in raw_lines]
        for i_sent, separated_line in enumerate(separated_lines):
            if len(separated_line) != 3:
                raise ValueError(f'Found some errors in line {i_sent}: {separated_line}')
        _, texts, labels = zip(*separated_lines)
        labels = [int(label) for label in labels]
        return texts, labels

    def get_all_texts(self):
        return self.train.texts + self.test.texts

    def get_all_labels(self):
        return self.train.labels + self.test.labels


def fetch_nsmc(root_dir, force_download):
    for info in NSMC_FETCH_INFORMATION:
        local_path = os.path.join(os.path.abspath(root_dir), info['destination'])
        fetch(info['url'], local_path, 'nsmc', force_download)
