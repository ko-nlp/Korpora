import os
from typing import List

from .korpora import Korpus, LabeledSentencePairKorpusData
from .fetch import fetch
from .utils import check_path, default_korpora_path, load_text


class KorNLIData(LabeledSentencePairKorpusData):
    def __init__(self, description, texts, pairs, labels):
        super().__init__(description, texts, pairs, labels)


class KorNLI(Korpus):
    def __init__(self, root_dir=None, force_download=False):
        if root_dir is None:
            root_dir = default_korpora_path
        self.description = """    Reference: https://github.com/kakaobrain/KorNLUDatasets

    This is the dataset repository for our paper
    "KorNLI and KorSTS: New Benchmark Datasets for Korean Natural Language Understanding."
    (https://arxiv.org/abs/2004.03289)

    We introduce KorNLI and KorSTS, which are NLI and STS datasets in Korean."""

        multinli_train_path = os.path.join(root_dir, 'kornli/multinli.train.ko.tsv')
        snli_train_path = os.path.join(root_dir, 'kornli/snli_1.0_train.ko.tsv')
        xnli_dev_path = os.path.join(root_dir, 'kornli/xnli.dev.ko.tsv')
        xnli_test_path = os.path.join(root_dir, 'kornli/xnli.test.ko.tsv')
        if (force_download or
            not check_path(multinli_train_path) or
            not check_path(snli_train_path) or
            not check_path(xnli_dev_path) or
            not check_path(xnli_test_path)
            ):
            fetch('kornli', root_dir)

        self.multinli_train = KorNLIData(
            self.description,
            *self.cleaning(load_text(multinli_train_path, num_heads=1)))
        self.snli_train = KorNLIData(
            self.description,
            *self.cleaning(load_text(snli_train_path, num_heads=1)))
        self.xnli_dev = KorNLIData(
            self.description,
            *self.cleaning(load_text(xnli_dev_path, num_heads=1)))
        self.xnli_test = KorNLIData(
            self.description,
            *self.cleaning(load_text(xnli_test_path, num_heads=1)))

        self.license = """    Creative Commons Attribution-ShareAlike license (CC BY-SA 4.0)
    Details in https://creativecommons.org/licenses/by-sa/4.0/"""

    def cleaning(self, raw_lines: List[str]):
        separated_lines = [line.split('\t') for line in raw_lines]
        for i_sent, separated_line in enumerate(separated_lines):
            if len(separated_line) != 3:
                raise ValueError(f'Found some errors in line {i_sent}: {separated_line}')
        texts, pairs, labels = zip(*separated_lines)
        return texts, pairs, labels
