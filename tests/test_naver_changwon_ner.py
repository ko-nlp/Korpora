from Korpora import Korpora, NaverChangwonNERKorpus


def test_usage():
    ner = Korpora.load('naver_changwon_ner')
    assert len(ner.train) == len(NaverChangwonNERKorpus().train)
    ner.train[0]
    assert len(ner.train) == 90000
    for example in ner.train:
        continue
