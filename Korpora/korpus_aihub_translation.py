import os
import xlrd
from glob import glob
from tqdm import tqdm

from Korpora.korpora import Korpus, SentencePairKorpusData
from Korpora.utils import default_korpora_path


description = """    AI Hub 에서는 학습용 데이터를 제공합니다.

    데이터를 활용하기 위해서는 아래 주소의 홈페이지에서 "AI데이터" 클릭 후,
    이용하려는 데이터마다 직접 신청을 하셔야 합니다.

    https://www.aihub.or.kr/

    AI Hub 학습데이터는 신청 즉시 자동 승인됩니다.
    Korpora>=0.2.0 에서는 로컬에 다운로드 된 말뭉치를 손쉽게 로딩하는 기능만 제공합니다.

    AI Hub 에서 제공하는 번역데이터는 압축파일 또는 엑셀파일 (확장자: xlsx) 형식입니다.
    압축 해제 시 다음의 한글로 파일 이름이 기록되어 있습니다.
    파일 이름을 한글로 기록할 경우 OS 에 따라 예상치 못한 문제들이 발생할 수 있습니다.

    그러므로 각 파일의 이름을 아래처럼 영어로 변경하였다고 가정합니다.

             한글 파일 이름                         영어 파일 이름
        --------------------------------------------------------------
        1_구어체(1)_200226.xlsx         ->  1_spoken(1)_200226.xlsx
        1_구어체(2)_200226.xlsx         ->  1_spoken(2)_200226.xlsx
        2_대화체_200226.xlsx            ->  2_conversation_200226.xlsx
        3_문어체_뉴스(1)_200226.xlsx     ->  3_news(1)_200226.xlsx
        3_문어체_뉴스(2)_200226.xlsx     ->  3_news(2)_200226.xlsx
        3_문어체_뉴스(3)_200226.xlsx     ->  3_news(3)_200226.xlsx
        3_문어체_뉴스(4)_200226.xlsx     ->  3_news(4)_200226.xlsx
        4_문어체_한국문화_200226.xlsx     ->  4_korean_culture_200226.xlsx
        5_문어체_조례_200226.xlsx        ->  5_decree_200226.xlsx
        6_문어체_지자체웹사이트_200226.xlsx ->  6_government_website_200226.xlsx

    위 파일들은 `~/Korpora/AIHub_Translation/` 혹은 `path/to/AIHub_Translation/` 에
    저장되었다고 가정합니다.

    (Korpora 개발진 lovit@github, ratsgo@github)"""

license = """    AI Hub 에서 제공하는 데이터의 소유권 및 전문은 다음의 주소에서 확인할 수 있습니다.

    https://aihub.or.kr/form/iyongyaggwan

    제16조 포털의 소유권
    1. AI 허브가 제공하는 서비스, 그에 필요한 소프트웨어, 이미지, 마크, 로고, 디자인, 서비스명칭, 정보 및
       상표 등과 관련된 지식재산권 및 기타 권리는 운영기관(및 AI허브 서비스 제공과 관련하여 운영기관과 계약을
       체결한 기관)에 소유권이 있습니다.
    2. 귀하는 AI 허브에서 명시적으로 승인한 경우를 제외하고는 전항의 소정의 각 재산에 대한 전부 또는 일부의 수정,
       대여, 대출, 판매, 배포, 제작, 양도, 재라이센스, 담보권 설정 행위, 상업적 이용 행위를 할 수 없으며,
       제3자로 하여금 이와 같은 행위를 하도록 허락할 수 없습니다"""


class AIHubTranslationKorpus(Korpus):
    def __init__(self, root_dir=None, force_download=False, prefix='', name='AIHub_translation'):
        super().__init__(description, license)
        if root_dir is None:
            root_dir = os.path.join(default_korpora_path, 'AIHub_Translation', prefix)
        elif isinstance(root_dir, str) and os.path.isdir(root_dir):
            root_dir = os.path.join(root_dir, prefix)
        paths = find_corpus_paths(root_dir)
        self.train = SentencePairKorpusData(
            f'{name}.train',
            *load_aihub_translation(paths, name)
        )


class AIHubSpokenTranslationKorpus(AIHubTranslationKorpus):
    def __init__(self, root_dir=None, force_download=False):
        super().__init__(root_dir, force_download, '1_spoken*', 'AIHub_spoken_translation')


class AIHubConversationTranslationKorpus(AIHubTranslationKorpus):
    def __init__(self, root_dir=None, force_download=False):
        super().__init__(root_dir, force_download, '2_conversation*', 'AIHub_conversation_translation')


class AIHubNewsTranslationKorpus(AIHubTranslationKorpus):
    def __init__(self, root_dir=None, force_download=False):
        super().__init__(root_dir, force_download, '3_news*', 'AIHub_news_translation')


class AIHubKoreanCultureTranslationKorpus(AIHubTranslationKorpus):
    def __init__(self, root_dir=None, force_download=False):
        super().__init__(root_dir, force_download, '4_korean_culture*', 'AIHub_korean_culture_translation')


class AIHubDecreeTranslationKorpus(AIHubTranslationKorpus):
    def __init__(self, root_dir=None, force_download=False):
        super().__init__(root_dir, force_download, '5_decree*', 'AIHub_decree_translation')


class AIHubGovernmentWebsiteTranslationKorpus(AIHubTranslationKorpus):
    def __init__(self, root_dir=None, force_download=False):
        super().__init__(root_dir, force_download, '6_government_website*', 'AIHub_government_website_translation')


def find_corpus_paths(root_dir, suffix='200226.xlsx'):
    def match(path):
        return path[-11:] == suffix

    # directory + wildcard
    if isinstance(root_dir, str):
        paths = sorted(glob(f'{root_dir}/*{suffix}') + glob(root_dir))
    else:
        paths = root_dir

    paths = [path for path in paths if match(path)]
    if not paths:
        raise ValueError('Not found corpus files. Check `root_dir`')
    return paths


def load_aihub_translation(paths, name):
    sources, targets = [], []
    for i_path, path in enumerate(tqdm(paths, desc=f'Loading {name}', total=len(paths))):
        workbook = xlrd.open_workbook(path)
        sheet = workbook.sheet_by_index(0)
        header = sheet.row(0)
        if not (header[-2].value.strip() == '원문' and header[-1].value.strip() == '번역문'):
            raise ValueError(f'The second last column and last column in header must be ("원문", "번역문")')
        for i_row in range(1, sheet.nrows):
            row = sheet.row(i_row)
            sources.append(row[-2].value.strip())
            targets.append(row[-1].value.strip())
    return sources, targets


def fetch_aihub(root_dir=None, force_download=False):
    raise NotImplementedError(
        "https://www.aihub.or.kr/ 에서 개별 신청 후 직접 데이터를 받으셔야 합니다."
        "\n이에 따라 AI Hub 의 말뭉치는 fetch 기능을 제공하지 않습니다"
    )
