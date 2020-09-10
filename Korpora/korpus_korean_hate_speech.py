import os
from dataclasses import dataclass
from typing import List

from .korpora import Korpus, KorpusData, SentencePairKorpusData
from .utils import fetch, default_korpora_path, load_text


KOREAN_HATE_SPEECH_FETCH_INFORMATION = [
    {
        'url': 'https://raw.githubusercontent.com/kocohub/korean-hate-speech/master/unlabeled/unlabeled_comments_1.txt',
        'destination': 'korean_hate_speech/unlabeled/unlabeled_comments_1.txt',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/kocohub/korean-hate-speech/master/unlabeled/unlabeled_comments_2.txt',
        'destination': 'korean_hate_speech/unlabeled/unlabeled_comments_2.txt',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/kocohub/korean-hate-speech/master/unlabeled/unlabeled_comments_3.txt',
        'destination': 'korean_hate_speech/unlabeled/unlabeled_comments_3.txt',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/kocohub/korean-hate-speech/master/unlabeled/unlabeled_comments_4.txt',
        'destination': 'korean_hate_speech/unlabeled/unlabeled_comments_4.txt',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/kocohub/korean-hate-speech/master/unlabeled/unlabeled_comments_5.txt',
        'destination': 'korean_hate_speech/unlabeled/unlabeled_comments_5.txt',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/kocohub/korean-hate-speech/master/news_title/unlabeled_comments.news_title_1.txt',
        'destination': 'korean_hate_speech/news_title/unlabeled_comments.news_title_1.txt',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/kocohub/korean-hate-speech/master/news_title/unlabeled_comments.news_title_2.txt',
        'destination': 'korean_hate_speech/news_title/unlabeled_comments.news_title_2.txt',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/kocohub/korean-hate-speech/master/news_title/unlabeled_comments.news_title_3.txt',
        'destination': 'korean_hate_speech/news_title/unlabeled_comments.news_title_3.txt',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/kocohub/korean-hate-speech/master/news_title/unlabeled_comments.news_title_4.txt',
        'destination': 'korean_hate_speech/news_title/unlabeled_comments.news_title_4.txt',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/kocohub/korean-hate-speech/master/news_title/unlabeled_comments.news_title_5.txt',
        'destination': 'korean_hate_speech/news_title/unlabeled_comments.news_title_5.txt',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/kocohub/korean-hate-speech/master/news_title/dev.news_title.txt',
        'destination': 'korean_hate_speech/news_title/dev.news_title.txt',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/kocohub/korean-hate-speech/master/news_title/test.news_title.txt',
        'destination': 'korean_hate_speech/news_title/test.news_title.txt',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/kocohub/korean-hate-speech/master/news_title/train.news_title.txt',
        'destination': 'korean_hate_speech/news_title/train.news_title.txt',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/kocohub/korean-hate-speech/master/labeled/dev.tsv',
        'destination': 'korean_hate_speech/labeled/dev.tsv',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/kocohub/korean-hate-speech/master/labeled/train.tsv',
        'destination': 'korean_hate_speech/labeled/train.tsv',
        'method': 'download'
    },
    {
        'url': 'https://raw.githubusercontent.com/kocohub/korean-hate-speech/master/test.no_label.tsv',
        'destination': 'korean_hate_speech/test.no_label.tsv',
        'method': 'download'
    }
]

description = """    Authors :
        - Jihyung Moon* (inmoonlight@github)
        - Won Ik Cho* (warnikchow@github)
        - Junbum Lee (beomi@github)
        * equal contribution
    Repository : https://github.com/kocohub/korean-hate-speech
    References :
        - Moon, J., Cho, W. I., & Lee, J. (2020). BEEP! Korean Corpus of Online News
          Comments for Toxic Speech Detection. arXiv preprint arXiv:2005.12503.

    We provide the first human-annotated Korean corpus for toxic speech detection and the large unlabeled corpus.
    The data is comments from the Korean entertainment news aggregation platform."""

license = """    Creative Commons Attribution-ShareAlike 4.0 International License.
    Visit here for detail : https://creativecommons.org/licenses/by-sa/4.0/"""


class KoreanHateSpeechPairData(SentencePairKorpusData):
    def __init__(self, description, texts, labels):
        super().__init__(description, texts, labels)


@dataclass
class KoreanHateSpeechLabeledExample:
    text: str
    title: str
    gender_bias: str
    bias: str
    hate: str


class KoreanHateSpeechLabeledData(KorpusData):
    titles: List[str]
    gender_biases: List[str]
    biases: List[str]
    hates: List[str]

    def __init__(self, description, texts, titles, gender_biases, biases, hates):
        super().__init__(description, texts)
        if not (len(texts) == len(titles) == len(gender_biases) == len(biases) == len(hates)):
            raise ValueError('All five arguments must be same length')
        self.titles = titles
        self.gender_biases = gender_biases
        self.biases = biases
        self.hates = hates

    def __getitem__(self, index):
        return KoreanHateSpeechLabeledExample(
            self.texts[index],
            self.titles[index],
            self.gender_biases[index],
            self.biases[index],
            self.hates[index]
        )


class KoreanHateSpeechKorpus(Korpus):
    def __init__(self, root_dir=None, force_download=False):
        super().__init__(description, license)

        if root_dir is None:
            root_dir = default_korpora_path
        fetch_korean_hate_speech(root_dir, force_download)

        self.train = load_train(root_dir)
        self.dev = load_dev(root_dir)
        self.unlabeled = load_unlabeled(root_dir)
        self.test = load_test(root_dir)


def load_train(root_dir):
    # head : comments, contain_gender_bias, bias, hate
    text_labels = load_text(f'{root_dir}/korean_hate_speech/labeled/train.tsv', num_heads=1)
    titles = load_text(f'{root_dir}/korean_hate_speech/news_title/train.news_title.txt')
    if len(text_labels) != len(titles):
        raise ValueError(f'Found len(train.texts) != len(train.pairs). Do `fetch(force_download=True)`')
    texts, gender_biases, biases, hates = zip(*[line.split('\t') for line in text_labels])
    return KoreanHateSpeechLabeledData(description, texts, titles, gender_biases, biases, hates)


def load_dev(root_dir):
    # head : comments, contain_gender_bias, bias, hate
    text_labels = load_text(f'{root_dir}/korean_hate_speech/labeled/dev.tsv', num_heads=1)
    titles = load_text(f'{root_dir}/korean_hate_speech/news_title/dev.news_title.txt')
    if len(text_labels) != len(titles):
        raise ValueError(f'Found len(dev.texts) != len(dev.pairs). Do `fetch(force_download=True)`')
    texts, gender_biases, biases, hates = zip(*[line.split('\t') for line in text_labels])
    return KoreanHateSpeechLabeledData(description, texts, titles, gender_biases, biases, hates)


def load_unlabeled(root_dir):
    text_paths = [f'{root_dir}/korean_hate_speech/news_title/unlabeled_comments.news_title_{i}.txt' for i in range(1, 6)]
    title_paths = [f'{root_dir}/korean_hate_speech/news_title/unlabeled_comments.news_title_{i}.txt' for i in range(1, 6)]
    texts = []
    titles = []
    for text_path, title_path in zip(text_paths, title_paths):
        texts_ = load_text(text_path)
        titles_ = load_text(title_path)
        if len(texts_) != len(titles_):
            raise ValueError(f'Found some errors. not equal num of texts and titles. Do `fetch(force_download=True)`')
        texts += texts_
        titles += titles_
    return KoreanHateSpeechPairData(description, texts, titles)


def load_test(root_dir):
    text_path = f'{root_dir}/korean_hate_speech/test.no_label.tsv'
    title_path = f'{root_dir}/korean_hate_speech/news_title/test.news_title.txt'
    texts = load_text(text_path, num_heads=1)
    titles = load_text(title_path)
    if len(texts) != len(titles):
        raise ValueError(f'Found some errors. not equal num of texts and titles. Do `fetch(force_download=True)`')
    return KoreanHateSpeechPairData(description, texts, titles)


def fetch_korean_hate_speech(root_dir, force_download):
    for info in KOREAN_HATE_SPEECH_FETCH_INFORMATION:
        local_path = os.path.join(os.path.abspath(root_dir), info['destination'])
        fetch(info['url'], local_path, 'korean hate speech', force_download)
