from .korpora_korean_petitions import KoreanPetitions, fetch_korean_petitions
from .korpora_kornli import KorNLI, fetch_kornli
from .korpora_korsts import KorSTS, fetch_korsts
from .korpora_namu_wiki import NamuwikiTextKorpus, fetch_namuwikitext
from .korpora_nsmc import NSMC, fetch_nsmc
from .korpora_chatbot_data import KoreanChatbotKorpus, fetch_chatbot
from .korpora_question_pair import QuestionPairKorpus, fetch_questionpair
from .korpora_nc_ner import NaverChangwonNERKorpus, fetch_nc_ner
from .korpora_korean_hate_speech import KoreanHateSpeech, fetch_korean_hate_speech
from .utils import default_korpora_path


class Korpora:
    """
    Examples::
        >>> from Korpora import Korpora
        >>> nsmc = Korpora.load('nsmc')
        >>> len(nsmc.train.texts)   # 150000
        >>> len(nsmc.train.labels)  # 50000
    """
    @classmethod
    def load(cls, corpus_names, root_dir=None, force_download=False):
        return_single = isinstance(corpus_names, str)
        if return_single:
            corpus_names = [corpus_names]

        if root_dir is None:
            root_dir = default_korpora_path

        corpora = [KORPORA[corpus_name](root_dir, force_download) for corpus_name in corpus_names]
        if return_single:
            return corpora[0]
        return corpora

    @classmethod
    def fetch(cls, corpus_name, root_dir=None, force_download=False):
        if corpus_name.lower() == 'all':
            corpus_name = sorted(FETCH.keys())
        elif corpus_name not in FETCH:
            raise ValueError(f'Support only f{sorted(FETCH.keys())}')

        if isinstance(corpus_name, str):
            corpus_name = [corpus_name]

        if root_dir is None:
            root_dir = default_korpora_path

        for name in corpus_name:
            fetch_func = FETCH[name]
            fetch_func(root_dir, force_download)


KORPORA = {
    'namuwikitext': NamuwikiTextKorpus,
    'nsmc': NSMC,
    'korean_petitions': KoreanPetitions,
    'korean_hate_speech': KoreanHateSpeech,
    'korean_chatbot_data': KoreanChatbotKorpus,
    'kornli': KorNLI,
    'korsts': KorSTS,
    'naver_changwon_ner': NaverChangwonNERKorpus,
    'question_pair': QuestionPairKorpus,
}

FETCH = {
    'namuwikitext': fetch_namuwikitext,
    'nsmc': fetch_nsmc,
    'korean_petitions': fetch_korean_petitions,
    'korean_hate_speech': fetch_korean_hate_speech,
    'korean_chatbot_data': fetch_chatbot,
    'kornli': fetch_kornli,
    'korsts': fetch_korsts,
    'naver_changwon_ner': fetch_nc_ner,
    'question_pair': fetch_questionpair,
}