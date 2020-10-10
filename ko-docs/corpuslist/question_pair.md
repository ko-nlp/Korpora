---
sort: 11
---

# 한국어 질문쌍

한국어 질문쌍(Paired Question v.2)는 songys@github 님이 공개한 데이터입니다.
데이터 정보는 다음과 같습니다.

- author: songys@github
- repository: [https://github.com/songys/Question_pair](https://github.com/songys/Question_pair)
- size:
  - train: 6,888 examples
  - test: 688 examples

데이터 구조는 다음과 같습니다.

|속성명|내용|
|---|---|
|text|문장|
|pair|text와 쌍을 이루는 문장|
|label|text와 pair가 같은 질문이면 0, 다른 질문이면 1|

## 1. 파이썬에서 사용하기

파이썬 콘솔을 실행한 뒤 말뭉치를 내려받고 읽어들일 수 있습니다.

### 말뭉치 다운로드

한국어 질문쌍을 로컬에 내려 받는 파이썬 예제는 다음과 같습니다.

```python
from Korpora import Korpora
Korpora.fetch("question_pair")
```

```note
기본적으로 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리에 말뭉치를 내려 받습니다(`~/Korpora`). 다른 경로에 말뭉치를 다운로드 받고 싶다면 
fetch 함수 실행시 `root_dir=custom_path`라는 인자를 추가하세요.
```

```tip
fetch 함수 실행시 `force_download=True`라는 인자를 줄 경우 해당 말뭉치가 이미 로컬에 있더라도 이를 무시하고 다시 내려 받습니다. 기본값은 `False`입니다.
```


### 말뭉치 읽어들이기

한국어 질문쌍을 파이썬 콘솔에서 읽어들이는 예제는 다음과 같습니다.
말뭉치가 로컬에 없다면 다운로드도 함께 수행합니다.

```python
from Korpora import Korpora
corpus = Korpora.load("question_pair")
```

다음과 같이 실행해도 한국어 질문쌍을 읽어들일 수 있습니다.
수행 결과는 위의 코드와 동일합니다.

```python
from Korpora import QuestionPairKorpus
corpus = QuestionPairKorpus()
```

위 코드 둘 중 하나를 택해 실행하면 `corpus`라는 변수에 말뭉치를 로드합니다.
`train`은 한국어 질문쌍의 train 데이터로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
>>> corpus.train[0]
LabeledSentencePair(text='1000일 만난 여자친구와 이별', pair='10년 연예의끝', label='1')
>>> corpus.train[0].text
1000일 만난 여자친구와 이별
>>> corpus.train[0].pair
10년 연예의끝
>>> corpus.train[0].label
1
```

`test`는 한국어 질문쌍의 test 데이터로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
>>> corpus.test[0]
LabeledSentencePair(text='21살의 사랑에 대해', pair='사랑을 노력한다는게 말이 되나요?', label='1')
```

`get_all_texts`라는 메소드를 실행하면 한국어 질문쌍의 모든 text(문장)를 확인할 수 있습니다.

```
>>> corpus.get_all_texts()
['1000일 만난 여자친구와 이별', ... ]
```

`get_all_pairs`라는 메소드를 실행하면 한국어 질문쌍의 모든 pair(text와 쌍을 이루는 문장)를 확인할 수 있습니다.

```
>>> corpus.get_all_pairs()
[SentencePair(text='1000일 만난 여자친구와 이별', pair='10년 연예의끝'), ... ]
```

`get_all_labels`라는 메소드를 실행하면 한국어 질문쌍의 모든 label(text와 pair가 같은 질문이면 0, 다른 질문이면 1)를 확인할 수 있습니다.

```
>>> corpus.get_all_labels()
['1', ... ]
```


## 2. 터미널에서 사용하기

파이썬 콘솔 실행 없이 바로 말뭉치를 다운받을 수 있습니다.
다음과 같이 실행하면 됩니다.

```bash
korpora fetch --corpus question_pair
```

```note
기본적으로 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리에 말뭉치를 내려 받습니다(`~/Korpora`). 다른 경로에 말뭉치를 다운로드 받고 싶다면 
터미널에서 fetch 함수 실행시 `--root_dir custom_path`라는 인자를 추가하세요.
```

```tip
터미널에서 fetch 함수 실행시 `--force_download`라는 인자를 줄 경우 해당 말뭉치가 이미 로컬에 있더라도 이를 무시하고 다시 내려 받습니다.
```