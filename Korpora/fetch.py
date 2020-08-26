from .utils import download, check_dir


def fetch(corpus_name, root_dir):
    if corpus_name not in DATA_LOCATIONS:
        raise ValueError(f'support only {set(DATA_LOCATIONS.keys())}')
    locations = DATA_LOCATIONS[corpus_name]
    for location in locations:
        if location['method'] == 'download':
            do_download(location)

def do_download(information, root_dir):
    url = information['url']
    destination = os.path.join(root_dir, information['destination'])
#    check_dir(destination)
#    download(url, destination)


DATA_LOCATIONS = {
    'nsmc': [
        {
            'url': 'https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt',
            'destination': 'nsmc/rating_train.txt',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt',
            'destination': 'nsmc/rating_test.txt',
            'method': 'download'
        },
    ],
}