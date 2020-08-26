from .utils import default_korpora_path

def fetch(corpus_name, root_dir=None):
    if root_dir is None:
        root_dir = default_korpora_path
    DATA_FETCH(corpus_name)(root_dir)


def fetch_gitclone(root_dir):
    raise NotImplementedError


DATA_FETCH = {
    'nsmc': fetch_gitclone,
}