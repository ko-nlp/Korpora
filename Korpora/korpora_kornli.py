import os
from typing import List

from .korpora import Korpus, LabeledSentencePairKorpusData
from .utils import fetch, default_korpora_path, load_text


KORNLI_CORPUS_INFORMATION = [
        {
            'url': 'https://raw.githubusercontent.com/kakaobrain/KorNLUDatasets/master/KorNLI/multinli.train.ko.tsv',
            'destination': 'kornli/multinli.train.ko.tsv',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/kakaobrain/KorNLUDatasets/master/KorNLI/snli_1.0_train.ko.tsv',
            'destination': 'kornli/snli_1.0_train.ko.tsv',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/kakaobrain/KorNLUDatasets/master/KorNLI/xnli.dev.ko.tsv',
            'destination': 'kornli/xnli.dev.ko.tsv',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/kakaobrain/KorNLUDatasets/master/KorNLI/xnli.test.ko.tsv',
            'destination': 'kornli/xnli.test.ko.tsv',
            'method': 'download'
        }
]


description = """    Author : KakaoBrain
    Repository : https://github.com/kakaobrain/KorNLUDatasets
    References :
        - Ham, J., Choe, Y. J., Park, K., Choi, I., & Soh, H. (2020). KorNLI and KorSTS: New Benchmark
           Datasets for Korean Natural Language Understanding. arXiv preprint arXiv:2004.03289.
           (https://arxiv.org/abs/2004.03289)

    This is the dataset repository for our paper
    "KorNLI and KorSTS: New Benchmark Datasets for Korean Natural Language Understanding."
    (https://arxiv.org/abs/2004.03289)
    We introduce KorNLI and KorSTS, which are NLI and STS datasets in Korean."""

license = """    Creative Commons Attribution-ShareAlike license (CC BY-SA 4.0)
    Details in https://creativecommons.org/licenses/by-sa/4.0/"""


class KorNLIData(LabeledSentencePairKorpusData):
    def __init__(self, description, texts, pairs, labels):
        super().__init__(description, texts, pairs, labels)


class KorNLI(Korpus):
    def __init__(self, root_dir=None, force_download=False):
        super().__init__(description, license)

        if root_dir is None:
            root_dir = default_korpora_path

        for info in KORNLI_CORPUS_INFORMATION:
            local_path = os.path.join(os.path.abspath(root_dir), info['destination'])
            fetch(info['url'], local_path, 'kornli', force_download)
            data = KorNLIData(
                self.description,
                *self.cleaning(load_text(local_path, num_heads=1))
            )
            if 'multinli.train' in info['destination']:
                self.multinli_train = data
            elif 'snli_1.0_train' in info['destination']:
                self.snli_train = data
            elif 'xnli.dev' in info['destination']:
                self.xnli_dev = data
            else:
                self.xnli_test = data

    def cleaning(self, raw_lines: List[str]):
        separated_lines = [line.split('\t') for line in raw_lines]
        for i_sent, separated_line in enumerate(separated_lines):
            if len(separated_line) != 3:
                raise ValueError(f'Found some errors in line {i_sent}: {separated_line}')
        texts, pairs, labels = zip(*separated_lines)
        return texts, pairs, labels

    def get_all_pairs(self):
        return (self.multinli_train.get_all_pairs() +
                self.snli_train.get_all_pairs() +
                self.xnli_dev.get_all_pairs() +
                self.xnli_test.get_all_pairs())

    def get_all_labels(self):
        return (self.multinli_train.get_all_labels() +
                self.snli_train.get_all_labels() +
                self.xnli_dev.get_all_labels() +
                self.xnli_test.get_all_labels())
