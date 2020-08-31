from dataclasses import dataclass
from typing import List

from .utils import default_korpora_path


@dataclass
class KorpusData:
    description: str
    texts: List[str]

    def __len__(self):
        return len(self.texts)

    def __iter__(self):
        raise NotImplementedError('Implement __iter__')

    def get_all_texts(self):
        """
        If Some KorpusDataClass has two or more text attributes, modify this function.

            class SentencePairData(KorpusData):
                pairs: List[str]

                def get_all_texts(self):
                    return self.texts + self.pairs

        """
        return self.texts

    def __str__(self):
        classname = self.__class__.__name__
        spec = ""
        for name, var in self.__dict__.items():
            if name not in {'description', 'self'}:
                spec += f'  {classname}.{name} (list[{var[0].__class__.__name__}]) : size={len(var)}\n'
        s = f"""{classname}\n{self.description}\n\nAttributes:\n{spec}\n"""
        return s


class Korpus:
    description: str
    license: str

    def __str__(self):
        classname = self.__class__.__name__
        s = f"{classname}\n{self.description}\n\nAttributes\n"
        for name, var in self.__dict__.items():
            if name not in {'description', 'license', 'self'}:
                s += f' {classname}.{name} : size={len(var)}\n'
        return s

    def cleaning(self, raw_documents: List[str], **kargs):
        """`raw_data` to `sentences`"""
        raise NotImplementedError('Implement this function')

    def get_all_texts(self):
        raise NotImplementedError('Implement this function')

    def save(self, root_dir):
        """save prorce` to `sentences`"""
        raise NotImplementedError('Implement this function')
