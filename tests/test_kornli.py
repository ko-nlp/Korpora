from Korpora import Korpora, KorNLIKorpus


def test_usage():
    kornli = Korpora.load('kornli')
    assert kornli.exists()
    assert len(kornli.snli_train) == len(KorNLIKorpus().snli_train)
    kornli.snli_train[0]
    assert len(kornli.snli_train) == 550152
    assert len(kornli.xnli_dev) == 2490
    assert len(kornli.xnli_test) == 5010
    assert len(kornli.multinli_train) == 392702
    print(f'str(korpus)\n{str(kornli)}')
    print(f'str(korpus.multinli_train)\n{str(kornli.multinli_train)}')
    for example in kornli.snli_train:
        continue
