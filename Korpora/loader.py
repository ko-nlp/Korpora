from .korpora_nsmc import NSMCData
from .utils import default_korpora_path


class Korpora:
    @classmethod
    def load(cls, corpus_names, root_dir=None):
        return_single = isinstance(corpus_names, str)
        if return_single:
            corpus_names = [corpus_names]

        if root_dir is None:
            root_dir = default_korpora_path

        corpora = [KORPORA[corpus_name](root_dir) for corpus_name in corpus_names]
        if return_single:
            return corpora[0]
        return corpora


KORPORA = {
    'nsmc': NSMCData
}
