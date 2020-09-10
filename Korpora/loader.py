from .korpus_chatbot_data import KoreanChatbotKorpus, fetch_chatbot
from .korpus_kcbert import KcBERTKorpus, fetch_kcbert
from .korpus_korean_hate_speech import KoreanHateSpeechKorpus, fetch_korean_hate_speech
from .korpus_korean_petitions import KoreanPetitionsKorpus, fetch_korean_petitions
from .korpus_kornli import KorNLIKorpus, fetch_kornli
from .korpus_korsts import KorSTSKorpus, fetch_korsts
from .korpus_namuwiki import NamuwikiTextKorpus, fetch_namuwikitext
from .korpus_naverchangwon_ner import NaverChangwonNERKorpus, fetch_naverchangwon_ner
from .korpus_nsmc import NSMCKorpus, fetch_nsmc
from .korpus_question_pair import QuestionPairKorpus, fetch_questionpair
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

        corpora = [KORPUS[corpus_name](root_dir, force_download) for corpus_name in corpus_names]
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

    @classmethod
    def corpus_list(cls):
        return KORPUS_DESCRIPTION


KORPUS = {
    'kcbert': KcBERTKorpus,
    'korean_chatbot_data': KoreanChatbotKorpus,
    'korean_hate_speech': KoreanHateSpeechKorpus,
    'korean_petitions': KoreanPetitionsKorpus,
    'kornli': KorNLIKorpus,
    'korsts': KorSTSKorpus,
    'namuwikitext': NamuwikiTextKorpus,
    'naver_changwon_ner': NaverChangwonNERKorpus,
    'nsmc': NSMCKorpus,
    'question_pair': QuestionPairKorpus,
}

KORPUS_DESCRIPTION = {
    'kcbert': "beomi@github 님이 만드신 KcBERT 학습데이터",
    'korean_chatbot_data': "songys@github 님이 만드신 챗봇 문답 데이터",
    'korean_hate_speech': "{inmoonlight,warnikchow,beomi}@github 님이 만드신 혐오댓글데이터",
    'korean_petitions': "lovit@github 님이 만드신 2017.08 ~ 2019.03 청와대 청원데이터",
    'kornli': "KakaoBrain 에서 제공하는 Natural Language Inference (NLI) 데이터",
    'korsts': "KakaoBrain 에서 제공하는 Semantic Textual Similarity (STS) 데이터",
    'namuwikitext': "lovit@github 님이 만드신 wikitext 형식의 나무위키 데이터",
    'naver_changwon_ner': "네이버 + 창원대 NER shared task data",
    'nsmc': "e9t@github 님이 만드신 Naver sentiment movie corpus v1.0",
    'question_pair': "songys@github 님이 만드신 질문쌍(Paired Question v.2)",
}

FETCH = {
    'kcbert': fetch_kcbert,
    'korean_chatbot_data': fetch_chatbot,
    'korean_hate_speech': fetch_korean_hate_speech,
    'korean_petitions': fetch_korean_petitions,
    'kornli': fetch_kornli,
    'korsts': fetch_korsts,
    'namuwikitext': fetch_namuwikitext,
    'naver_changwon_ner': fetch_naverchangwon_ner,
    'nsmc': fetch_nsmc,
    'question_pair': fetch_questionpair,
}