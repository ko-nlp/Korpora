import os
from typing import List

from .korpora import Korpus, LabeledSentencePairKorpusData, LabeledSentenceKorpusData, SentencePairKorpusData
from .utils import load_text


class CustomLabeledSentencePairKorpus(Korpus):
    """
    We assume that all custom LabeledSentencePair files are in `tap-separated text` format

        sent a\tsent b\tlabel_ab
        sent c\tsent d\tlabel_cd

    Examples:
        If custom corpus text files have no header

            >>> paths = [
            >>>     'path/to/mycorpus/train.tsv',
            >>>     'path/to/mycorpus/test.tsv',
            >>> ]
            >>> custom_korpus = CustomLabeledSentencePairKorpus(paths)

        If these files have headers

            >>> paths = [
            >>>     'path/to/mycorpus/train.tsv',
            >>>     'path/to/mycorpus/test.tsv',
            >>> ]
            >>> custom_korpus = CustomLabeledSentencePairKorpus(
            >>>     paths, num_headers=num_headers)
    """
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
    """
    We assume that all custom LabeledSentence files are in `tap-separated text` format

        sent 1\tlabel_1
        sent 2\tlabel_2

    Examples:
        If custom corpus text files have no header

            >>> paths = [
            >>>     'path/to/mycorpus/train.tsv',
            >>>     'path/to/mycorpus/test.tsv',
            >>> ]
            >>> custom_korpus = CustomLabeledSentenceKorpus(paths)

        If these files have headers

            >>> paths = [
            >>>     'path/to/mycorpus/train.tsv',
            >>>     'path/to/mycorpus/test.tsv',
            >>> ]
            >>> custom_korpus = CustomLabeledSentenceKorpus(
            >>>     paths, num_headers=num_headers)
    """
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
    We assume that all custom SentencePair files are in `tap-separated text` format

        sent a\tsent b
        sent c\tsent d

    Examples:
        If custom corpus text files have no header

            >>> paths = [
            >>>     'path/to/mycorpus/train.tsv',
            >>>     'path/to/mycorpus/test.tsv',
            >>> ]
            >>> custom_korpus = CustomSentencePairKorpus(paths)

        If these files have headers

            >>> paths = [
            >>>     'path/to/mycorpus/train.tsv',
            >>>     'path/to/mycorpus/test.tsv',
            >>> ]
            >>> custom_korpus = CustomSentencePairKorpus(
            >>>     paths, num_headers=num_headers)
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
