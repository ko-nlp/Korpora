from Korpora import Korpora
from Korpora import KoreanPetitions


def test_usage():
    petitions = Korpora.load('korean_petitions')
    assert len(petitions.train) == len(KoreanPetitions().train)
    assert len(petitions.train) == 433631
    assert len(petitions.train[0].text) == 1491
    assert petitions.train[0].begin == '2017-08-25'
    assert petitions.train[0].end == '2017-09-24'
    assert petitions.train.titles[0] == petitions.train[0].title
    assert '청와대 국민청원' in petitions.description
    assert 'CC0 1.0 Universal' in petitions.license
    for petition in petitions.train:
        continue
