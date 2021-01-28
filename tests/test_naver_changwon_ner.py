from Korpora import Korpora, NaverChangwonNERKorpus


def test_usage():
    ner = Korpora.load('naver_changwon_ner')
    assert ner.exists()
    assert len(ner.train) == len(NaverChangwonNERKorpus().train)
    ner.train[0]
    assert len(ner.train) == 90000
    print(f'str(korpus)\n{str(ner)}')
    print(f'str(korpus.train)\n{str(ner.train)}')
    for example in ner.train:
        continue
