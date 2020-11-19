import json
import os
import re
from dataclasses import dataclass
from glob import glob
from tqdm import tqdm
from typing import List, Tuple

from .korpora import KorpusData
from .korpus_modu_news import ModuKorpus
from .utils import default_korpora_path


class ModuNEKorpus(ModuKorpus):
    def __init__(self, root_dir=None, force_download=False):
        super().__init__()
        if root_dir is None:
            root_dir = os.path.join(default_korpora_path, 'NIKL_NE')
        alternative_root_dir = os.path.join(root_dir, 'NIKL_NE')
        if os.path.exists(alternative_root_dir):
            root_dir = alternative_root_dir
        paths = find_corpus_paths(root_dir)
        self.train = KorpusData('모두의_개체명_말뭉치.train', load_modu_ne(paths))
        self.tagmap = {
            'PS': 'PERSON',
            'LC': 'LOCATION',
            'OG': 'ORGANIZATION',
            'AF': 'ARTIFACT',
            'DT': 'DATE',
            'TI': 'TIME',
            'CV': 'CIVILIZATION',
            'AM': 'ANIMAL',
            'PT': 'PLANT',
            'QT': 'QUANTITY',
            'FD': 'STUDY_FIELD',
            'TR': 'THEORY',
            'EV': 'EVENT',
            'MT': 'MATERIAL',
            'TM': 'TERM'
        }


def find_corpus_paths(root_dir_or_paths):
    prefix_pattern = re.compile('[NS]XNE')
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


@dataclass
class NamedEntityExample:
    sentence_id: str
    sentence: str
    tags: List[str]
    positions: List[Tuple]

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"""NamedEntityExample(
    id={self.sentence_id},
    sentence={self.sentence},
    tags={self.tags},
    positions={self.positions}
)"""


def document_to_examples(document):
    examples = []
    sentence = document['sentence']
    for example in sentence:
        example_id = example['id']
        form = example['form']
        tags = [ne['label'] for ne in example['NE']]
        positions = [(ne['begin'], ne['end']) for ne in example['NE']]
        examples.append(NamedEntityExample(example_id, form, tags, positions))
    return examples


def load_modu_ne(paths):
    examples = []
    for path in paths:
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        documents = data['document']
        desc = f'Loading ModuNE ({os.path.basename(path)})'
        documents_iterator = tqdm(documents, desc=desc, total=len(documents))
        examples += [example for doc in documents_iterator for example in document_to_examples(doc)]
    return examples
