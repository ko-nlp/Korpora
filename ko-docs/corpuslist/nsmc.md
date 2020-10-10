---
sort: 10
---

# NAVER Sentiment Movie Corpus

NAVER Sentiment Movie Corpus(NSMC)는 e9t@github 님이 가공해 공개한 영화 리뷰 데이터입니다.
데이터 정보는 다음과 같습니다.

- author: e9t@github
- repository: https://github.com/e9t/nsmc
- references: www.lucypark.kr/docs/2015-pyconkr/#39
- size:
  - train: 150,000 examples
  - test: 50,000 examples

데이터 구조는 다음과 같습니다.

|속성명|내용|
|---|---|
|text|영화 리뷰 댓글|
|label|영화에 대한 평가 (긍정 1, 부정 0)|

## 1. 파이썬에서 사용하기

파이썬 콘솔을 실행한 뒤 말뭉치를 내려받고 읽어들일 수 있습니다.

### 말뭉치 다운로드

NSMC를 로컬에 내려 받는 파이썬 예제는 다음과 같습니다.

```python
from Korpora import Korpora
Korpora.fetch("nsmc")
```

```note
기본적으로 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리에 말뭉치를 내려 받습니다(`~/Korpora`). 다른 경로에 말뭉치를 다운로드 받고 싶다면 
fetch 함수 실행시 `root_dir=custom_path`라는 인자를 추가하세요.
```

```tip
fetch 함수 실행시 `force_download=True`라는 인자를 줄 경우 해당 말뭉치가 이미 로컬에 있더라도 이를 무시하고 다시 내려 받습니다. 기본값은 `False`입니다.
```


### 말뭉치 읽어들이기

NSMC를 파이썬 콘솔에서 읽어들이는 예제는 다음과 같습니다.
말뭉치가 로컬에 없다면 다운로드도 함께 수행합니다.

```python
from Korpora import Korpora
corpus = Korpora.load("nsmc")
```

다음과 같이 실행해도 NSMC를 읽어들일 수 있습니다.
수행 결과는 위의 코드와 동일합니다.

```python
from Korpora import NSMCKorpus
corpus = NSMCKorpus()
```

위 코드 둘 중 하나를 택해 실행하면 `corpus`라는 변수에 말뭉치를 로드합니다.
`train`은 NSMC의 train 데이터로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
nsmc.train[0]
# LabeledSentence(text='아 더빙.. 진짜 짜증나네요 목소리', label=0)
nsmc.train[0].text
# 아 더빙.. 진짜 짜증나네요 목소리
nsmc.train[0].label
# 0
```

`get_all_texts`라는 메소드를 실행하면 NSMC의 모든 text(영화 리뷰 댓글)를 확인할 수 있습니다.

```
>>> corpus.get_all_texts()
['아 더빙.. 진짜 짜증나네요 목소리', ... ]
```

`get_all_labels`라는 메소드를 실행하면 NSMC의 모든 label(긍정, 부정)를 확인할 수 있습니다.

```
>>> corpus.get_all_labels()
[0, ... ]
```



## 2. 터미널에서 사용하기

파이썬 콘솔 실행 없이 바로 말뭉치를 다운받을 수 있습니다.
다음과 같이 실행하면 됩니다.

```bash
korpora fetch --corpus nsmc
```

```note
기본적으로 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리에 말뭉치를 내려 받습니다(`~/Korpora`). 다른 경로에 말뭉치를 다운로드 받고 싶다면 
터미널에서 fetch 함수 실행시 `--root_dir custom_path`라는 인자를 추가하세요.
```

```tip
터미널에서 fetch 함수 실행시 `--force_download`라는 인자를 줄 경우 해당 말뭉치가 이미 로컬에 있더라도 이를 무시하고 다시 내려 받습니다.
```