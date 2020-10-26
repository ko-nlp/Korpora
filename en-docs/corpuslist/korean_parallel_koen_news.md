---
sort: 12
---

# 한영 병렬 말뭉치

한영 병렬 말뭉치는 jungyeul@github 님이 공개한 데이터입니다.
데이터 정보는 다음과 같습니다.

- author: jungyeul@github
- repository: [https://github.com/jungyeul/korean-parallel-corpora](https://github.com/jungyeul/korean-parallel-corpora)
- size:
  - train: 94,123 pairs
  - dev: 1,000 pairs
  - test: 2,000 pairs

데이터 구조는 다음과 같습니다.

|속성명|내용|
|---|---|
|text|한국어 문장|
|pair|영어 문장|

## 1. 파이썬에서 사용하기

파이썬 콘솔을 실행한 뒤 말뭉치를 내려받고 읽어들일 수 있습니다.

### 말뭉치 다운로드

한영 병렬 말뭉치를 로컬에 내려 받는 파이썬 예제는 다음과 같습니다.

```python
from Korpora import Korpora
Korpora.fetch("korean_parallel_koen_news")
```

```note
기본적으로 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리에 말뭉치를 내려 받습니다(`~/Korpora`). 다른 경로에 말뭉치를 다운로드 받고 싶다면 
fetch 함수 실행시 `root_dir=custom_path`라는 인자를 추가하세요.
```

```tip
fetch 함수 실행시 `force_download=True`라는 인자를 줄 경우 해당 말뭉치가 이미 로컬에 있더라도 이를 무시하고 다시 내려 받습니다. 기본값은 `False`입니다.
```


### 말뭉치 읽어들이기

한영 병렬 말뭉치를 파이썬 콘솔에서 읽어들이는 예제는 다음과 같습니다.
말뭉치가 로컬에 없다면 다운로드도 함께 수행합니다.

```python
from Korpora import Korpora
corpus = Korpora.load("korean_parallel_koen_news")
```

다음과 같이 실행해도 한영 병렬 말뭉치를 읽어들일 수 있습니다.
수행 결과는 위의 코드와 동일합니다.

```python
from Korpora import KoreanParallelKOENNewsKorpus
corpus = KoreanParallelKOENNewsKorpus()
```

위 코드 둘 중 하나를 택해 실행하면 `corpus`라는 변수에 말뭉치를 로드합니다.
`train`은 한영 병렬 말뭉치의 train 데이터로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
>>> corpus.train[0]
SentencePair(text='개인용 컴퓨터 사용의 상당 부분은 "이것보다 뛰어날 수 있느냐?"', pair='Much of personal computing is about "can you top this?"')
>>> corpus.train[0].text
개인용 컴퓨터 사용의 상당 부분은 "이것보다 뛰어날 수 있느냐?"
>>> corpus.train[0].pair
Much of personal computing is about "can you top this?"
```

`dev`, `test`는 각각 한영 병렬 말뭉치의 dev, test 데이터로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
>>> corpus.test[0]
SentencePair(text='토론에 참여한 사람들은 법 집행과 국가 ...', pair='Those involved in the discussions do take seriously ...')
>>> corpus.dev[0]
SentencePair(text='세계 에서 가장 강력한 수퍼컴퓨터를 1년...', pair="After keeping the world's most powerful supercomputer ...")
```

`get_all_texts`라는 메소드를 실행하면 한영 병렬 말뭉치의 모든 text(한국어 문장)를 확인할 수 있습니다.

```
>>> corpus.get_all_texts()
['세계 에서 가장 강력한 수퍼컴퓨터를 1년...', ... ]
```

`corpus.train`에서 `get_all_texts`, `get_all_pairs`라는 메소드를 각각 실행하면 한영 병렬 말뭉치 train의 모든 text(한국어 문장), pair(영어 문장)를 확인할 수 있습니다.
이는 `corpus.dev`, `corpus.test`에서도 마찬가지입니다.

```
>>> corpus.train.get_all_texts()
['개인용 컴퓨터 사용의 상당 부분은 "이것보다 뛰어날 수 있느냐?"', ... ]
>>> corpus.train.get_all_pairs()
['Much of personal computing is...', ... ]
```


## 2. 터미널에서 사용하기

파이썬 콘솔 실행 없이 바로 말뭉치를 다운받을 수 있습니다.
다음과 같이 실행하면 됩니다.

```bash
korpora fetch --corpus korean_parallel_koen_news
```

```note
기본적으로 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리에 말뭉치를 내려 받습니다(`~/Korpora`). 다른 경로에 말뭉치를 다운로드 받고 싶다면 
터미널에서 fetch 함수 실행시 `--root_dir custom_path`라는 인자를 추가하세요.
```

```tip
터미널에서 fetch 함수 실행시 `--force_download`라는 인자를 줄 경우 해당 말뭉치가 이미 로컬에 있더라도 이를 무시하고 다시 내려 받습니다.
```

