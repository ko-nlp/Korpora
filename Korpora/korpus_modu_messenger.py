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


class ModuMessengerKorpus(ModuKorpus):
    def __init__(self, root_dir=None, force_download=False):
        super().__init__()
        if root_dir is None:
            root_dir = os.path.join(default_korpora_path, 'NIKL_MESSENGER')
        alternative_root_dir = os.path.join(root_dir, 'NIKL_MESSENGER')
        if os.path.exists(alternative_root_dir):
            root_dir = alternative_root_dir
        paths = find_corpus_paths(root_dir)
        self.train = KorpusData('모두의_메신저_말뭉치(conversation).train', load_modu_messenger(paths))


@dataclass
class Utterance:
    document_id: str
    form: List[str]
    original_form: List[str]
    speaker_id: List[int]
    time: List[str]

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'Conversation(id={self.document_id}, len={len(self.form)}, attributes=(form(str), original_form(str), speaker_id(str), time(str)))'


def document_to_utterance(document):
    document_id = document['id']
    utterance = document['utterance']
    columns = [(u['form'], u['original_form'], u['speaker_id'], u['time']) for u in utterance]
    form, original_form, speaker_id, time = zip(*columns)
    return Utterance(document_id, form, original_form, speaker_id, time)


def find_corpus_paths(root_dir_or_paths):
    prefix_pattern = re.compile('M[DM]RW')
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


def load_modu_messenger(paths):
    utterances = []
    for i_path, path in enumerate(tqdm(paths, desc='Loading ModuMessenger', total=len(paths))):
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        documents = data['document']
        utterances += [document_to_utterance(doc) for doc in documents]
    return utterances
