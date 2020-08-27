import os
from .utils import download, check_dir


def fetch(corpus_name, root_dir):
    """
    Examples::
        >>> from Korpora.fetch import fetch
        >>> fetch('nsmc', './Korpora')
    """
    if corpus_name not in DATA_LOCATIONS:
        raise ValueError(f'support only {set(DATA_LOCATIONS.keys())}')
    locations = DATA_LOCATIONS[corpus_name]
    print(f'Fetch {corpus_name} to {os.path.abspath(root_dir)}')
    for information in locations:
        if information['method'] == 'download':
            do_download(information, root_dir)


def do_download(information, root_dir):
    url = information['url']
    destination = os.path.join(root_dir, information['destination'])
    check_dir(destination)
    corpus_name = information['destination'].split('/')[0]
    download(url, destination, corpus_name)


DATA_LOCATIONS = {
    'nsmc': [
        {
            'url': 'https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt',
            'destination': 'nsmc/ratings_train.txt',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt',
            'destination': 'nsmc/ratings_test.txt',
            'method': 'download'
        },
    ],
}