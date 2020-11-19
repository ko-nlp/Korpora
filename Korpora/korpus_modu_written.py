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


class ModuWrittenKorpus(ModuKorpus):
    def __init__(self, root_dir=None, force_download=False):
        super().__init__()
        if root_dir is None:
            root_dir = os.path.join(default_korpora_path, 'NIKL_WRITTEN')
        alternative_root_dir = os.path.join(root_dir, 'NIKL_WRITTEN')
        if os.path.exists(alternative_root_dir):
            root_dir = alternative_root_dir
        paths = find_corpus_paths(root_dir)
        self.train = KorpusData('모두의_문어_말뭉치.train', load_modu_written(paths))


def find_corpus_paths(root_dir_or_paths):
    prefix_pattern = re.compile('W[ABCZ]RW')
    def match(path):
        prefix = path.split(os.path.sep)[-1][:4]
        return prefix_pattern.match(prefix)

    # directory + wildcard
    if isinstance(root_dir_or_paths, str):
        paths = sorted(glob(f'{root_dir_or_paths}/*.json') + glob(root_dir_or_paths))
    else:
        paths = root_dir_or_paths

    paths = [path for path in paths if match(path)]
    if not paths:
        raise ValueError('Not found corpus files. Check `root_dir_or_paths`')
    return paths


def load_modu_written(paths):
    texts = []
    for i_path, path in enumerate(tqdm(paths, desc='Loading Written', total=len(paths))):
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        documents = data['document']
        texts += [paragraph for document in documents for paragraph in document_to_texts(document)]
    return texts


def document_to_texts(document):
    return [p['form'] for p in document['paragraph']]
