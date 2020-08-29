from dataclasses import dataclass
from typing import List

from .utils import default_korpora_path


@dataclass
class KorpusData:
    texts: List[str]

    def __len__(self):
        return len(self.texts)


class Korpus:
    def cleaning(self, raw_documents: List[str], **kargs):
        """`raw_data` to `sentences`"""
        raise NotImplementedError('Implement this function')

    def get_all_texts(self):
        raise NotImplementedError('Implement this function')

    def save(self, root_dir):
        """save prorce` to `sentences`"""
        raise NotImplementedError('Implement this function')
