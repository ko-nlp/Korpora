from Korpora import Korpora


def test_fetch_all():
    Korpora.fetch('nsmc', force_download=True)
