import os
import csv

from .korpora import Korpus, LabeledSentencePairKorpusData
from .utils import fetch, default_korpora_path


KOREAN_CHATBOT_FETCH_INFORMATION = [
    {
        'url': 'https://raw.githubusercontent.com/songys/Chatbot_data/master/ChatbotData%20.csv',
        'destination': 'korean_chatbot_data/ChatbotData.csv',
        'method': 'download'
    }
]

description = """    Author : songys@github
    Repository : https://github.com/songys/Chatbot_data
    References :

    Chatbot_data_for_Korean v1.0
      1. 챗봇 트레이닝용 문답 페어 11,876개
      2. 일상다반사 0, 이별(부정) 1, 사랑(긍정) 2로 레이블링
    자세한 내용은 위의 repository를 참고하세요."""

license = """    CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
    Details in https://creativecommons.org/publicdomain/zero/1.0/"""


class KoreanChatbotData(LabeledSentencePairKorpusData):
    """
    Attributes:
        texts (list of str) : questions
        pairs (list of str) : answers
        labels (list of int) : categories

    See description for detail

        >>> print(str(kor_chat_data))  # or
        >>> print(kor_chat_data.description)
    """
    def __init__(self, description, texts, pairs, labels):
        super().__init__(
            description=description,
            texts=texts,
            pairs=pairs,
            labels=labels
        )


class KoreanChatbotKorpus(Korpus):
    """ Reference: https://github.com/songys/Chatbot_data

        Example
            {
                "question": "12시 땡!",
                "answer": "하루가 또 가네요.",
                "label": 0
            }
    """
    def __init__(self, root_dir=None, force_download=False):
        super().__init__(description, license)

        if root_dir is None:
            root_dir = default_korpora_path
        fetch_chatbot(root_dir, force_download)

        local_path = os.path.join(os.path.abspath(root_dir), KOREAN_CHATBOT_FETCH_INFORMATION[0]['destination'])
        with open(local_path, 'r', encoding='utf-8') as f:
            questions, answers, labels = self.cleaning(csv.reader(f, delimiter=','))
        self.train = KoreanChatbotData(description, questions, answers, labels)

    def cleaning(self, examples):
        next(examples) # skip head
        examples = [example for example in examples]
        for i_sent, example in enumerate(examples):
            if len(example) != 3:
                raise ValueError(f'Found some errors in line {i_sent}: {example}')
        questions, answers, labels = zip(*examples)
        labels = [int(label) for label in labels]
        return questions, answers, labels

    def get_all_pairs(self):
        return self.train.get_all_pairs()

    def get_all_labels(self):
        return self.train.get_all_labels()


def fetch_chatbot(root_dir, force_download):
    for information in KOREAN_CHATBOT_FETCH_INFORMATION:
        url = information['url']
        destination = information['destination']
        local_path = os.path.join(os.path.abspath(root_dir), destination)
        fetch(url, local_path, 'korean_chatbot_data', force_download, information['method'])