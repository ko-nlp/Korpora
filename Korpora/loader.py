from .korpus_aihub_translation import (
    AIHubTranslationKorpus,
    AIHubSpokenTranslationKorpus,
    AIHubConversationTranslationKorpus,
    AIHubNewsTranslationKorpus,
    AIHubKoreanCultureTranslationKorpus,
    AIHubDecreeTranslationKorpus,
    AIHubGovernmentWebsiteTranslationKorpus,
    fetch_aihub
)
from .korpus_chatbot_data import KoreanChatbotKorpus, fetch_chatbot
from .korpus_kcbert import KcBERTKorpus, fetch_kcbert
from .korpus_korean_hate_speech import KoreanHateSpeechKorpus, fetch_korean_hate_speech
from .korpus_korean_parallel import KoreanParallelKOENNewsKorpus, fetch_korean_parallel_koen_news
from .korpus_korean_petitions import KoreanPetitionsKorpus, fetch_korean_petitions
from .korpus_kornli import KorNLIKorpus, fetch_kornli
from .korpus_korsts import KorSTSKorpus, fetch_korsts
from .korpus_kowiki import KowikiTextKorpus, fetch_kowikitext
from .korpus_namuwiki import NamuwikiTextKorpus, fetch_namuwikitext
from .korpus_naverchangwon_ner import NaverChangwonNERKorpus, fetch_naverchangwon_ner
from .korpus_nsmc import NSMCKorpus, fetch_nsmc
from .korpus_question_pair import QuestionPairKorpus, fetch_questionpair
from .korpus_open_subtitles import OpenSubtitleKorpus, fetch_open_subtitles
from .korpus_modu_news import ModuNewsKorpus, fetch_modu
from .korpus_modu_messenger import ModuMessengerKorpus
from .korpus_modu_morpheme import ModuMorphemeKorpus
from .korpus_modu_ne import ModuNEKorpus
from .korpus_modu_spoken import ModuSpokenKorpus
from .korpus_modu_web import ModuWebKorpus
from .korpus_modu_written import ModuWrittenKorpus
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
        corpora = [KORPUS[corpus_name](root_dir, force_download) for corpus_name in corpus_names]
        if return_single:
            return corpora[0]
        return corpora

    @classmethod
    def fetch(cls, corpus_name, root_dir=None, force_download=False):
        if corpus_name.lower() == 'all':
            corpus_name = sorted(FETCH.keys())

        if isinstance(corpus_name, str):
            corpus_name = [corpus_name]

        corpus_name = [name for name in corpus_name if (name[:5] != 'modu_' and name[:6] != 'aihub_')]
        for name in corpus_name:
            if name not in FETCH:
                raise ValueError(f'Support only f{sorted(FETCH.keys())}')

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
    'korean_parallel_koen_news': KoreanParallelKOENNewsKorpus,
    'korean_petitions': KoreanPetitionsKorpus,
    'kornli': KorNLIKorpus,
    'korsts': KorSTSKorpus,
    'kowikitext': KowikiTextKorpus,
    'namuwikitext': NamuwikiTextKorpus,
    'naver_changwon_ner': NaverChangwonNERKorpus,
    'nsmc': NSMCKorpus,
    'question_pair': QuestionPairKorpus,
    'modu_news': ModuNewsKorpus,
    'modu_messenger': ModuMessengerKorpus,
    'modu_mp': ModuMorphemeKorpus,
    'modu_ne': ModuNEKorpus,
    'modu_spoken': ModuSpokenKorpus,
    'modu_web': ModuWebKorpus,
    'modu_written': ModuWrittenKorpus,
    'open_subtitles': OpenSubtitleKorpus,
    'aihub_translation': AIHubTranslationKorpus,
    'aihub_spoken_translation': AIHubSpokenTranslationKorpus,
    'aihub_conversation_translation': AIHubConversationTranslationKorpus,
    'aihub_news_translation': AIHubNewsTranslationKorpus,
    'aihub_korean_culture_translation': AIHubKoreanCultureTranslationKorpus,
    'aihub_decree_translation': AIHubDecreeTranslationKorpus,
    'aihub_government_website_translation': AIHubGovernmentWebsiteTranslationKorpus,
}

KORPUS_DESCRIPTION = {
    'kcbert': "beomi@github 님이 만드신 KcBERT 학습데이터",
    'korean_chatbot_data': "songys@github 님이 만드신 챗봇 문답 데이터",
    'korean_hate_speech': "{inmoonlight,warnikchow,beomi}@github 님이 만드신 혐오댓글데이터",
    'korean_parallel_koen_news': "jungyeul@github 님이 만드신 병렬 말뭉치",
    'korean_petitions': "lovit@github 님이 만드신 2017.08 ~ 2019.03 청와대 청원데이터",
    'kornli': "KakaoBrain 에서 제공하는 Natural Language Inference (NLI) 데이터",
    'korsts': "KakaoBrain 에서 제공하는 Semantic Textual Similarity (STS) 데이터",
    'kowikitext': "lovit@github 님이 만드신 wikitext 형식의 한국어 위키피디아 데이터",
    'namuwikitext': "lovit@github 님이 만드신 wikitext 형식의 나무위키 데이터",
    'naver_changwon_ner': "네이버 + 창원대 NER shared task data",
    'nsmc': "e9t@github 님이 만드신 Naver sentiment movie corpus v1.0",
    'question_pair': "songys@github 님이 만드신 질문쌍(Paired Question v.2)",
    'modu_news': '국립국어원에서 만든 모두의 말뭉치: 뉴스 말뭉치',
    'modu_messenger': '국립국어원에서 만든 모두의 말뭉치: 메신저 말뭉치',
    'modu_mp': '국립국어원에서 만든 모두의 말뭉치: 형태 분석 말뭉치',
    'modu_ne': '국립국어원에서 만든 모두의 말뭉치: 개체명 분석 말뭉치',
    'modu_spoken': '국립국어원에서 만든 모두의 말뭉치: 구어 말뭉치',
    'modu_web': '국립국어원에서 만든 모두의 말뭉치: 웹 말뭉치',
    'modu_written': '국립국어원에서 만든 모두의 말뭉치: 문어 말뭉치',
    'open_subtitles': 'Open parallel corpus (OPUS) 에서 제공하는 영화 자막 번역 병렬 말뭉치',
    'aihub_translation': "AI Hub 에서 제공하는 번역용 병렬 말뭉치 (구어 + 대화 + 뉴스 + 한국문화 + 조례 + 지자체웹사이트)",
    'aihub_spoken_translation': "AI Hub 에서 제공하는 번역용 병렬 말뭉치 (구어)",
    'aihub_conversation_translation': "AI Hub 에서 제공하는 번역용 병렬 말뭉치 (대화)",
    'aihub_news_translation': "AI Hub 에서 제공하는 번역용 병렬 말뭉치 (뉴스)",
    'aihub_korean_culture_translation': "AI Hub 에서 제공하는 번역용 병렬 말뭉치 (한국문화)",
    'aihub_decree_translation': "AI Hub 에서 제공하는 번역용 병렬 말뭉치 (조례)",
    'aihub_government_website_translation': "AI Hub 에서 제공하는 번역용 병렬 말뭉치 (지자체웹사이트)",
}

FETCH = {
    'kcbert': fetch_kcbert,
    'korean_chatbot_data': fetch_chatbot,
    'korean_hate_speech': fetch_korean_hate_speech,
    'korean_parallel_koen_news': fetch_korean_parallel_koen_news,
    'korean_petitions': fetch_korean_petitions,
    'kornli': fetch_kornli,
    'korsts': fetch_korsts,
    'kowikitext': fetch_kowikitext,
    'namuwikitext': fetch_namuwikitext,
    'naver_changwon_ner': fetch_naverchangwon_ner,
    'nsmc': fetch_nsmc,
    'question_pair': fetch_questionpair,
    'modu_news': fetch_modu,
    'modu_messenger': fetch_modu,
    'modu_mp': fetch_modu,
    'modu_ne': fetch_modu,
    'modu_spoken': fetch_modu,
    'modu_web': fetch_modu,
    'modu_written': fetch_modu,
    'open_subtitles': fetch_open_subtitles,
    'aihub_translation': fetch_aihub,
    'aihub_spoken_translation': fetch_aihub,
    'aihub_conversation_translation': fetch_aihub,
    'aihub_news_translation': fetch_aihub,
    'aihub_korean_culture_translation': fetch_aihub,
    'aihub_decree_translation': fetch_aihub,
    'aihub_government_website_translation': fetch_aihub,
}