import argparse
import os

from .about import __version__
from .loader import KORPUS_DESCRIPTION
from .task_fetch import fetch
from .task_lmdata import create_lmdata


def listup(args):
    for name, description in KORPUS_DESCRIPTION.items():
        print(f'[Corpus] {name} : {description}')


def show_arguments(args):
    print('## Arguments of Korpora CLI ##')
    for name, var in sorted(vars(args).items()):
        if callable(var):
            print(f'  - {name} : {var.__name__}')
        else:
            print(f'  - {name} : {var}')


def show_version(args):
    print(f'Korpora=={__version__}')
    print('Execute `korpora --help` to see what Korpora provides')


def main():
    parser = argparse.ArgumentParser(description='Korpora Command Line Interface')
    parser.set_defaults(func=show_version)
    subparsers = parser.add_subparsers(help='Korpora')

    # fetch
    parser_fetch = subparsers.add_parser('fetch', help='Fetch `corpus` to `root`')
    parser_fetch.add_argument('--corpus', type=str, default='all', nargs='+', help='corpus name')
    parser_fetch.add_argument('--root', type=str, default=None, help='path/to/Korpora/')
    parser_fetch.add_argument('--force_download', dest='force_download', action='store_true')
    parser_fetch.set_defaults(func=fetch)

    # list
    parser_list = subparsers.add_parser('list', help='Tokenize `input` and save the result to `output`')
    parser_list.set_defaults(func=listup)

    # create language model train data
    parser_lmdata = subparsers.add_parser('lmdata', help='Create language model train data')
    parser_lmdata.add_argument('--corpus', type=str, required=True, nargs='+', help='corpus names')
    parser_lmdata.add_argument('--root_dir', type=str, default=None, help='path/to/Korpora')
    parser_lmdata.add_argument('--output_dir', type=str, required=True, help='output file path')
    parser_lmdata.add_argument('--sampling_ratio', type=float, default=None, help='Sampling ratio')
    parser_lmdata.add_argument('--n_first_samples', type=int, default=None, help='Number of first samples')
    parser_lmdata.add_argument('--min_length', type=int, default=None, help='Mininum length of text')
    parser_lmdata.add_argument('--max_length', type=int, default=None, help='Maximum length of text')
    parser_lmdata.add_argument('--seed', type=int, default=None, help='Random seed')
    parser_lmdata.add_argument('--force_download', dest='force_download', action='store_true')
    parser_lmdata.add_argument('--multilingual', dest='multilingual', action='store_true', help='If True, make include train data foreign language text')
    parser_lmdata.add_argument('--save_each', dest='save_each', action='store_true', help='store each corpus as a file')
    parser_lmdata.set_defaults(func=create_lmdata)

    # Do task
    args = parser.parse_args()
    show_arguments(args)
    task_function = args.func
    task_function(args)


if __name__ == '__main__':
    main()
