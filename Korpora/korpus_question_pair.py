import os
import csv

from .korpora import Korpus, LabeledSentencePairKorpusData
from .utils import fetch, default_korpora_path


QUESTION_PAIR_FETCH_INFORMATION = [
    {
        'url': 'https://raw.githubusercontent.com/songys/Question_pair/master/kor_pair_train.csv',
        'destination': 'question_pair/kor_pair_train.csv',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/songys/Question_pair/master/kor_Pair_test.csv',
        'destination': 'question_pair/kor_pair_test.csv',
        'method': 'download'
    },
]

description = """     Author : songys@github
    Repository : https://github.com/songys/Question_pair
    References :

    질문쌍(Paired Question v.2)
    짝 지어진 두 개의 질문이 같은 질문인지 다른 질문인지 핸드 레이블을 달아둔 데이터
    사랑, 이별, 또는 일상과 같은 주제로 도메인 특정적이지 않음"""

license = """    Creative Commons Attribution-ShareAlike license (CC BY-SA 4.0)
    Details in https://creativecommons.org/licenses/by-sa/4.0/"""


class QuestionPairData(LabeledSentencePairKorpusData):
    def __init__(self, description, texts, pairs, labels):
        super().__init__(description, texts, pairs, labels)


class QuestionPairKorpus(Korpus):
    def __init__(self, root_dir=None, force_download=False):
        super().__init__(description, license)

        if root_dir is None:
            root_dir = default_korpora_path
        fetch_questionpair(root_dir, force_download)

        for info in QUESTION_PAIR_FETCH_INFORMATION:
            local_path = os.path.join(os.path.abspath(root_dir), info['destination'])
            is_train = 'train' in info['destination']
            with open(local_path, 'r', encoding='utf-8') as f:
                texts, pairs, labels = self.cleaning(csv.reader(f, delimiter=','), is_train)
                data = QuestionPairData(self.description, texts, pairs, labels)
            if is_train:
                self.train = data
            else:
                self.test = data

    def cleaning(self, examples, is_train):
        next(examples)  # skip head
        examples = [example for example in examples]
        for i, example in enumerate(examples):
            if (is_train and len(example) != 6) or (not is_train and len(example) != 5):
                raise ValueError(f'Found some errors in line {i}: {example}')
        if is_train:
            # train data column names : id, qid1, qid2, question1, question2, is_duplicate
            _, _, _, texts, pairs, labels = zip(*examples)
        else:
            # test data column names : test_id, question1, question2, is_duplicate, blank
            _, texts, pairs, labels, _ = zip(*examples)
        return texts, pairs, labels

    def get_all_texts(self):
        return self.train.get_all_texts() + self.test.get_all_texts()

    def get_all_pairs(self):
        return self.train.get_all_pairs() + self.test.get_all_pairs()

    def get_all_labels(self):
        return self.train.get_all_labels() + self.test.get_all_labels()


def fetch_questionpair(root_dir, force_download):
    for info in QUESTION_PAIR_FETCH_INFORMATION:
        local_path = os.path.join(os.path.abspath(root_dir), info['destination'])
        fetch(info['url'], local_path, 'question_pair', force_download)
