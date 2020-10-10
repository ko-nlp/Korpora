---
sort: 3
---

# 빠른 사용법

`Korpora` 패키지의 핵심 기능을 빠르게 살펴봅니다.

## 파이썬에서 사용하기

`Korpora`는 오픈소스 파이썬 패키지입니다.
기본적으로 파이썬 콘솔(console)에서 동작합니다. 

### 말뭉치 목록 확인

`Korpora` 패키지가 제공하는 말뭉치 목록을 확인하는 파이썬 예제는 다음과 같습니다.

```python
from Korpora import Korpora
Korpora.corpus_list()
```

```python
{
   'kcbert': 'beomi@github 님이 만드신 KcBERT 학습데이터',
   'korean_chatbot_data': 'songys@github 님이 만드신 챗봇 문답 데이터',
   'korean_hate_speech': '{inmoonlight,warnikchow,beomi}@github 님이 만드신 혐오댓글데이터',
   'korean_petitions': 'lovit@github 님이 만드신 2017.08 ~ 2019.03 청와대 청원데이터',
   'kornli': 'KakaoBrain 에서 제공하는 Natural Language Inference (NLI) 데이터',
   'korsts': 'KakaoBrain 에서 제공하는 Semantic Textual Similarity (STS) 데이터',
   'namuwikitext': 'lovit@github 님이 만드신 wikitext 형식의 나무위키 데이터',
   'naver_changwon_ner': '네이버 + 창원대 NER shared task data',
   'nsmc': 'e9t@github 님이 만드신 Naver sentiment movie corpus v1.0',
   'question_pair': 'songys@github 님이 만드신 질문쌍(Paired Question v.2)',
}
```

### 말뭉치 다운로드

KcBERT 학습데이터를 내려 받는 파이썬 예제는 다음과 같습니다.
다른 데이터를 받고 싶다면 위에서 확인한 말뭉치 이름을 인자로 주면 됩니다.

```python
from Korpora import Korpora
Korpora.fetch("kcbert")
```

```note
기본적으로 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리에 말뭉치를 내려 받습니다(`~/Korpora`). 다른 경로에 말뭉치를 다운로드 받고 싶다면 
fetch 함수 실행시 `root_dir=custom_path`라는 인자를 추가하세요.
```

```tip
fetch 함수 실행시 `force_download=True`라는 인자를 줄 경우 해당 말뭉치가 이미 로컬에 있더라도 이를 무시하고 다시 내려 받습니다. 기본값은 `False`입니다.
```

`Korpora`가 제공하는 모든 말뭉치를 내려받고 싶다면 다음과 같이 실행하세요.

```python
from Korpora import Korpora
Korpora.fetch('all')
```

```warning
국립국어원에서 제공하는 '모두의 말뭉치'는 라이센스 문제로 `Korpora` 패키지에서는 다운로드 기능을 제공하지 않습니다. 
해당 말뭉치를 사용하고 싶다면 국립국어원 안내대로 인증 과정을 거쳐 수작업으로 말뭉치를 내려받아야 합니다.
```

### 말뭉치 읽어들이기

KcBERT 학습데이터를 파이썬 콘솔에서 읽어들이는 예제는 다음과 같습니다.
다른 데이터를 읽고 싶다면 위에서 확인한 말뭉치 이름을 인자로 주면 됩니다.

```python
from Korpora import Korpora
corpus = Korpora.load("kcbert")
```

위 코드를 실행하면 `corpus`라는 파이썬 변수에 말뭉치 데이터가 담기게 됩니다.
만일 로컬에 데이터가 없다면 다운로드까지 한번에 수행합니다.
한편 `corpus`는 말뭉치별로 그 내용과 구조가 다릅니다.
데이터 내용과 구조에 관해서는 이 페이지의 각 말뭉치 설명 란을 참고하세요.


## 터미널에서 사용하기

`Korpora`는 터미널에서도 동작합니다(Command Line Interface, CLI).
파이썬 콘솔 실행 없이 바로 말뭉치를 다운받을 수 있습니다.
터미널에서 KcBERT 학습데이터 하나를 다운받는 예제는 다음과 같습니다.

```bash
korpora fetch --corpus kcbert
```

```note
기본적으로 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리에 말뭉치를 내려 받습니다(`~/Korpora`). 다른 경로에 말뭉치를 다운로드 받고 싶다면 
터미널에서 fetch 함수 실행시 `--root_dir custom_path`라는 인자를 추가하세요.
```

```tip
fetch 함수 실행시 `--force_download`라는 인자를 줄 경우 해당 말뭉치가 이미 로컬에 있더라도 이를 무시하고 다시 내려 받습니다.
```

터미널에서 KcBERT 학습데이터와 챗봇 문답 데이터 두 개를 동시에 다운로드 받는 예제는 다음과 같습니다.
이같은 방식으로 3개 이상의 데이터도 동시에 내려받을 수 있습니다.

```bash
korpora fetch --corpus kcbert korean_chatbot_data
```

터미널에서 `Korpora`가 제공하는 모든 말뭉치를 내려받는 예제는 다음과 같습니다.

```bash
korpora fetch --corpus all
```

```warning
국립국어원에서 제공하는 '모두의 말뭉치'는 라이센스 문제로 `Korpora` 패키지에서는 다운로드 기능을 제공하지 않습니다. 
해당 말뭉치를 사용하고 싶다면 국립국어원 안내대로 인증 과정을 거쳐 수작업으로 말뭉치를 내려받아야 합니다.
```
