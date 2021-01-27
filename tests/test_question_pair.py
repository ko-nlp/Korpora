from Korpora import Korpora, QuestionPairKorpus


def test_usage():
    pair = Korpora.load('question_pair')
    assert pair.exists()
    assert len(pair.train) == len(QuestionPairKorpus().train)
    pair.train[0]
    pair.test[0]
    assert len(pair.train) == 6888
    assert len(pair.test) == 688
    assert len(pair.get_all_pairs()) == 7576
    assert len(pair.get_all_labels()) == 7576
    print(f'str(korpus)\n{str(pair)}')
    print(f'str(korpus.train)\n{str(pair.train)}')
    for example in pair.train:
        continue
    for example in pair.test:
        continue
