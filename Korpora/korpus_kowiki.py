import os
from .korpora import Korpus, SentencePairKorpusData
from .utils import fetch, default_korpora_path, load_wikitext


KOWIKI_FETCH_INFORMATION = [
    {
        'url': 'https://github.com/lovit/kowikitext/releases/download/kowikitext.20200920.v2/kowikitext_20200920.train.zip',
        'destination': 'kowikitext/kowikitext_20200920.train.zip',
        'method': 'download & unzip'
    },
    {
        'url': 'https://github.com/lovit/kowikitext/releases/download/kowikitext.20200920.v2/kowikitext_20200920.test.zip',
        'destination': 'kowikitext/kowikitext_20200920.test.zip',
        'method': 'download & unzip'
    },
    {
        'url': 'https://github.com/lovit/kowikitext/releases/download/kowikitext.20200920.v2/kowikitext_20200920.dev.zip',
        'destination': 'kowikitext/kowikitext_20200920.dev.zip',
        'method': 'download & unzip'
    }
]

description = """    Author : Hyunjoong Kim lovit@github
    Repository : https://github.com/lovit/kowikitext
    References :

    한국어 위키피디아의 덤프 데이터를 바탕을 제작한 wikitext 형식의 텍스트 파일입니다.
    학습 및 평가를 위하여 위키페이지 별로 train (99%), dev (0.5%), test (0.5%) 로 나뉘어져있습니다.
"""

license = "    CC-BY-SA 3.0 which kowiki dump dataset is licensed"


class KowikiTextKorpus(Korpus):
    def __init__(self, root_dir=None, force_download=False):
        super().__init__(description, license)

        if root_dir is None:
            root_dir = default_korpora_path
        fetch_kowikitext(root_dir, force_download)

        for information in KOWIKI_FETCH_INFORMATION:
            destination = information['destination']
            local_path = os.path.join(os.path.abspath(root_dir), destination[:-4])

            if 'train' in destination:
                response = input(
                    'kowikiText.train text file is large (1.6G).\n'
                    'If you want to load text in your memory, please insert `yes`\n'
                    'If the `INPUT` is integer, it loads only first `INPUT` sentences\n').lower()
                if (len(response) == 1 and response == 'y') or (response == 'yes'):
                    texts, titles = self.load(local_path)
                    self.train = SentencePairKorpusData('KowikiText.train', texts, titles)
                elif response.isdigit():
                    texts, titles = self.load(local_path, num_lines=int(response))
                    self.train = SentencePairKorpusData('KowikiText.train', texts, titles)
                else:
                    dirname = os.path.abspath(f'{root_dir}/kowikitext')
                    self.train = f'kowikitext corpus is downloaded. Open local directory {dirname}'
                    print('Continue to load `dev` and `test`')
                continue

            texts, titles = self.load(local_path)
            if 'dev' in destination:
                self.dev = SentencePairKorpusData('KowikiText.dev', texts, titles)
            elif 'test' in destination:
                self.test = SentencePairKorpusData('KowikiText.test', texts, titles)
            else:
                raise ValueError(f'Check local files')

    def load(self, path, num_lines=-1):
        def split_title_text(wikitext):
            lines = wikitext.split('\n')
            title = lines[0]
            text = '\n'.join([line.strip() for line in lines[2:] if line.strip()])
            return title, text

        wikitexts = load_wikitext(path, num_lines)
        wikitexts = [split_title_text(wikitext) for wikitext in wikitexts]
        titles, texts = zip(*wikitexts)
        # swap position
        return texts, titles


def fetch_kowikitext(root_dir, force_download):
    for information in KOWIKI_FETCH_INFORMATION:
        url = information['url']
        destination = information['destination']
        local_path = os.path.join(os.path.abspath(root_dir), destination)
        fetch(url, local_path, 'kowikitext', force_download, information['method'])
