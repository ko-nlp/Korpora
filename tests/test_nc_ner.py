from Korpora import Korpora, NaverChangwonNERCorpus


def test_usage():
    ner = Korpora.load('naver_changwon_ner')
    assert len(ner.train) == len(NaverChangwonNERCorpus().train)
    ner.train[0]
    assert len(ner.train) == 90000
    for example in ner.train:
        continue
