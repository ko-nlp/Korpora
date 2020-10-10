from dataclasses import dataclass
from typing import List, Union


@dataclass
class KorpusData:
    name: str
    texts: List[str]

    def __len__(self):
        return len(self.texts)

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def __getitem__(self, index):
        return self.texts[index]

    def get_all_texts(self):
        return self.texts

    def __str__(self):
        attributes = ""
        for var_name, var in self.__dict__.items():
            if var_name not in {'name', 'description', 'self'}:
                attributes += f'  - {self.name}.{var_name} : list[{var[0].__class__.__name__}]\n'
        s = f"""{self.name}: size={len(self.texts)}\n{attributes}"""
        return s

    def __repr__(self):
        return self.__str__()


@dataclass
class LabeledSentence:
    text: str
    label: Union[int, float, str, bool]


class LabeledSentenceKorpusData(KorpusData):
    labels: List[Union[str, int]]

    def __init__(self, name, texts, labels):
        if not (len(texts) == len(labels)):
            raise ValueError('All two arguments must be same length')
        super().__init__(name, texts)
        self.labels = labels

    def __getitem__(self, index):
        return LabeledSentence(self.texts[index], self.labels[index])

    def get_all_labels(self):
        return self.labels


@dataclass
class SentencePair:
    text: str
    pair: str


class SentencePairKorpusData(KorpusData):
    pairs: List[str]

    def __init__(self, name, texts, pairs):
        if not (len(texts) == len(pairs)):
            raise ValueError('All two arguments must be same length')
        super().__init__(name, texts)
        self.pairs = pairs

    def __getitem__(self, index):
        return SentencePair(self.texts[index], self.pairs[index])

    def get_all_pairs(self):
        return self.pairs


@dataclass
class LabeledSentencePair:
    text: str
    pair: str
    label: Union[str, int, float, bool]


class LabeledSentencePairKorpusData(KorpusData):
    pairs: List[str]
    labels: List

    def __init__(self, name, texts, pairs, labels):
        if not (len(texts) == len(pairs) == len(labels)):
            raise ValueError('All three arguments must be same length')
        super().__init__(name, texts)
        self.pairs = pairs
        self.labels = labels

    def __getitem__(self, index):
        return LabeledSentencePair(self.texts[index], self.pairs[index], self.labels[index])

    def get_all_pairs(self):
        return self.pairs

    def get_all_labels(self):
        return self.labels


@dataclass
class WordTag:
    text: str
    words: List[str]
    tags: List[str]


class WordTagKorpusData(KorpusData):
    words: List[List[str]]
    tags: List[List[str]]

    def __init__(self, name, texts, words, tags):
        if not (len(texts) == len(words) == len(tags)):
            raise ValueError('All three arguments must be same length')
        super().__init__(name, texts)
        self.words = words
        self.tags = tags

    def __getitem__(self, index):
        return WordTag(self.texts[index], self.words[index], self.tags[index])

    def get_all_words(self):
        return self.words

    def get_all_tags(self):
        return self.tags


class Korpus:
    description: str
    license: str

    def __init__(self, description, license):
        self.description = description
        self.license = license
        print(f"""
    Korpora 는 다른 분들이 연구 목적으로 공유해주신 말뭉치들을
    손쉽게 다운로드, 사용할 수 있는 기능만을 제공합니다.

    말뭉치들을 공유해 주신 분들에게 감사드리며, 각 말뭉치 별 설명과 라이센스를 공유 드립니다.
    해당 말뭉치에 대해 자세히 알고 싶으신 분은 아래의 description 을 참고,
    해당 말뭉치를 연구/상용의 목적으로 이용하실 때에는 아래의 라이센스를 참고해 주시기 바랍니다.

    # Description
{description}

    # License
{license}\n""")

    def __str__(self):
        classname = self.__class__.__name__
        s = f"{classname}\n{self.description}\n\nAttributes\n----------\n"
        for var_name, var in self.__dict__.items():
            if isinstance(var, KorpusData):
                s += f'{str(var)}'
        return s

    def cleaning(self, raw_documents: List[str], **kargs):
        """`raw_data` to `sentences`"""
        raise NotImplementedError('Implement this function')

    def get_all_texts(self):
        texts = []
        for name, var in sorted(self.__dict__.items()):
            if isinstance(var, KorpusData):
                texts += var.get_all_texts()
        return texts

    def save(self, root_dir):
        """save prorce` to `sentences`"""
        raise NotImplementedError('Implement this function')
