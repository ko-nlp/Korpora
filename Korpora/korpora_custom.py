import os
from typing import List

from .korpora import Korpus, LabeledSentencePairKorpusData, LabeledSentenceKorpusData, SentencePairKorpusData
from .utils import load_text


class CustomLabeledSentencePairKorpus(Korpus):
    def __init__(self, paths, num_headers=0):
        super().__init__()
        for path in paths:
            attribute_name = get_attribute_name(path)
            raw_documents = load_text(path, num_heads=num_headers)
            texts, pairs, labels = self.cleaning(raw_documents)
            setattr(self, attribute_name, LabeledSentencePairKorpusData(
                'custom LabeledSentencePairKorpus', texts, pairs, labels))

    def cleaning(self, raw_documents: List[str], **kargs):
        examples = [example.split('\t') for example in raw_documents]
        for i_sent, columns in enumerate(examples):
            if len(columns) != 3:
                print(columns)
                raise ValueError(f'Found some errors in line {i_sent}: {examples[i_sent]}')
        texts, pairs, labels = zip(*examples)
        return texts, pairs, labels


class CustomLabeledSentenceKorpus(Korpus):
    def __init__(self, paths, num_headers=0):
        super().__init__()
        for path in paths:
            attribute_name = get_attribute_name(path)
            raw_documents = load_text(path, num_heads=num_headers)
            texts, labels = self.cleaning(raw_documents)
            setattr(self, attribute_name, LabeledSentenceKorpusData(
                'custom LabeledSentenceKorpus', texts, labels))

    def cleaning(self, raw_documents: List[str], **kargs):
        examples = [example.split('\t') for example in raw_documents]
        for i_sent, columns in enumerate(examples):
            if len(columns) != 2:
                print(columns)
                raise ValueError(f'Found some errors in line {i_sent}: {examples[i_sent]}')
        texts, labels = zip(*examples)
        return texts, labels


class CustomSentencePairKorpus(Korpus):
    """
    Examples:

        >>> paths = [
        >>>     '/Users/hyunjoongkim/Korpora/test/train.tsv',
        >>>     '/Users/hyunjoongkim/Korpora/test/test.tsv',
        >>> ]
        >>> custom_korpus = CustomSentencePairKorpus(paths)
    """
    def __init__(self, paths, num_headers=0):
        super().__init__()
        for path in paths:
            attribute_name = get_attribute_name(path)
            raw_documents = load_text(path, num_heads=num_headers)
            texts, pairs = self.cleaning(raw_documents)
            setattr(self, attribute_name, SentencePairKorpusData(
                'custom SentencePairKorpus', texts, pairs))

    def cleaning(self, raw_documents: List[str], **kargs):
        examples = [example.split('\t') for example in raw_documents]
        for i_sent, columns in enumerate(examples):
            if len(columns) != 2:
                print(columns)
                raise ValueError(f'Found some errors in line {i_sent}: {examples[i_sent]}')
        texts, pairs = zip(*examples)
        return texts, pairs


def get_attribute_name(path):
    if path[-4:] != '.tsv':
        raise ValueError('File must be format of tsv')
    name = os.path.basename(path)[:-4].replace('.', '_')
    return name
