from Korpora import Korpora, KorSTSKorpus


def test_usage():
    korsts = Korpora.load('korsts')
    assert len(korsts.train) == len(KorSTSKorpus().train)
    korsts.train[0]
    korsts.dev[0]
    korsts.test[0]
    assert len(korsts.train) == len(korsts.train.get_all_pairs()) == \
           len(korsts.train.get_all_labels()) == len(korsts.train.get_all_genres()) == \
           len(korsts.train.get_all_filenames()) == len(korsts.train.get_all_years()) == 5749
    assert len(korsts.dev) == len(korsts.dev.get_all_pairs()) == \
           len(korsts.dev.get_all_labels()) == len(korsts.dev.get_all_genres()) == \
           len(korsts.dev.get_all_filenames()) == len(korsts.dev.get_all_years()) == 1500
    assert len(korsts.test) == len(korsts.test.get_all_pairs()) == \
           len(korsts.test.get_all_labels()) == len(korsts.test.get_all_genres()) == \
           len(korsts.test.get_all_filenames()) == len(korsts.test.get_all_years()) == 1379
    print(f'str(korpus)\n{str(korsts)}')
    print(f'str(korpus.train)\n{str(korsts.train)}')
    for example in korsts.train:
        continue
    for example in korsts.dev:
        continue
    for example in korsts.test:
        continue
