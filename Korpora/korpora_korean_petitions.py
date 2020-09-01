import json
from dataclasses import dataclass
from glob import glob
from typing import List

from .korpora import Korpus, KorpusData
from .fetch import fetch
from .utils import check_path, default_korpora_path, load_text


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

    def __init__(self, contents, categories, begins, ends, num_agrees, titles, description):
        if not (len(contents) ==
                len(categories) ==
                len(begins) ==
                len(ends) ==
                len(num_agrees) ==
                len(titles)
               ):
            raise ValueError('All length of input arguments must be same.')

        super().__init__(description=description, texts=contents)
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
    def __init__(self, root_dir=None, force_download=False):
        if root_dir is None:
            root_dir = default_korpora_path
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
        description = """    청와대 국민청원 게시판의 데이터를 월별로 수집한 것입니다.
            청원은 게시판에 글을 올린 뒤, 한달 간 청원이 진행됩니다. 수집되는 데이터는 청원종료가 된 이후의 데이터이며, 청원 내 댓글은 수집되지 않습니다. 단 청원의 동의 개수는 수집됩니다.
            자세한 내용은 아래 repository를 참고하세요.

            https://github.com/lovit/petitions_archive
                """
        self.train = KoreanPetitionsData(
            contents, categories, begins,
            ends, num_agrees, titles, description)
        self.description = description
        self.license = """    CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
    Details in https://creativecommons.org/publicdomain/zero/1.0/"""

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
