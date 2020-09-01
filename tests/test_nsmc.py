from Korpora import NSMCData
from Korpora import Korpora


def test_usage():
    root_dir = 'path/to/Korpora/'
    nsmc = NSMCData(root_dir)
    assert len(nsmc.train.texts) == 150000
    assert len(nsmc.train.labels) == 150000
    assert len(nsmc.test.texts) == 50000
    assert len(nsmc.test.labels) == 50000
    assert len(nsmc.get_all_labels()) == 200000

    nsmc = Korpora.load('nsmc', root_dir)
    assert len(nsmc.train.texts) == 150000
    assert len(nsmc.train.labels) == 150000
    assert len(nsmc.test.texts) == 50000
    assert len(nsmc.test.labels) == 50000
