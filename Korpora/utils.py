import os
from os.path import expanduser
from tqdm import tqdm
from urllib import request


default_korpora_path = f'{expanduser("~")}/Korpora/'


def check_path(path):
    return os.path.exists(path)


def check_dir(filepath):
    dirname = os.path.abspath(os.path.dirname(filepath))
    if not os.path.exists(dirname):
        os.makedirs(dirname)


def load_text(path, num_heads=0):
    with open(path, encoding='utf-8') as f:
        lines = [line.rstrip('\n') for line in f]
    if num_heads > 0:
        lines = lines[num_heads:]
    return lines


def _reporthook(t):
    """ ``reporthook`` to use with ``urllib.request`` that prints the process of the download.

    Uses ``tqdm`` for progress bar.

    **Reference:**
    https://github.com/tqdm/tqdm

    Args:
        t (tqdm.tqdm) Progress bar.

    Example:
        >>> with tqdm(unit='B', unit_scale=True, miniters=1, desc=filename) as t:  # doctest: +SKIP
        ...   urllib.request.urlretrieve(file_url, filename=full_path, reporthook=reporthook(t))
    """
    last_b = [0]

    def inner(b=1, bsize=1, tsize=None):
        """
        Args:
            b (int, optional): Number of blocks just transferred [default: 1].
            bsize (int, optional): Size of each block (in tqdm units) [default: 1].
            tsize (int, optional): Total size (in tqdm units). If [default: None] remains unchanged.
        """
        if tsize is not None:
            t.total = tsize
        t.update((b - last_b[0]) * bsize)
        last_b[0] = b

    return inner

def download(url, local_path, corpus_name=''):
    filename = os.path.basename(local_path)
    with tqdm(unit='B', unit_scale=True, miniters=1, desc=f'[{corpus_name}] download {filename}') as t:
        request.urlretrieve(url, filename=local_path, reporthook=_reporthook(t))
