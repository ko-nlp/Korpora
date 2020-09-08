from .about import __author__   # noqa: F401
from .about import __version__  # noqa: F401

from .korpora_custom import (
    CustomLabeledSentencePairKorpus,
    CustomLabeledSentenceKorpus,
    CustomSentencePairKorpus
)
from .korpora_korean_petitions import KoreanPetitions
from .korpora_kornli import KorNLI
from .korpora_namu_wiki import NamuwikiTextKorpus
from .korpora_nsmc import NSMC
from .korpora_chatbot_data import KoreanChatbotCorpus
from .korpora_question_pair import QuestionPairCorpus
from .korpora_nc_ner import NaverChangwonNERCorpus
from .loader import Korpora
