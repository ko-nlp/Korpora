import argparse
import time
import sys, os
from contextlib import contextmanager
from Korpora import (
    Korpora,
    ModuNewsKorpus,
    ModuMessengerKorpus,
    ModuMorphemeKorpus,
    ModuNEKorpus,
    ModuSpokenKorpus,
    ModuWebKorpus,
    ModuWrittenKorpus
)


corpus_list = Korpora.corpus_list()

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout


def fetch_test(args):
    exclusive_fetch_test = {
        'aihub_conversation_translation', 'aihub_decree_translation', 'aihub_government_website_translation',
        'aihub_korean_culture_translation', 'aihub_news_translation', 'aihub_spoken_translation', 'aihub_translation',
        'modu_messenger', 'modu_mp', 'modu_ne', 'modu_news', 'modu_spoken', 'modu_web', 'modu_written'
    }
    for corpus_name in corpus_list:
        if corpus_name in exclusive_fetch_test:
            continue
        Korpora.fetch(corpus_name, root_dir=args.root_dir)
        time.sleep(0.5)


def load_small_test(args):
    exclusive_load_test = {
        'kcbert', 'kowikitext', 'namuwikitext',
        'modu_messenger', 'modu_mp', 'modu_ne', 'modu_news', 'modu_spoken', 'modu_web', 'modu_written'
    }
    for corpus_name in corpus_list:
        if corpus_name in exclusive_load_test:
            continue
        with suppress_stdout():
            corpus = Korpora.load(corpus_name, root_dir=args.root_dir)
        bar = '=' * 80
        print(corpus, end=f'\n\n{bar}\n\n', flush=True)
        time.sleep(0.5)


def load_large_test(args):
    for corpus_name in ['kcbert', 'kowikitext', 'namuwikitext']:
        corpus = Korpora.load(corpus_name, root_dir=args.root_dir)
        bar = '=' * 80
        print(corpus, end=f'\n\n{bar}\n\n', flush=True)
        time.sleep(0.5)


def load_modu_test(args):
    for corpus_name in ['modu_messenger', 'modu_mp', 'modu_ne', 'modu_news', 'modu_spoken', 'modu_web', 'modu_written']:
        with suppress_stdout():
            corpus = Korpora.load(corpus_name, root_dir=args.root_dir)
        bar = '=' * 80
        print(corpus, end=f'\n\n{bar}\n\n', flush=True)
        time.sleep(0.5)


def main():
    parser = argparse.ArgumentParser(description='Korpora Manual Test')
    subparsers = parser.add_subparsers(help='Korpora Manual Test')

    # fetch
    parser_fetch = subparsers.add_parser('fetch', help='Fetch `corpus` to `root`')
    parser_fetch.add_argument('--root_dir', type=str, default=None, help='default is `~/Korpora/`')
    parser_fetch.set_defaults(func=fetch_test)

    # load small corpus
    parser_load_small = subparsers.add_parser('load_small', help='Fetch `corpus` to `root`')
    parser_load_small.add_argument('--root_dir', type=str, default=None, help='default is `~/Korpora/`')
    parser_load_small.set_defaults(func=load_small_test)

    # load large corpus
    parser_load_large = subparsers.add_parser('load_large', help='Fetch `corpus` to `root`')
    parser_load_large.add_argument('--root_dir', type=str, default=None, help='default is `~/Korpora/`')
    parser_load_large.set_defaults(func=load_large_test)

    # load modu corpus
    parser_load_modu = subparsers.add_parser('load_modu', help='Fetch `corpus` to `root`')
    parser_load_modu.add_argument('--root_dir', type=str, default=None, help='default is `~/Korpora/`')
    parser_load_modu.set_defaults(func=load_modu_test)

    # Do task
    args = parser.parse_args()
    task_function = args.func
    task_function(args)


if __name__ == '__main__':
    main()
