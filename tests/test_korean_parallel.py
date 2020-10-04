from Korpora import Korpora, KoreanParallelKOENNewsKorpus


def test_usage():
    koen_news = Korpora.load('korean_parallel_koen_news')
    koen_news_ = KoreanParallelKOENNewsKorpus()
    assert len(koen_news.train) == len(koen_news_.train) == 94123
    assert len(koen_news.dev) == 1000
    assert len(koen_news.test) == 2000
    print(f'str(korpus)\n{str(koen_news)}')
    print(f'str(korpus.train)\n{str(koen_news.train)}')
    for data in [koen_news.train, koen_news.dev, koen_news.test]:
        for _ in data:
            continue
