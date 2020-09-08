import os
from typing import List
from dataclasses import dataclass

from .korpora import Korpus, LabeledSentencePairKorpusData, LabeledSentencePair
from .utils import fetch, default_korpora_path, load_text


KORSTS_INFORMATION = [
        {
            'url': 'https://raw.githubusercontent.com/kakaobrain/KorNLUDatasets/master/KorSTS/sts-train.tsv',
            'destination': 'korsts/sts-train.tsv',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/kakaobrain/KorNLUDatasets/master/KorSTS/sts-dev.tsv',
            'destination': 'korsts/sts-dev.tsv',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/kakaobrain/KorNLUDatasets/master/KorSTS/sts-test.tsv',
            'destination': 'korsts/sts-test.tsv',
            'method': 'download'
        },
]

description = """     Author : KakaoBrain
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


@dataclass
class KorSTSExample(LabeledSentencePair):
    genre: str
    filename: str
    year: str


class KorSTSData(LabeledSentencePairKorpusData):
    genres: List[str]
    filenames: List[str]
    years: List[str]

    def __init__(self, description, texts, pairs, labels, genres, filenames, years):
        super().__init__(description, texts, pairs, labels)
        if not (len(labels) == len(genres) == len(filenames) == len(years)):
            raise ValueError('All length of `texts`, `pairs`, `labels`, `genres`, `filenames`, `years` should be same')
        self.genres = genres
        self.filenames = filenames
        self.years = years

    def __getitem__(self, index):
        return KorSTSExample(
            text=self.texts[index],
            pair=self.pairs[index],
            label=float(self.labels[index]),
            genre=self.genres[index],
            filename=self.filenames[index],
            year=self.years[index],
        )

    def get_all_genres(self):
        return self.genres

    def get_all_filenames(self):
        return self.filenames

    def get_all_years(self):
        return self.years


class KorSTS(Korpus):
    def __init__(self, root_dir=None, force_download=False):
        super().__init__(description, license)

        if root_dir is None:
            root_dir = default_korpora_path

        fetch_korsts(root_dir, force_download)

        for info in KORSTS_INFORMATION:
            local_path = os.path.join(os.path.abspath(root_dir), info['destination'])
            returns = self.cleaning(load_text(local_path, num_heads=1))
            texts, pairs, labels, genres, filenames, years = returns
            data = KorSTSData(self.description, texts, pairs, labels, genres, filenames, years)
            if 'train' in info['destination']:
                self.train = data
            elif 'dev' in info['destination']:
                self.dev = data
            elif 'test' in info['destination']:
                self.test = data
            else:
                raise ValueError('Check `KORSTS_INFORMATION`')

    def cleaning(self, raw_lines: List[str]):
        separated_lines = [line.split('\t') for line in raw_lines]
        for i_sent, separated_line in enumerate(separated_lines):
            if len(separated_line) != 7:
                raise ValueError(f'Found some errors in line {i_sent}: {separated_line}')
        genres, filenames, years, _, labels, texts, pairs = zip(*separated_lines)
        return texts, pairs, labels, genres, filenames, years

    def get_all_pairs(self):
        return self.train.get_all_pairs() + self.dev.get_all_pairs() + self.test.get_all_pairs()

    def get_all_labels(self):
        return self.train.get_all_labels() + self.dev.get_all_labels() + self.test.get_all_labels()

    def get_all_genres(self):
        return self.train.get_all_genres() + self.dev.get_all_genres() + self.test.get_all_genres()

    def get_all_filenames(self):
        return self.train.get_all_filenames() + self.dev.get_all_filenames() + self.test.get_all_filenames()

    def get_all_years(self):
        return self.train.get_all_years() + self.dev.get_all_years() + self.test.get_all_years()


def fetch_korsts(root_dir, force_download):
    for info in KORSTS_INFORMATION:
        local_path = os.path.join(os.path.abspath(root_dir), info['destination'])
        fetch(info['url'], local_path, 'korsts', force_download)
