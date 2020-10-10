---
sort: 8
---

# 나무 위키 텍스트

나무 위키 텍스트는 lovit@github 님이 나무 위키 백과를 텍스트 형태로 가공해 공개한 데이터입니다.
데이터 정보는 다음과 같습니다.

- author: lovit@github
- repository: [https://github.com/lovit/namuwikitext](https://github.com/lovit/namuwikitext)
- size:
  - train: 38,278,040 lines (500,104 docs, 5.3G)
  - dev: 197,723 lines (2,525 docs, 28M)
  - test: 193,614 lines (2,525 docs, 29M)

데이터 구조는 다음과 같습니다.

|속성명|내용|
|---|---|
|text|섹션 본문|
|pair|섹션 타이틀|


## 1. 파이썬에서 사용하기

파이썬 콘솔을 실행한 뒤 말뭉치를 내려받고 읽어들일 수 있습니다.

### 말뭉치 다운로드

나무 위키 텍스트를 로컬에 내려 받는 파이썬 예제는 다음과 같습니다.

```python
from Korpora import Korpora
Korpora.fetch("namuwikitext")
```

```note
기본적으로 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리에 말뭉치를 내려 받습니다(`~/Korpora`). 다른 경로에 말뭉치를 다운로드 받고 싶다면
fetch 함수 실행시 `root_dir=custom_path`라는 인자를 추가하세요.
```

```tip
fetch 함수 실행시 `force_download=True`라는 인자를 줄 경우 해당 말뭉치가 이미 로컬에 있더라도 이를 무시하고 다시 내려 받습니다. 기본값은 `False`입니다.
```


### 말뭉치 읽어들이기

나무 위키 텍스트를 파이썬 콘솔에서 읽어들이는 예제는 다음과 같습니다.
말뭉치가 로컬에 없다면 다운로드도 함께 수행합니다.

```python
from Korpora import Korpora
corpus = Korpora.load("namuwikitext")
```

다음과 같이 실행해도 나무 위키 텍스트를 읽어들일 수 있습니다.
수행 결과는 위의 코드와 동일합니다.

```python
from Korpora import NamuwikiTextKorpus
corpus = NamuwikiTextKorpus()
```

위 코드 둘 중 하나를 택해 실행하면 `corpus`라는 변수에 말뭉치를 로드합니다.
`train`은 나무 위키 텍스트의 train 데이터로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
>>> corpus.train[0]
SentencePair(text='상위 문서: 아스날 FC\n2009-10 시즌 2011-12 시즌\n2010 -11 시즌...', pair=' = 아스날 FC/2010-11 시즌 =')
>>> corpus.train[0].text
상위 문서: 아스날 FC\n2009-10 시즌 2011-12 시즌\n2010 -11 시즌...
>>> corpus.train[0].pair
= 아스날 FC/2010-11 시즌 =
```

`dev`, `test`는 각각 나무 위키 텍스트의 dev, test 데이터로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
>>> corpus.dev[0]
SentencePair(text='상위 항목: 축구 관련 인물, 외국인 선수/역대 프로축구\n...', pair=' = 소말리아(축구선수) =')
>>> corpus.test[0]
SentencePair(text='', pair=' = 덴덴타운 =')
```

`get_all_texts`라는 메소드를 실행하면 나무 위키 텍스트의 모든 text(섹션 본문)를 확인할 수 있습니다.

```
>>> corpus.get_all_texts()
['상위 문서: 아스날 FC\n2009-10 시즌 2011-12 시즌\n2010 -11 시즌...', ... ]
```

`get_all_pairs`라는 메소드를 실행하면 나무 위키 텍스의 모든 pair(섹션 타이틀)를 확인할 수 있습니다.

```
>>> corpus.get_all_pairs()
['= 아스날 FC/2010-11 시즌 =', ... ]
```


## 2. 터미널에서 사용하기

파이썬 콘솔 실행 없이 바로 말뭉치를 다운받을 수 있습니다.
다음과 같이 실행하면 됩니다.

```bash
korpora fetch --corpus namuwikitext
```

```note
기본적으로 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리에 말뭉치를 내려 받습니다(`~/Korpora`). 다른 경로에 말뭉치를 다운로드 받고 싶다면
터미널에서 fetch 함수 실행시 `--root_dir custom_path`라는 인자를 추가하세요.
```

```tip
터미널에서 fetch 함수 실행시 `--force_download`라는 인자를 줄 경우 해당 말뭉치가 이미 로컬에 있더라도 이를 무시하고 다시 내려 받습니다.
```