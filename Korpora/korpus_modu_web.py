import json
import os
import re
from dataclasses import dataclass
from glob import glob
from tqdm import tqdm
from typing import List

from .korpora import KorpusData
from .korpus_modu_news import ModuKorpus
from .utils import default_korpora_path


class ModuWebKorpus(ModuKorpus):
    def __init__(self, root_dir=None, force_download=False):
        super().__init__()
        paths = ModuKorpus.get_corpus_path(root_dir, 'NIKL_WEB', find_corpus_paths)
        if not paths:
            raise ValueError('Not found corpus files. Check `root_dir`')

        self.train = KorpusData('모두의_웹_말뭉치.train', load_modu_web(paths))

    @classmethod
    def exists(cls, root_dir=None):
        paths = ModuKorpus.get_corpus_path(root_dir, 'NIKL_WEB', find_corpus_paths)
        return len(paths) > 0


def find_corpus_paths(root_dir_or_paths):
    prefix_pattern = re.compile('E[BPSR]RW')
    def match(path):
        prefix = path.split(os.path.sep)[-1][:4]
        return prefix_pattern.match(prefix)

    # directory + wildcard
    if isinstance(root_dir_or_paths, str):
        paths = sorted(glob(f'{root_dir_or_paths}/*.json') + glob(root_dir_or_paths))
    else:
        paths = root_dir_or_paths

    paths = [path for path in paths if match(path)]
    return paths


def load_modu_web(paths):
    texts = []
    for i_path, path in enumerate(tqdm(paths, desc='Loading ModuWeb', total=len(paths))):
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        documents = data['document']
        texts += [document_to_text(document) for document in documents]
    return texts


def document_to_text(document):
    return '\n'.join([p['form'] for p in document['paragraph']])
