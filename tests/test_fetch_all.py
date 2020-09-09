from Korpora import Korpora


def test_fetch_all():
    Korpora.fetch('all', force_download=True)
