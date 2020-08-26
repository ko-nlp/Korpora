import os
from os.path import expanduser
from urllib import request


default_korpora_path = f'{expanduser("~")}/Korpora/'


def check_path(path, dataname=''):
    if not os.path.exists(path):
        raise FileNotFoundError(f'[{dataname}] {path}')


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


def download(url, local_path):
    check_dir(local_path)
    path, http_message = request.urlretrieve(url, local_path)
    return http_message
