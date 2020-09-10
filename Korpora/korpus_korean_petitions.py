import os
import json
from dataclasses import dataclass
from typing import List

from .korpora import Korpus, KorpusData
from .utils import fetch, default_korpora_path, load_text


KOREAN_PETITIONS_FETCH_INFORMATION = [
    {
        'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2017-08',
        'destination': 'korean_petitions/petitions_2017-08',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2017-09',
        'destination': 'korean_petitions/petitions_2017-09',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2017-10',
        'destination': 'korean_petitions/petitions_2017-10',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2017-11',
        'destination': 'korean_petitions/petitions_2017-11',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2017-12',
        'destination': 'korean_petitions/petitions_2017-12',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2018-01',
        'destination': 'korean_petitions/petitions_2018-01',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2018-02',
        'destination': 'korean_petitions/petitions_2018-02',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2018-03',
        'destination': 'korean_petitions/petitions_2018-03',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2018-04',
        'destination': 'korean_petitions/petitions_2018-04',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2018-05',
        'destination': 'korean_petitions/petitions_2018-05',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2018-06',
        'destination': 'korean_petitions/petitions_2018-06',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2018-07',
        'destination': 'korean_petitions/petitions_2018-07',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2018-08',
        'destination': 'korean_petitions/petitions_2018-08',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2018-09',
        'destination': 'korean_petitions/petitions_2018-09',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2018-10',
        'destination': 'korean_petitions/petitions_2018-10',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2018-11',
        'destination': 'korean_petitions/petitions_2018-11',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2018-12',
        'destination': 'korean_petitions/petitions_2018-12',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2019-01',
        'destination': 'korean_petitions/petitions_2019-01',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2019-02',
        'destination': 'korean_petitions/petitions_2019-02',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2019-03',
        'destination': 'korean_petitions/petitions_2019-03',
        'method': 'download'
    },
]


description = """     Author : Hyunjoong Kim lovit@github
    Repository : https://github.com/lovit/petitions_archive
    References :

    청와대 국민청원 게시판의 데이터를 월별로 수집한 것입니다.
    청원은 게시판에 글을 올린 뒤, 한달 간 청원이 진행됩니다.
    수집되는 데이터는 청원종료가 된 이후의 데이터이며, 청원 내 댓글은 수집되지 않습니다.
    단 청원의 동의 개수는 수집됩니다.
    자세한 내용은 위의 repository를 참고하세요."""

license = """    CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
    Details in https://creativecommons.org/publicdomain/zero/1.0/"""


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

    def __init__(self, description, contents, categories, begins, ends, num_agrees, titles):
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


class KoreanPetitionsKorpus(Korpus):
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
        super().__init__(description, license)

        if root_dir is None:
            root_dir = default_korpora_path
        fetch_korean_petitions(root_dir, force_download)

        contents, categories, begins, ends, num_agrees, titles = [], [], [], [], [], []
        for info in KOREAN_PETITIONS_FETCH_INFORMATION:
            local_path = os.path.join(os.path.abspath(root_dir), info['destination'])
            con, cat, b, e, num, tit = self.cleaning(load_text(local_path))
            categories += cat
            contents += con
            begins += b
            ends += e
            num_agrees += num
            titles += tit
        self.train = KoreanPetitionsData(
            description, contents, categories,
            begins, ends, num_agrees, titles)

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

    def get_all_categories(self):
        return self.train.categories

    def get_all_num_agrees(self):
        return self.train.num_agrees

    def get_all_titles(self):
        return self.train.titles


def fetch_korean_petitions(root_dir, force_download):
    for info in KOREAN_PETITIONS_FETCH_INFORMATION:
        local_path = os.path.join(os.path.abspath(root_dir), info['destination'])
        fetch(info['url'], local_path, 'korean_petitions', force_download)
