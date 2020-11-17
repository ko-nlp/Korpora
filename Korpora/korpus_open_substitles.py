import os
import re
import urllib

from .korpora import Korpus, SentencePairKorpusData
from .utils import fetch, default_korpora_path


OPEN_SUBSTITLES_FETCH_INFORMATION = [
    {
        'url': 'http://opus.nlpl.eu/download.php?f=OpenSubtitles/v2018/tmx/en-ko.tmx.gz',
        'destination': 'open_substitles/en-ko.tmx.gz',
        'method': 'download & ungzip'
    }
]


description = """    Author : TRAC (https://trac.edgewall.org/)
    Repository : http://opus.nlpl.eu/OpenSubtitles-v2018.php
    References :
        - P. Lison and J. Tiedemann, 2016, OpenSubtitles2016: Extracting Large Parallel Corpora
          from Movie and TV Subtitles. In Proceedings of the 10th International Conference on
          Language Resources and Evaluation (LREC 2016)

    This is a new collection of translated movie subtitles from http://www.opensubtitles.org/.

    [[ IMPORTANT ]]
    If you use the OpenSubtitle corpus: Please, add a link to http://www.opensubtitles.org/
    to your website and to your reports and publications produced with the data!
    I promised this when I got the data from the providers of that website!

    This is a slightly cleaner version of the subtitle collection using improved sentence alignment
    and better language checking.

    62 languages, 1,782 bitexts
    total number of files: 3,735,070
    total number of tokens: 22.10G
    total number of sentence fragments: 3.35G

    [[ NOTICE ]]
    In original data, the source language is `en` and target language is `ko`. However in Korpora,
    we change the language pair so that source language is `ko` and target language is `en`."""

license = """    Open Data. Details in https://opendefinition.org/od/2.1/en/"""


class OpenSubstitleKorpus(Korpus):
    def __init__(self, root_dir=None, force_download=False):
        super().__init__(description, license)

        if root_dir is None:
            root_dir = default_korpora_path
        fetch_open_substitles(root_dir, force_download)

        sources, targets = [], []
        for info in OPEN_SUBSTITLES_FETCH_INFORMATION:
            local_path = os.path.join(os.path.abspath(root_dir), info['destination'])[:-3]
            sources_, targets_ = parse_xtm(local_path)
            sources += sources_
            targets += targets_
        self.train = SentencePairKorpusData('OpenSubstitle.train', targets, sources)

    def get_all_pairs(self):
        return self.train.get_all_pairs()


def parse_xtm(path):
    pattern = re.compile('<seg>[\S ]+</seg>')
    def parse_segment(line):
        seg = pattern.findall(line)[0]
        return seg[5:-6]

    sources = []
    targets = []
    mode = 0
    source, target = None, None
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line[:4] == '<tu>':
                mode += 1
                continue
            elif line[:5] == '</tu>':
                mode = 0
                if source is not None and target is not None:
                    sources.append(source)
                    targets.append(target)
                source, target = None, None
                continue
            try:
                if mode == 1:
                    source = parse_segment(line)
                    mode += 1
                    continue
                if mode == 2:
                    target = parse_segment(line)
                    continue
            except:
                mode = 0
    return sources, targets


def fetch_open_substitles(root_dir, force_download):
    for info in OPEN_SUBSTITLES_FETCH_INFORMATION:
        try:
            local_path = os.path.join(os.path.abspath(root_dir), info['destination'])
            fetch(info['url'], local_path, 'open_substitles', force_download, info['method'])
        except urllib.error.HTTPError as exception:
            print('[Korpora] [open_subtitles] Failed to download. Re-try again')
            print(f'[Korpora] [open_subtitles] error messgae: {str(exception)}')
            continue
