from dataclasses import dataclass
from typing import List, Union


@dataclass
class KorpusData:
    description: str
    texts: List[str]

    def __len__(self):
        return len(self.texts)

    def __getitem__(self):
        raise NotImplementedError('Implement __getitem__')

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

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


@dataclass
class LabeledSentence:
    text: str
    label: Union[int, float, str, bool]


class LabeledSentenceKorpusData(KorpusData):
    pairs: List[str]

    def __init__(self, description, texts, labels):
        if not (len(texts) == len(labels)):
            raise ValueError('All two arguments must be same length')
        super().__init__(description, texts)
        self.labels = labels

    def __getitem__(self, index):
        return SentencePair(self.texts[index], self.labels[index])

    def get_all_labeled_sentences(self):
        return [LabeledSentence(s, l) for s, l in zip(self.texts, self.labels)]


@dataclass
class SentencePair:
    text: str
    pair: str


class SentencePairKorpusData(KorpusData):
    pairs: List[str]

    def __init__(self, description, texts, pairs):
        if not (len(texts) == len(pairs)):
            raise ValueError('All two arguments must be same length')
        super().__init__(description, texts)
        self.pairs = pairs

    def __getitem__(self, index):
        return SentencePair(self.texts[index], self.pairs[index])

    def get_all_pairs(self):
        return [SentencePair(s, p) for s, p in zip(self.texts, self.pairs)]


@dataclass
class LabeledSentencePair:
    text: str
    pair: str
    label: Union[str, int, float, bool]


class LabeledSentencePairKorpusData(KorpusData):
    pairs: List[str]
    labels: List

    def __init__(self, description, texts, pairs, labels):
        if not (len(texts) == len(pairs) == len(labels)):
            raise ValueError('All three arguments must be same length')
        super().__init__(description, texts)
        self.pairs = pairs
        self.labels = labels

    def __getitem__(self, index):
        return LabeledSentencePair(self.texts[index], self.pairs[index], self.labels[index])

    def get_all_pairs(self):
        return [SentencePair(s, p) for s, p in zip(self.texts, self.pairs)]

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

    def __init__(self, description, texts, words, tags):
        if not (len(texts) == len(words) == len(tags)):
            raise ValueError('All three arguments must be same length')
        super().__init__(description, texts)
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
        s = f"{classname}\n{self.description}\n\nAttributes\n"
        for name, var in self.__dict__.items():
            if name not in {'description', 'license', 'self'}:
                s += f' {classname}.{name} : size={len(var)}\n'
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
