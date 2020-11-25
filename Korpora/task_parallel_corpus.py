import numpy as np
import os
from tqdm import tqdm

from .loader import Korpora
from .utils import default_korpora_path


def create_parallel_corpus(args):
    corpus_names = check_corpus(args.corpus)
    os.makedirs(os.path.abspath(args.output_dir), exist_ok=True)

    sampling_ratio = args.sampling_ratio
    if sampling_ratio is not None:
        sampling_ratio = float(sampling_ratio)
        if not (0 < sampling_ratio < 1):
            raise ValueError('`sampling_ratio` must be None or (0, 1) float')
    n_first_samples = args.head
    np.random.seed(args.seed)
    selector = Selector(sampling_ratio, args.min_length, args.max_length)

    status = [['', name, ' - ', ''] for name in corpus_names]

    for i_corpus, name in enumerate(corpus_names):
        if not args.save_each and i_corpus > 0:
            mode = 'a'
        else:
            mode = 'w'

        source_filename = f'{name}.source' if args.save_each else 'all.source'
        target_filename = f'{name}.target' if args.save_each else 'all.target'
        source_corpus_path = f'{args.output_dir}/{source_filename}'
        target_corpus_path = f'{args.output_dir}/{target_filename}'

        pair_iterator = tqdm(
            Korpora.load(name, root_dir=args.root_dir, force_download=args.force_download).train,
            desc=f'Create train data from {name}'
        )
        print_status(status)

        n_sampled = 0
        fs = open(source_corpus_path, mode, encoding='utf-8')
        ft = open(target_corpus_path, mode, encoding='utf-8')
        for i_sent, pair in enumerate(pair_iterator):
            if not selector.use(pair.text) or not selector.use(pair.pair):
                continue
            source = pair.text.replace('\n', ' ')
            target = pair.pair.replace('\n', ' ')
            fs.write(f'{source}\n')
            ft.write(f'{target}\n')
            n_sampled += 1
            if (n_first_samples is not None) and (n_first_samples <= n_sampled):
                break
        fs.close()
        ft.close()

        status[i_corpus][0] = ' x '
        status[i_corpus][2] = n_sampled
        status[i_corpus][3] = f'{source_filename} & *.target'
    print_status(status)


class Selector:
    def __init__(self, sampling_ratio, min_length, max_length):
        if isinstance(min_length, int) and min_length < 0:
            min_length = None
        if isinstance(max_length, int) and max_length < 0:
            max_length = None
        self.sampling_ratio = sampling_ratio
        self.min_length = min_length
        self.max_length = max_length

    def use(self, text):
        length = len(text)
        if (self.min_length is not None) and (length < self.min_length):
            return False
        if (self.max_length is not None) and (length > self.max_length):
            return False
        if self.sampling_ratio is None:
            return True
        return np.random.rand() < self.sampling_ratio


def check_corpus(corpus_names):
    if (corpus_names == 'all') or (corpus_names[0] == 'all'):
        corpus_names = list(ITERATE_TEXTS)
    if isinstance(corpus_names, str):
        corpus_names = [corpus_names]
    available = []
    for name in corpus_names:
        if name not in ITERATE_TEXTS:
            print(f'{name} corpus not provided. Check the `corpus` argument')
            continue
        available.append(name)
    if 'aihub_translation' in available:
        available = [name for name in available if (name[:6] != 'aihub_')]
        available = ['aihub_spoken_translation',
                     'aihub_conversation_translation',
                     'aihub_news_translation',
                     'aihub_korean_culture_translation',
                     'aihub_decree_translation',
                     'aihub_government_website_translation'
                    ] + available
    if not available:
        raise ValueError('Not found any proper corpus name. Check the `corpus` argument')
    return available


def print_status(status):
    max_len = max(max(len(row[3]) for row in status), 9)
    form = '| {:4} | {:40} | {:10} | {} |'
    print('\n\n' + form.format('Done', 'Corpus name', 'Num pairs', 'File name' + ' ' * (max_len - 9)))
    print(form.format('-' * 4, '-' * 40, '-' * 10, '-' * max_len))
    for finish, name, num_pairs, filename in status:
        if not filename:
            filename = ' ' * max_len
        else:
            filename += ' ' * (max_len -len(filename))
        print(form.format(finish, name, num_pairs, filename))


ITERATE_TEXTS = {
    'aihub_translation',
    'aihub_spoken_translation',
    'aihub_conversation_translation',
    'aihub_news_translation',
    'aihub_korean_culture_translation',
    'aihub_decree_translation',
    'aihub_government_website_translation',
    'korean_parallel_koen_news',
    'open_subtitles'
}