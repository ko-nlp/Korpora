import os
from typing import List

from .korpora import Korpus, SentencePairKorpusData
from .utils import fetch, default_korpora_path, load_parallel_text


KOREAN_PARALLEL_KOEN_NEWS_FETCH_INFORMATION = [
    {
        'url': 'https://raw.githubusercontent.com/jungyeul/korean-parallel-corpora/master/korean-english-news-v1/korean-english-park.train.tar.gz',
        'destination': 'korean_parallel/korean-english-park.train.tar.gz',
        'method': 'download & untar'
    },
    {
        'url': 'https://raw.githubusercontent.com/jungyeul/korean-parallel-corpora/master/korean-english-news-v1/korean-english-park.dev.tar.gz',
        'destination': 'korean_parallel/korean-english-park.dev.tar.gz',
        'method': 'download & untar'
    },
    {
        'url': 'https://raw.githubusercontent.com/jungyeul/korean-parallel-corpora/master/korean-english-news-v1/korean-english-park.test.tar.gz',
        'destination': 'korean_parallel/korean-english-park.test.tar.gz',
        'method': 'download & untar'
    },
]


description = """    Author : KakaoBrain
    Repository : https://github.com/jungyeul/korean-parallel-corpora
    References :
        - Jungyeul Park, Jeen-Pyo Hong and Jeong-Won Cha (2016) Korean Language Resources for Everyone.
          In Proceedings of the 30th Pacific Asia Conference on Language, Information and Computation
          (PACLIC 30). October 28 - 30, 2016. Seoul, Korea. 
          (https://www.aclweb.org/anthology/Y16-2002/)"""

license = """    Creative Commons Attribution Noncommercial No-Derivative-Works 3.0
    Details in https://creativecommons.org/licenses/by-nc-nd/3.0/"""


class KoreanParallelKOENNewsKorpus(Korpus):
    def __init__(self, root_dir=None, force_download=False):
        super().__init__(description, license)

        if root_dir is None:
            root_dir = default_korpora_path
        fetch_korean_parallel_koen_news(root_dir, force_download)

        source_base = '{}/korean_parallel/korean-english-park.{}.ko'
        target_base = '{}/korean_parallel/korean-english-park.{}.en'
        self.train = SentencePairKorpusData(
            'koennews.train',
            *load_parallel_text(
                source_base.format(root_dir, 'train'),
                target_base.format(root_dir, 'train')
            )
        )
        self.dev = SentencePairKorpusData(
            'koennews.dev',
            *load_parallel_text(
                source_base.format(root_dir, 'dev'),
                target_base.format(root_dir, 'dev')
            )
        )
        self.test = SentencePairKorpusData(
            'koennews.test',
            *load_parallel_text(
                source_base.format(root_dir, 'test'),
                target_base.format(root_dir, 'test')
            )
        )


def fetch_korean_parallel_koen_news(root_dir, force_download):
    for info in KOREAN_PARALLEL_KOEN_NEWS_FETCH_INFORMATION:
        local_path = os.path.join(os.path.abspath(root_dir), info['destination'])
        fetch(info['url'], local_path, 'korean_parallel', force_download, info['method'])
