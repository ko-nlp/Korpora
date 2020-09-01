import os
import csv
from typing import List

from .korpora import Korpus, LabeledSentencePairKorpusData
from .fetch import fetch
from .utils import check_path, default_korpora_path


class KoreanChatbotData(LabeledSentencePairKorpusData):
    answers:  List[str]
    labels: List[int]

    def __init__(self, description, texts, pairs, labels):
        super().__init__(
            description=description,
            texts=texts,
            pairs=pairs,
            labels=labels
        )

class KoreanChatbotCorpus(Korpus):
    """ Reference: https://github.com/songys/Chatbot_data

        Example
            {
                "question": "12시 땡!",
                "answer": "하루가 또 가네요.",
                "label": 0
            }
    """
    def __init__(self, root_dir=None, force_download=False):
        if root_dir is None:
            root_dir = default_korpora_path
        train_path = os.path.join(root_dir, 'korean_chatbot_data/ChatbotData.csv')
        if (force_download or not check_path(train_path)):
            fetch('korean_chatbot_data', root_dir)

        f = open(train_path, 'r', encoding='utf-8')
        questions, answers, labels = self.cleaning(csv.reader(f, delimiter=','))
        description = """    Chatbot_data_for_Korean v1.0
    1. 챗봇 트레이닝용 문답 페어 11,876개
    2. 일상다반사 0, 이별(부정) 1, 사랑(긍정) 2로 레이블링
    자세한 내용은 아래 repository를 참고하세요.

    https://github.com/songys/Chatbot_data
                """
        self.train = KoreanChatbotData(description, questions, answers, labels)
        self.description = description
        self.license = """    CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
    Details in https://creativecommons.org/publicdomain/zero/1.0/"""

    def cleaning(self, examples):
        next(examples) # skip head
        examples = [example for example in examples]
        for i_sent, example in enumerate(examples):
            if len(example) != 3:
                raise ValueError(f'Found some errors in line {i_sent}: {example}')
        questions, answers, labels = zip(*examples)
        labels = [int(label) for label in labels]
        return questions, answers, labels

    def get_all_texts(self):
        return self.train.texts

    def get_all_pairs(self):
        return self.train.get_all_pairs()

    def get_all_labels(self):
        return self.train.get_all_labels()
