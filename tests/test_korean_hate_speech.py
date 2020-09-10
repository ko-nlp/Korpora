from Korpora import Korpora, KoreanHateSpeechKorpus


def test_usage():
    korean_hate_speech = Korpora.load('korean_hate_speech')
    korean_hate_speech_ = KoreanHateSpeechKorpus()
    assert len(korean_hate_speech.unlabeled) == len(korean_hate_speech_.unlabeled) == 2033893
    assert len(korean_hate_speech.test) == 974
    assert len(korean_hate_speech.dev) == 471
    assert len(korean_hate_speech.train) == 7896
    for data in [korean_hate_speech.train, korean_hate_speech.dev, korean_hate_speech.test, korean_hate_speech.unlabeled]:
        for _ in data:
            continue
