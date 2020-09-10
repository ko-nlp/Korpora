import os
import platform

from .korpora import Korpus, KorpusData
from .utils import fetch, load_text, default_korpora_path


KCBERT_FETCH_INFORMATION = [
    {
        'url': 'https://github.com/Beomi/KcBERT/releases/download/TrainData_v1/kcbert-train.tar.gzaa',
        'destination': 'kcbert/kcbert-train.tar.gzaa',
        'method': 'download'
    },
    {
        'url': 'https://github.com/Beomi/KcBERT/releases/download/TrainData_v1/kcbert-train.tar.gzab',
        'destination': 'kcbert/kcbert-train.tar.gzab',
        'method': 'download'
    },
    {
        'url': 'https://github.com/Beomi/KcBERT/releases/download/TrainData_v1/kcbert-train.tar.gzac',
        'destination': 'kcbert/kcbert-train.tar.gzac',
        'method': 'download'
    }
]

description = """     Author : beomi@github
    Repository : https://github.com/Beomi/KcBERT/
    References :

    공개된 한국어 BERT는 대부분 한국어 위키, 뉴스 기사, 책 등 잘 정제된 데이터를 기반으로 학습한 모델입니다.

    한편, 실제로 NSMC와 같은 댓글형 데이터셋은 정제되지 않았고 구어체 특징에 신조어가 많으며,
    오탈자 등 공식적인 글쓰기에서 나타나지 않는 표현들이 빈번하게 등장합니다.

    KcBERT는 위와 같은 특성의 데이터셋에 적용하기 위해, 네이버 뉴스에서 댓글과 대댓글을 수집해,
    토크나이저와 BERT모델을 처음부터 학습한 Pretrained BERT 모델입니다.

    KcBERT는 Huggingface의 Transformers 라이브러리를 통해 간편히 불러와 사용할 수 있습니다.
    (별도의 파일 다운로드가 필요하지 않습니다.)"""

license = """    MIT License"""


class KcBERTData(KorpusData):
    def __init__(self, description, texts):
        super().__init__(description, texts)


class KcBERTKorpus(Korpus):
    def __init__(self, root_dir=None, force_download=False):
        super().__init__(description, license)

        if root_dir is None:
            root_dir = default_korpora_path
        fetch_kcbert(root_dir, force_download)

        response = input('KcBERT text file is large (12G).'
              'If you want to load text in your memory, please insert `yes`').lower()
        if (len(response) == 1 and response == 'y') or (response == 'yes'):
            self.train = KcBERTData(
                description,
                load_text(f'{root_dir}/kcbert/20190101_20200611_v2.txt')
            )
        else:
            dirname = os.path.abspath(f'{root_dir}/kcbert')
            self.train = f'KcBERT corpus is downloaded. Open local directory {dirname}'


def fetch_kcbert(root_dir, force_download):
    for info in KCBERT_FETCH_INFORMATION:
        local_path = os.path.join(os.path.abspath(root_dir), info['destination'])
        fetch(info['url'], local_path, 'kcbert', force_download)

    if os.path.exists(f'{root_dir}/kcbert/20190101_20200611_v2.txt'):
        return None

    if platform.system().lower() == 'windows':
        print('Korpora does not support KcBERT fetch in Windows OS.'
              f'Please open local directory {root_dir} and unzip manually tar files')
        return None

    cwd = os.getcwd()
    print('Unzip tar. It needs a few minutes ... ', end='')
    os.chdir(f'{root_dir}/kcbert/')
    os.system("cat kcbert-train.tar.gz* | tar -zxvpf -")
    print('done')
    os.chdir(cwd)
