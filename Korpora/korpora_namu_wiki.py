import os

from .utils import fetch, default_korpora_path


NAMU_WIKI_CORPUS_INFORMATION = [
        {
            'googledrive_file_id': '1gZFsbP1CXYcBWk1_WIHy4EfGmgw3gOHu',
            'destination': 'namiwiki/namuwikitext_20200302.train.zip',
            'method': 'google_drive'
        },
        {
            'googledrive_file_id': '17DNjnwB7SDnyxb4deX7EaSA8DkaBHfxU',
            'destination': 'namiwiki/namuwikitext_20200302.test.zip',
            'method': 'google_drive'
        },
        {
            'googledrive_file_id': '1FT7ARSI3QD7mhCyKV-0NSwI6Rq6s4D2S',
            'destination': 'namiwiki/namuwikitext_20200302.dev.zip',
            'method': 'google_drive'
        },
]


for info in NAMU_WIKI_CORPUS_INFORMATION:
    local_path = os.path.join(os.path.abspath(default_korpora_path), info['destination'])
    fetch(info['googledrive_file_id'],
          local_path,
          'namuwiki',
          info['method'],
          forced_download=False)
