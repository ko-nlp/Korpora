import os
from typing import List

from .korpora import Korpus
from .utils import fetch, default_korpora_path, load_text


KOREAN_HATE_SPEECH_CORPUS_INFORMATION = [
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


class KoreanHateSpeech(Korpus):
    def __init__(self, root_dir=None, force_download=False):
        super().__init__(description, license)

        if root_dir is None:
            root_dir = default_korpora_path
        fetch_korean_hate_speech(root_dir, force_download)


def fetch_korean_hate_speech(root_dir, force_download):
    for info in KOREAN_HATE_SPEECH_CORPUS_INFORMATION:
        local_path = os.path.join(os.path.abspath(root_dir), info['destination'])
        fetch(info['url'], local_path, 'korean hate speech', force_download)
