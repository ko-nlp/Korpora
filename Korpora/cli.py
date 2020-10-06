import argparse
import os

from .about import __version__
from .loader import Korpora, KORPUS_DESCRIPTION


def fetch(args):
    corpus_names = args.corpus
    if corpus_names == 'all':
        Korpora.fetch(corpus_names, args.root, args.force_download)
        return

    if isinstance(corpus_names, str):
        corpus_names = [corpus_names]
    for name in corpus_names:
        if name not in KORPUS_DESCRIPTION:
            print(f'Korpora does not provide `{name}` corpus')
            continue
        Korpora.fetch(name, args.root, args.force_download)


def listup(args):
    for name, description in KORPUS_DESCRIPTION.items():
        print(f'[Corpus] {name} : {description}')


def show_arguments(args):
    print('## Arguments of Moducorpus sanitizer ##')
    for name, var in sorted(vars(args).items()):
        if callable(var):
            print(f'  - {name} : {var.__name__}')
        else:
            print(f'  - {name} : {var}')


def show_version(args):
    print(f'moducorpus_sanitizer=={__version__}')


def main():
    parser = argparse.ArgumentParser(description='Korpora Command Line Interface')
    parser.set_defaults(func=show_version)
    subparsers = parser.add_subparsers(help='Korpora')

    # fetch
    parser_fetch = subparsers.add_parser('fetch', help='Tokenize `input` and save the result to `output`')
    parser_fetch.add_argument('--corpus', type=str, default='all', nargs='+', help='corpus type')
    parser_fetch.add_argument('--root', type=str, default=None, help='path/to/Korpora/')
    parser_fetch.add_argument('--force_download', dest='force_download', action='store_true')
    parser_fetch.set_defaults(func=fetch)

    parser_list = subparsers.add_parser('list', help='Tokenize `input` and save the result to `output`')
    parser_list.set_defaults(func=listup)

    # Do task
    args = parser.parse_args()
    show_arguments(args)
    task_function = args.func
    task_function(args)


if __name__ == '__main__':
    main()