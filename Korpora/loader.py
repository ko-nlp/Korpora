from .korpora_kcbert import KcBERT
from .korpora_korean_petitions import KoreanPetitions
from .korpora_kornli import KorNLI
from .korpora_korsts import KorSTS
from .korpora_namu_wiki import NamuwikiTextKorpus
from .korpora_nsmc import NSMC
from .korpora_chatbot_data import KoreanChatbotKorpus
from .korpora_question_pair import QuestionPairKorpus
from .korpora_nc_ner import NaverChangwonNERKorpus
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


KORPORA = {
    'namuwikitext': NamuwikiTextKorpus,
    'nsmc': NSMC,
    'kcbert': KcBERT,
    'korean_petitions': KoreanPetitions,
    'korean_chatbot_data': KoreanChatbotKorpus,
    'kornli': KorNLI,
    'korsts': KorSTS,
    'naver_changwon_ner': NaverChangwonNERKorpus,
    'question_pair': QuestionPairKorpus,
}
