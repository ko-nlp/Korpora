import numpy as np
import os
from tqdm import tqdm

from .loader import Korpora
from .utils import default_korpora_path


def create_lmdata(args):
    corpus_names = check_corpus(args.corpus)
    os.makedirs(os.path.abspath(args.output_dir), exist_ok=True)

    sampling_ratio = args.sampling_ratio
    if sampling_ratio is not None:
        sampling_ratio = float(sampling_ratio)
        if not (0 < sampling_ratio < 1):
            raise ValueError('`sampling_ratio` must be None or (0, 1) float')
    n_first_samples = args.n_first_samples
    np.random.seed(args.seed)
    selector = Selector(sampling_ratio, args.min_length, args.max_length)

    root_dir = args.root_dir
    if root_dir is None:
        root_dir = default_korpora_path
    force_download = args.force_download
    multilingual = args.multilingual

    status = [['', name, ' - ', ''] for name in corpus_names]

    for i_corpus, name in enumerate(corpus_names):
        if not args.save_each and i_corpus > 0:
            mode = 'a'
        else:
            mode = 'w'

        filename = f'{name}.train' if args.save_each else 'all.train'
        lmdata_path = f'{args.output_dir}/{filename}'

        sent_iterator = tqdm(
            ITERATE_TEXTS[name](root_dir, force_download, multilingual),
            desc=f'Create train data from {name}'
        )
        print_status(status)

        n_sampled = 0
        with open(lmdata_path, mode, encoding='utf-8') as f:
            for i_sent, sent in enumerate(sent_iterator):
                if not selector.use(sent):
                    continue
                f.write(f'{sent}\n')
                n_sampled += 1
                if (n_first_samples is not None) and (n_first_samples <= n_sampled):
                    break

        status[i_corpus][0] = ' x '
        status[i_corpus][2] = n_sampled
        status[i_corpus][3] = filename
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
            print(f'Not provide {name} corpus. Check the `corpus` argument')
            continue
        available.append(name)
    if not available:
        raise ValueError('Not found any proper corpus name. Check the `corpus` argument')
    return available


def print_status(status):
    max_len = max(max(len(row[3]) for row in status), 9)
    form = '| {:4} | {:25} | {:10} | {} |'
    print('\n\n' + form.format('Done', 'Corpus name', 'Num sents', 'File name' + ' ' * (max_len - 9)))
    print(form.format('-' * 4, '-' * 25, '-' * 10, '-' * max_len))
    for finish, name, num_sent, filename in status:
        if not filename:
            filename = ' ' * max_len
        else:
            filename += ' ' * (max_len -len(filename))
        print(form.format(finish, name, num_sent, filename))


def iterate_kcbert(root_dir, force_download, multilingual=False):
    Korpora.fetch('kcbert', root_dir, force_download)
    with open(f'{root_dir}/kcbert/20190101_20200611_v2.txt', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            yield line


def iterate_korean_chatbot_data(root_dir, force_download, multilingual=False):
    corpus = Korpora.load('korean_chatbot_data', root_dir, force_download)
    for sents in [corpus.train.texts, corpus.train.pairs]:
        for sent in sents:
            if not sent:
                continue
            yield sent


def iterate_korean_hate_speech(root_dir, force_download, multilingual=False):
    corpus = Korpora.load('korean_hate_speech', root_dir, force_download)
    for sents in [corpus.train.texts, corpus.dev.texts, corpus.unlabeled.texts]:
        for sent in sents:
            yield sent


def iterate_korean_parallel_koen_news(root_dir, force_download, multilingual):
    corpus = Korpora.load('korean_parallel_koen_news', root_dir, force_download)
    data = [corpus.train.texts, corpus.dev.texts, corpus.test.texts]
    if multilingual:
        data += [corpus.train.pairs, corpus.dev.pairs, corpus.test.pairs]
    for sents in data:
        for sent in sents:
            yield sent


def iterate_korean_petitions(root_dir, force_download, multilingual=False):
    corpus = Korpora.load('korean_petitions', root_dir, force_download)
    for example in corpus.train:
        yield example.title
        yield example.text


def iterate_kornli(root_dir, force_download, multilingual=False):
    corpus = Korpora.load('kornli', root_dir, force_download)
    for data in [corpus.multinli_train, corpus.snli_train, corpus.xnli_dev, corpus.xnli_test]:
        for sent in data.texts:
            yield sent
        for sent in data.pairs:
            yield sent


def iterate_korsts(root_dir, force_download, multilingual=False):
    corpus = Korpora.load('korsts', root_dir, force_download)
    for data in [corpus.train, corpus.dev, corpus.test]:
        for sent in data.texts:
            yield sent
        for sent in data.pairs:
            yield sent


def iterate_kowikitext(root_dir, force_download, multilingual=False):
    Korpora.fetch('kowikitext', root_dir, force_download)
    paths = [
        f'{root_dir}/kowiki/kowikitext_20200920.train',
        f'{root_dir}/kowiki/kowikitext_20200920.dev',
        f'{root_dir}/kowiki/kowikitext_20200920.test'
    ]
    for path in paths:
        with open(path, encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or (line[0] == '=' and line[-1] == '='):
                    continue
                yield line


def iterate_namuwikitext(root_dir, force_download, multilingual=False):
    Korpora.fetch('namuwikitext', root_dir, force_download)
    paths = [
        f'{root_dir}/namiwiki/namuwikitext_20200302.train',
        f'{root_dir}/namiwiki/namuwikitext_20200302.dev',
        f'{root_dir}/namiwiki/namuwikitext_20200302.test'
    ]
    for path in paths:
        with open(path, encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or (line[0] == '=' and line[-1] == '='):
                    continue
                yield line


def iterate_naver_changwon_ner(root_dir, force_download, multilingual=False):
    corpus = Korpora.load('naver_changwon_ner', root_dir, force_download)
    for sent in corpus.train.texts:
        yield sent


def iterate_nsmc(root_dir, force_download, multilingual=False):
    corpus = Korpora.load('nsmc', root_dir, force_download)
    for sents in [corpus.train.texts, corpus.test.texts]:
        for sent in sents:
            yield sent


def iterate_question_pair(root_dir, force_download, multilingual=False):
    corpus = Korpora.load('question_pair', root_dir, force_download)
    for sents in [corpus.train.texts, corpus.train.pairs]:
        for sent in sents:
            yield sent


ITERATE_TEXTS = {
    'kcbert': iterate_kcbert,
    'korean_chatbot_data': iterate_korean_chatbot_data,
    'korean_hate_speech': iterate_korean_hate_speech,
    'korean_parallel_koen_news': iterate_korean_parallel_koen_news,
    'korean_petitions': iterate_korean_petitions,
    'kornli': iterate_kornli,
    'korsts': iterate_korsts,
    'kowikitext': iterate_kowikitext,
    'namuwikitext': iterate_namuwikitext,
    'naver_changwon_ner': iterate_naver_changwon_ner,
    'nsmc': iterate_nsmc,
    'question_pair': iterate_question_pair
}