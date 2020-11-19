import os
import requests
import tarfile
import zipfile
from os.path import expanduser
from tqdm import tqdm
from urllib import request

import gzip
import shutil

default_korpora_path = f'{expanduser("~")}/Korpora/'
GOOGLE_DRIVE_URL = "https://docs.google.com/uc?export=download"


def check_path(path):
    return os.path.exists(path)


def check_dir(filepath):
    dirname = os.path.abspath(os.path.dirname(filepath))
    if not os.path.exists(dirname):
        os.makedirs(dirname)


def load_text(path, num_heads=0, num_samples=-1):
    lines = []
    with open(path, encoding='utf-8') as f:
        if num_heads > 0:
            for _ in range(num_heads):
                next(f)
        for i, line in enumerate(f):
            if (num_samples > 0) and (i >= num_samples):
                break
            lines.append(line.rstrip('\n'))
    return lines


def load_parallel_text(source_path, target_path, num_heads=0, num_samples=-1):
    sources = load_text(source_path, num_heads, num_samples)
    targets = load_text(target_path, num_heads, num_samples)
    if len(sources) != len(targets):
        raise ValueError('Parallel corpus must have same length two files')
    return sources, targets


def load_wikitext(path, num_lines=-1):
    """
    Wikitext format

         = Head1 =

        text ...
        text ...

         = = 2ead = =

        text ...
        text ...
    """
    if num_lines <= 0:
        with open(path, encoding='utf-8') as f:
            texts = f.read().split('\n =')
    else:
        lines = []
        with open(path, encoding='utf-8') as f:
            for i, line in enumerate(f):
                if (i >= num_lines):
                    break
                lines.append(line)
        texts = ''.join(lines).split('\n =')
    # fix missing prefix
    texts = [texts[0]] + [f' ={text}' for text in texts[1:]]
    return texts


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


def web_download(url, local_path, corpus_name='', force_download=False):
    site = request.urlopen(url)
    meta = site.info()
    remote_size = int(meta['Content-Length'])
    if (not force_download) and os.path.exists(local_path) and (os.stat(local_path).st_size == remote_size):
        print(f'[Korpora] Corpus `{corpus_name}` is already installed at {local_path}')
        return None
    filename = os.path.basename(local_path)
    with tqdm(unit='B', unit_scale=True, miniters=1, desc=f'[{corpus_name}] download {filename}') as t:
        request.urlretrieve(url, filename=local_path, reporthook=_reporthook(t))


def web_download_unzip(url, zip_path, corpus_name='', force_download=False):
    web_download(url, zip_path, corpus_name, force_download)
    # assume that path/to/abc.zip consists path/to/abc
    data_path = zip_path[:-4]
    if (not force_download) and os.path.exists(data_path):
        print(f'[Korpora] Corpus `{corpus_name}` is already installed at {data_path}')
        return None
    data_root = os.path.dirname(zip_path)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(data_root)
    print(f'unzip {data_path}')


def web_download_untar(url, tar_path, corpus_name='', force_download=False):
    web_download(url, tar_path, corpus_name, force_download)
    # assume that path/to/abc.tar consists path/to/abc
    data_path = tar_path[:-4]
    if (not force_download) and os.path.exists(data_path):
        print(f'[Korpora] Corpus `{corpus_name}` is already installed at {data_path}')
        return None
    data_root = os.path.dirname(tar_path)
    with tarfile.open(tar_path) as tar:
        tar.extractall(data_root)
    print(f'decompress {tar_path}')


def web_download_ungzip(url, gzip_path, corpus_name='', force_download=False):
    web_download(url, gzip_path, corpus_name, force_download)
    # assume that path/to/abc.gzip consists path/to/abc
    data_path = gzip_path[:-3]
    if (not force_download) and os.path.exists(data_path):
        print(f'[Korpora] Corpus `{corpus_name}` is already installed at {data_path}')
        return None
    with gzip.open(gzip_path, 'rb') as fi:
        with open(data_path, 'wb') as fo:
            shutil.copyfileobj(fi, fo)
    print(f'decompress {gzip_path}')


def google_drive_download(file_id, local_path, corpus_name='', force_download=False):
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value
        return None

    if (not force_download) and os.path.exists(local_path):
        print(f'[Korpora] Corpus `{corpus_name}` is already installed at {local_path}')
        return None

    # init a HTTP session
    session = requests.Session()

    # make a request
    response = session.get(GOOGLE_DRIVE_URL, params={'id': file_id}, stream=True)

    # get confirmation token
    token = get_confirm_token(response)

    if token:
        params = {'id': file_id, 'confirm': token}
        response = session.get(GOOGLE_DRIVE_URL, params=params, stream=True)

    # download to disk
    with open(local_path, "wb") as f:
        content_length = response.headers.get("Content-Length")
        total = int(content_length) if content_length is not None else None
        progress = tqdm(
            unit="B",
            unit_scale=True,
            total=total,
            initial=0,
            desc=f'[{corpus_name}] download {local_path}',
        )
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                progress.update(len(chunk))
                f.write(chunk)
        progress.close()


def fetch(remote_path, local_path, corpus_name=None, force_download=False, method="download"):
    """
       Examples::

           >>> from Korpora.utils import fetch
           >>> fetch(
           >>>    'https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt',
           >>>    'nsmc/ratings_train.txt', 'nsmc')
    """
    destination = os.path.abspath(local_path)
    check_dir(destination)

    if method == "download":
        web_download(remote_path, destination, corpus_name, force_download)
    elif method == "google_drive":
        google_drive_download(remote_path, destination, corpus_name, force_download)
    elif method == "download & unzip":
        web_download_unzip(remote_path, destination, corpus_name, force_download)
    elif method == "download & untar":
        web_download_untar(remote_path, destination, corpus_name, force_download)
    elif method == "download & ungzip":
        web_download_ungzip(remote_path, destination, corpus_name, force_download)
    else:
        print(f'download method is not valid ({method})')
