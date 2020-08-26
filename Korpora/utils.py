import os
from os.path import expanduser


default_korpora_path = f'{expanduser("~")}/Korpora/'


def check_path(path, dataname=''):
    if not os.path.exists(path):
        raise FileNotFoundError(f'[{dataname}] {path}')


def load_text(path, num_heads=0):
    with open(path, encoding='utf-8') as f:
        lines = [line.rstrip('\n') for line in f]
    if num_heads > 0:
        lines = lines[num_heads:]
    return lines


def fetch(source_url, destination):
    raise NotImplementedError
