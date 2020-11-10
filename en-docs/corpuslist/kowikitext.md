---
sort: 7
---

# 한국어 위키 텍스트

한국어 위키 텍스트는 lovit@github 님이 한국어 위키백과를 텍스트 형태로 가공해 공개한 데이터입니다.
데이터 정보는 다음과 같습니다.

- author: lovit@github
- repository: [https://github.com/lovit/kowikitext](https://github.com/lovit/kowikitext)
- size:
  - train : 26794425 lines (877754 articles, 1.7G)
  - dev : 130419 lines (4433 articles, 7.7M)
  - test : 134340 lines (4434 articles, 8.4M)

데이터 구조는 다음과 같습니다.

|속성명|내용|
|---|---|
|text|섹션 본문|
|pair|섹션 타이틀|


## 1. 파이썬에서 사용하기

파이썬 콘솔을 실행한 뒤 말뭉치를 내려받고 읽어들일 수 있습니다.

### 말뭉치 다운로드

한국어 위키 텍스트를 로컬에 내려 받는 파이썬 예제는 다음과 같습니다.

```python
from Korpora import Korpora
Korpora.fetch("kowikitext")
```

```note
기본적으로 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리에 말뭉치를 내려 받습니다(`~/Korpora`). 다른 경로에 말뭉치를 다운로드 받고 싶다면 
fetch 함수 실행시 `root_dir=custom_path`라는 인자를 추가하세요.
```

```tip
fetch 함수 실행시 `force_download=True`라는 인자를 줄 경우 해당 말뭉치가 이미 로컬에 있더라도 이를 무시하고 다시 내려 받습니다. 기본값은 `False`입니다.
```


### 말뭉치 읽어들이기

한국어 위키 텍스트를 파이썬 콘솔에서 읽어들이는 예제는 다음과 같습니다.
말뭉치가 로컬에 없다면 다운로드도 함께 수행합니다.

```python
from Korpora import Korpora
corpus = Korpora.load("kowikitext")
```

다음과 같이 실행해도 한국어 위키 텍스트를 읽어들일 수 있습니다.
수행 결과는 위의 코드와 동일합니다.

```python
from Korpora import KowikiTextKorpus
corpus = KowikiTextKorpus()
```

위 코드 둘 중 하나를 택해 실행하면 `corpus`라는 변수에 말뭉치를 로드합니다.
`train`은 한국어 위키 텍스트의 train 데이터로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
>>> corpus.train[0]
SentencePair(text='외교부장\n외교부장', pair=' = 분류:중화인민공화국의 외교부장 =')
>>> corpus.train[0].text
'외교부장\n외교부장'
>>> corpus.train[0].pair
= 분류:중화인민공화국의 외교부장 =
```

`dev`, `test`는 각각 한국어 위키 텍스트의 dev, test 데이터로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
>>> corpus.dev[0]
SentencePair(text='스폴리아텔레(, )는 이탈리아의 후식으로서 ...', pair=' = 스폴리아텔레 =')
>>> corpus.test[0]
SentencePair(text='기타', pair=' = 분류:러시아의 기타 연주자 =')
```

`get_all_texts`라는 메소드를 실행하면 한국어 위키 텍스트의 모든 text(섹션 본문)를 확인할 수 있습니다.

```
>>> corpus.get_all_texts()
['외교부장\n외교부장', ... ]
```

`get_all_pairs`라는 메소드를 실행하면 한국어 위키 텍스트의 모든 pair(섹션 타이틀)를 확인할 수 있습니다.

```
>>> corpus.get_all_pairs()
['= 분류:중화인민공화국의 외교부장 =', ... ]
```


## 2. 터미널에서 사용하기

파이썬 콘솔 실행 없이 바로 말뭉치를 다운받을 수 있습니다.
다음과 같이 실행하면 됩니다.

```bash
korpora fetch --corpus kowikitext
```

```note
기본적으로 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리에 말뭉치를 내려 받습니다(`~/Korpora`). 다른 경로에 말뭉치를 다운로드 받고 싶다면 
터미널에서 fetch 함수 실행시 `--root_dir custom_path`라는 인자를 추가하세요.
```

```tip
터미널에서 fetch 함수 실행시 `--force_download`라는 인자를 줄 경우 해당 말뭉치가 이미 로컬에 있더라도 이를 무시하고 다시 내려 받습니다.
```

