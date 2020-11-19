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
