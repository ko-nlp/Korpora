---
sort: 1
---

# 챗봇 문답 페어

챗봇 문답 페어는 songys@github 님이 만드신 챗봇 문답 데이터입니다.
데이터 정보는 다음과 같습니다.

- author: songys@github
- repository: https://github.com/songys/Chatbot_data
- size:
  - train: 11,876 examples

데이터 구조는 다음과 같습니다.

|속성명|내용|
|---|---|
|text|질문|
|pair|답변|
|label|일상다반사 0, 이별(부정) 1, 사랑(긍정) 2|


## 1. 파이썬에서 사용하기

파이썬 콘솔을 실행한 뒤 말뭉치를 내려받고 읽어들일 수 있습니다.

### 말뭉치 다운로드

챗봇 문답 페어를 로컬에 내려 받는 파이썬 예제는 다음과 같습니다.

```python
from Korpora import Korpora
Korpora.fetch("korean_chatbot_data")
```

```note
기본적으로 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리에 말뭉치를 내려 받습니다(`~/Korpora`). 다른 경로에 말뭉치를 다운로드 받고 싶다면 
fetch 함수 실행시 `root_dir=custom_path`라는 인자를 추가하세요.
```

```tip
fetch 함수 실행시 `force_download=True`라는 인자를 줄 경우 해당 말뭉치가 이미 로컬에 있더라도 이를 무시하고 다시 내려 받습니다. 기본값은 `False`입니다.
```


### 말뭉치 읽어들이기

챗봇 문답 페어를 파이썬 콘솔에서 읽어들이는 예제는 다음과 같습니다.
말뭉치가 로컬에 없다면 다운로드도 함께 수행합니다.

```python
from Korpora import Korpora
corpus = Korpora.load("korean_chatbot_data")
```

다음과 같이 실행해도 챗봇 문답 페어를 읽어들일 수 있습니다.
수행 결과는 위의 코드와 동일합니다.

```python
from Korpora import KoreanChatbotKorpus
corpus = KoreanChatbotKorpus()
```

위 코드 둘 중 하나를 택해 실행하면 `corpus`라는 변수에 다음과 같은 정보가 들어 있음을 확인할 수 있습니다.

```
>>> chatbot_corpus.train[0]
LabeledSentencePair(text='12시 땡!', pair='하루가 또 가네요.', label=0)
>>> chatbot_corpus.train[0].text
12시 땡!
>>> chatbot_corpus.train[0].pair
하루가 또 가네요.
>>> chatbot_corpus.train[0].label
0
```

## 2. 터미널에서 사용하기

파이썬 콘솔 실행 없이 바로 말뭉치를 다운받을 수 있습니다.
다음과 같이 실행하면 됩니다.

```bash
korpora fetch --corpus korean_chatbot_data
```

```note
기본적으로 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리에 말뭉치를 내려 받습니다(`~/Korpora`). 다른 경로에 말뭉치를 다운로드 받고 싶다면 
터미널에서 fetch 함수 실행시 `--root_dir custom_path`라는 인자를 추가하세요.
```

```tip
터미널에서 fetch 함수 실행시 `--force_download`라는 인자를 줄 경우 해당 말뭉치가 이미 로컬에 있더라도 이를 무시하고 다시 내려 받습니다.
```