from .about import __author__   # noqa: F401
from .about import __version__  # noqa: F401

from .korpus_chatbot_data import KoreanChatbotKorpus
from .korpus_custom import (
    CustomLabeledSentencePairKorpus,
    CustomLabeledSentenceKorpus,
    CustomSentencePairKorpus
)
from .korpus_kcbert import KcBERTKorpus
from .korpus_korean_hate_speech import KoreanHateSpeechKorpus
from .korpus_korean_petitions import KoreanPetitionsKorpus
from .korpus_kornli import KorNLIKorpus
from .korpus_korsts import KorSTSKorpus
from .korpus_namuwiki import NamuwikiTextKorpus
from .korpus_naverchangwon_ner import NaverChangwonNERKorpus
from .korpus_nsmc import NSMCKorpus
from .korpus_question_pair import QuestionPairKorpus
from .loader import Korpora
