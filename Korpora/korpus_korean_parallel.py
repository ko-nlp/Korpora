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

        train_info, dev_info, test_info = KOREAN_PARALLEL_KOEN_NEWS_FETCH_INFORMATION
        self.train = self.fetch_and_load('train', root_dir, train_info, force_download)
        self.dev = self.fetch_and_load('dev', root_dir, dev_info, force_download)
        self.test = self.fetch_and_load('test', root_dir, test_info, force_download)

    def fetch_and_load(self, mode, root_dir, fetch_info, force_download):
        dataname = f'koennews.{mode}'
        source_path = f'{root_dir}/korean_parallel/korean-english-park.{mode}.ko'
        target_path = f'{root_dir}/korean_parallel/korean-english-park.{mode}.en'
        if (force_download) or (not os.path.exists(source_path)) or (not os.path.exists(target_path)):
            local_path = os.path.join(os.path.abspath(root_dir), fetch_info['destination'])
            fetch(fetch_info['url'], local_path, 'korean_parallel', force_download, fetch_info['method'])
        sources, targets = load_parallel_text(source_path, target_path)
        return SentencePairKorpusData(dataname, sources, targets)


def fetch_korean_parallel_koen_news(root_dir, force_download):
    for info in KOREAN_PARALLEL_KOEN_NEWS_FETCH_INFORMATION:
        local_path = os.path.join(os.path.abspath(root_dir), info['destination'])
        fetch(info['url'], local_path, 'korean_parallel', force_download, info['method'])
