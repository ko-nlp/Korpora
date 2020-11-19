from .about import __author__   # noqa: F401
from .about import __version__  # noqa: F401

from .korpus_aihub_translation import (
    AIHubTranslationKorpus,
    AIHubSpokenTranslationKorpus,
    AIHubConversationTranslationKorpus,
    AIHubNewsTranslationKorpus,
    AIHubKoreanCultureTranslationKorpus,
    AIHubDecreeTranslationKorpus,
    AIHubGovernmentWebsiteTranslationKorpus
)
from .korpus_chatbot_data import KoreanChatbotKorpus
from .korpus_custom import (
    CustomLabeledSentencePairKorpus,
    CustomLabeledSentenceKorpus,
    CustomSentencePairKorpus
)
from .korpus_kcbert import KcBERTKorpus
from .korpus_korean_hate_speech import KoreanHateSpeechKorpus
from .korpus_korean_parallel import KoreanParallelKOENNewsKorpus
from .korpus_korean_petitions import KoreanPetitionsKorpus
from .korpus_kornli import KorNLIKorpus
from .korpus_korsts import KorSTSKorpus
from .korpus_kowiki import KowikiTextKorpus
from .korpus_namuwiki import NamuwikiTextKorpus
from .korpus_naverchangwon_ner import NaverChangwonNERKorpus
from .korpus_nsmc import NSMCKorpus
from .korpus_question_pair import QuestionPairKorpus
from .korpus_open_subtitles import OpenSubtitleKorpus
from .loader import Korpora
from .korpus_modu_news import ModuNewsKorpus
from .korpus_modu_messenger import ModuMessengerKorpus
from .korpus_modu_morpheme import ModuMorphemeKorpus
from .korpus_modu_ne import ModuNEKorpus
from .korpus_modu_spoken import ModuSpokenKorpus
from .korpus_modu_web import ModuWebKorpus
from .korpus_modu_written import ModuWrittenKorpus
