import os
from dataclasses import dataclass
from typing import List

from .korpora import Korpus, KorpusData
from .fetch import fetch
from .utils import check_path, load_text


@dataclass
class NSMCExample:
    text: str
    label: int


class NSMCData(KorpusData):
    labels: List[str]

    def __init__(self, texts, labels):
        if len(texts) != len(labels):
            raise ValueError('`texts` and `labels` must be same length')
        self.description = f"    Naver sentiment movie corpus v1.0. size of data={len(texts)}"
        self.texts = texts
        self.labels = labels

    def __getitem__(self, index):
        return NSMCExample(self.texts[index], self.labels[index])

    def __iter__(self):
        for text, label in zip(self.texts, self.labels):
            yield text, label


class NSMC(Korpus):
    def __init__(self, root_dir, force_download=False):
        train_path = os.path.join(root_dir, 'nsmc/ratings_train.txt')
        test_path = os.path.join(root_dir, 'nsmc/ratings_test.txt')
        if (force_download or
            not check_path(train_path) or
            not check_path(test_path)
           ):
            fetch('nsmc', root_dir)

        train_texts, train_labels = self.cleaning(load_text(train_path, num_heads=1))
        test_texts, test_labels = self.cleaning(load_text(test_path, num_heads=1))
        self.train = NSMCData(train_texts, train_labels)
        self.test = NSMCData(test_texts, test_labels)
        self.description = """    Reference: https://github.com/e9t/nsmc

    Naver sentiment movie corpus v1.0
    This is a movie review dataset in the Korean language.
    Reviews were scraped from Naver Movies.

    The dataset construction is based on the method noted in
    [Large movie review dataset][^1] from Maas et al., 2011.

    [^1]: http://ai.stanford.edu/~amaas/data/sentiment/"""

        self.license = """    CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
    Details in https://creativecommons.org/publicdomain/zero/1.0/"""

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
