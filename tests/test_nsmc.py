from Korpora import Korpora


def test_usage():
    root_dir = './data/'
    nsmc = Korpora.load('nsmc', root_dir)
    assert len(nsmc.train.texts) == 150000
    assert len(nsmc.train.labels) == 150000
    assert len(nsmc.test.texts) == 50000
    assert len(nsmc.test.labels) == 50000
