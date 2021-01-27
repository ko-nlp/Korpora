import os
import platform

from .korpora import Korpus, KorpusData
from .utils import fetch, load_text, default_korpora_path


CC100KO_FETCH_INFORMATION = [
    {
        'url': 'http://data.statmt.org/cc-100/ko.txt.xz',
        'destination': 'cc-100-ko/ko.txt.xz',
        'method': 'download & unxz'
    }
]

description = """    Author : beomi@github
    Repository : http://data.statmt.org/cc-100/
    References :
      - Unsupervised Cross-lingual Representation Learning at Scale,
        Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary,
          Guillaume Wenzek, Francisco Guzmán, Edouard Grave, Myle Ott,
          Luke Zettlemoyer, Veselin Stoyanov,
        Proceedings of the 58th Annual Meeting of the Association for
          Computational Linguistics (ACL), p. 8440-8451, July 2020
      - CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data,
        Guillaume Wenzek, Marie-Anne Lachaux, Alexis Conneau, Vishrav Chaudhary,
          Francisco Guzmán, Armand Joulin, Edouard Grave,
        Proceedings of the 12th Language Resources and Evaluation Conference (LREC),
          p. 4003-4012, May 2020
    This corpus is an attempt to recreate the dataset used for training XLM-R.
    This corpus comprises of monolingual data for 100+ languages and also includes
    data for romanized languages (indicated by *_rom). This was constructed using
    the urls and paragraph indices provided by the CC-Net repository by processing
    January-December 2018 Commoncrawl snapshots. Each file comprises of documents
    separated by double-newlines and paragraphs within the same document
    separated by a newline. The data is generated using the open source CC-Net repository.
    No claims of intellectual property are made on the work of preparation of the corpus."""

license = """    No claims of intellectual property"""


class CC100KoKorpus(Korpus):
    def __init__(self, root_dir=None, force_download=False):
        super().__init__(description, license)

        if root_dir is None:
            root_dir = default_korpora_path
        fetch_cc100ko(root_dir, force_download)

        response = input(
            'KcBERT text file is large (54).\n'
            'If you want to load text in your memory, please insert `yes`\n'
            'If the `INPUT` is integer, it loads only first `INPUT` sentences\n').lower()
        if (len(response) == 1 and response == 'y') or (response == 'yes'):
            self.train = KorpusData(
                'CC100Ko.train',
                load_text(f'{root_dir}/cc-100-ko/ko.txt')
            )
        elif response.isdigit():
            self.train = KorpusData(
                'CC100Ko.train',
                load_text(f'{root_dir}/cc-100-ko/ko.txt', num_samples=int(response))
            )
        else:
            dirname = os.path.abspath(f'{root_dir}/cc-100-ko')
            self.train = f'KcBERT corpus is downloaded. Open local directory {dirname}'


def fetch_cc100ko(root_dir, force_download):
    for info in CC100KO_FETCH_INFORMATION:
        local_path = os.path.join(os.path.abspath(root_dir), info['destination'])
        fetch(info['url'], local_path, 'CC-100-Ko', force_download)

    if os.path.exists(f'{root_dir}/cc-100-ko/ko.txt'):
        return None