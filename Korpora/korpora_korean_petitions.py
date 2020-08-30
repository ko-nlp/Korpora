import json
from dataclasses import dataclass
from glob import glob
from typing import List

from .korpora import Korpus, KorpusData
from .fetch import fetch
from .utils import check_path, load_text


@dataclass
class KoreanPetition:
    text: str
    category: str
    num_agree: int
    begin: str
    end: str
    title: str


class KoreanPetitionsData(KorpusData):
    categories: List[str]
    num_agrees: List[int]
    begins: List[str]
    ends: List[str]
    titles: List[str]

    def __init__(self, contents, categories, begins, ends, num_agrees, titles):
        if not (len(contents) ==
                len(categories) ==
                len(begins) ==
                len(ends) ==
                len(num_agrees) ==
                len(titles)
               ):
            raise ValueError('All length of input arguments must be same.')

        super().__init__(contents)
        self.categories = categories
        self.num_agrees = num_agrees
        self.begins = begins
        self.ends = ends
        self.titles = titles

    def __getitem__(self, index):
        return KoreanPetition(
            self.texts[index],
            self.categories[index],
            self.num_agrees[index],
            self.begins[index],
            self.ends[index],
            self.titles[index]
        )


class KoreanPetitions(Korpus):
    """ Reference: https://github.com/lovit/petitions_archive

        Examples in a petition

            {
                "category": "일자리",
                "begin": "2018-05-01",
                "end": "2018-05-31",
                "content": "CONTENT TEXT',
                "num_agree": 2560,
                "petition_idx": "216521",
                "status": "청원종료",
                "title": "TITLE"
            }
    """
    def __init__(self, root_dir, force_download=False):
        dates = [
            '2017-08', '2017-09', '2017-10', '2017-11', '2017-12',
            '2018-01', '2018-02', '2018-03', '2018-04', '2018-05',
            '2018-06', '2018-07', '2018-08', '2018-09', '2018-10',
            '2018-11', '2018-12', '2019-01', '2019-02', '2019-03'
        ]
        paths = [f'{root_dir}/korean_petitions/petitions_{d}' for d in dates]
        exists_all = True
        for path in paths:
            exists_all *= check_path(path)
        if (force_download or not exists_all):
            fetch('korean_petitions', root_dir)

        contents, categories, begins, ends, num_agrees, titles = [], [], [], [], [], []
        for path in paths:
            con, cat, b, e, num, tit = self.cleaning(load_text(path))
            categories += cat
            contents += con
            begins += b
            ends += e
            num_agrees += num
            titles += tit
        self.train = KoreanPetitionsData(
            contents, categories, begins,
            ends, num_agrees, titles)

    def cleaning(self, raw_lines: List[str]):
        def parse(json_line):
            data = json.loads(json_line)
            return (data.get('content', None),
                    data.get('category', None),
                    data.get('begin', None),
                    data.get('end', None),
                    data.get('num_agree', 0),
                    data.get('title', None))

        separated_lines = [parse(line) for line in raw_lines]
        contents, categories, begins, ends, num_agrees, titles = zip(*separated_lines)
        return contents, categories, begins, ends, num_agrees, titles

    def get_all_texts(self):
        return self.train.texts

    def get_all_categories(self):
        return self.train.categories

    def get_all_num_agrees(self):
        return self.train.num_agrees

    def get_all_titles(self):
        return self.train.titles
