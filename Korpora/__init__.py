from .about import __author__   # noqa: F401
from .about import __version__  # noqa: F401

from .korpora_custom import (
    CustomLabeledSentencePairKorpus,
    CustomLabeledSentenceKorpus,
    CustomSentencePairKorpus
)
from .korpora_korean_hate_speech import KoreanHateSpeech
from .korpora_korean_petitions import KoreanPetitions
from .korpora_kornli import KorNLI
from .korpora_korsts import KorSTS
from .korpora_namu_wiki import NamuwikiTextKorpus
from .korpora_nsmc import NSMC
from .korpora_chatbot_data import KoreanChatbotKorpus
from .korpora_question_pair import QuestionPairKorpus
from .korpora_nc_ner import NaverChangwonNERKorpus
from .loader import Korpora
