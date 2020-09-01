import os
import time
from .utils import download, check_dir


def fetch(corpus_name, root_dir):
    """
    Examples::
        >>> from Korpora.fetch import fetch
        >>> fetch('nsmc', './Korpora')
    """
    corpus_name = corpus_name.lower()
    if corpus_name not in DATA_LOCATIONS:
        raise ValueError(f'support only {set(DATA_LOCATIONS.keys())}')
    locations = DATA_LOCATIONS[corpus_name]
    print(f'Fetch {corpus_name} to {os.path.abspath(root_dir)}', flush=True)
    time.sleep(0.03)
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
    'korean_petitions': [
        {
            'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2017-08',
            'destination': 'korean_petitions/petitions_2017-08',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2017-09',
            'destination': 'korean_petitions/petitions_2017-09',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2017-10',
            'destination': 'korean_petitions/petitions_2017-10',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2017-11',
            'destination': 'korean_petitions/petitions_2017-11',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2017-12',
            'destination': 'korean_petitions/petitions_2017-12',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2018-01',
            'destination': 'korean_petitions/petitions_2018-01',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2018-02',
            'destination': 'korean_petitions/petitions_2018-02',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2018-03',
            'destination': 'korean_petitions/petitions_2018-03',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2018-04',
            'destination': 'korean_petitions/petitions_2018-04',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2018-05',
            'destination': 'korean_petitions/petitions_2018-05',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2018-06',
            'destination': 'korean_petitions/petitions_2018-06',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2018-07',
            'destination': 'korean_petitions/petitions_2018-07',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2018-08',
            'destination': 'korean_petitions/petitions_2018-08',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2018-09',
            'destination': 'korean_petitions/petitions_2018-09',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2018-10',
            'destination': 'korean_petitions/petitions_2018-10',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2018-11',
            'destination': 'korean_petitions/petitions_2018-11',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2018-12',
            'destination': 'korean_petitions/petitions_2018-12',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2019-01',
            'destination': 'korean_petitions/petitions_2019-01',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2019-02',
            'destination': 'korean_petitions/petitions_2019-02',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/lovit/petitions_archive/archive/petitions_2019-03',
            'destination': 'korean_petitions/petitions_2019-03',
            'method': 'download'
        }
    ],
    'korean_chatbot_data': [
        {
            'url': 'https://raw.githubusercontent.com/songys/Chatbot_data/master/ChatbotData%20.csv',
            'destination': 'korean_chatbot_data/ChatbotData.csv',
            'method': 'download'
        }
    ],
    'kornli': [
        {
            'url': 'https://raw.githubusercontent.com/kakaobrain/KorNLUDatasets/master/KorNLI/multinli.train.ko.tsv',
            'destination': 'kornli/multinli.train.ko.tsv',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/kakaobrain/KorNLUDatasets/master/KorNLI/snli_1.0_train.ko.tsv',
            'destination': 'kornli/snli_1.0_train.ko.tsv',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/kakaobrain/KorNLUDatasets/master/KorNLI/xnli.dev.ko.tsv',
            'destination': 'kornli/xnli.dev.ko.tsv',
            'method': 'download'
        },
        {
            'url': 'https://raw.githubusercontent.com/kakaobrain/KorNLUDatasets/master/KorNLI/xnli.test.ko.tsv',
            'destination': 'kornli/xnli.test.ko.tsv',
            'method': 'download'
        }
    ]
}
