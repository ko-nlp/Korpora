---
sort: 3
---

# 한국어 혐오 데이터셋

한국어 혐오 데이터셋은 inmoonlight@github, warnikchow@github, beomi@github 님이 만드신 데이터입니다.
데이터 정보는 다음과 같습니다.

- author: inmoonlight@github, warnikchow@github, beomi@github
- repository: https://github.com/kocohub/korean-hate-speech
- size:
  - train: 7,896 examples
  - dev: 471 examples
  - test: 974 examples
  - unlabeled: 2,033,893 examples

데이터 구조는 다음과 같습니다.

|속성명|내용|
|---|---|
|text|뉴스 댓글|
|title/pair|뉴스 제목|
|gender_bias|성적 차별 여부(True/False)|
|bias|차별 종류(종교 인종 나이 외모 등)|
|hate|특정 계층 혐오 여부(hate/none)|


## 1. 파이썬에서 사용하기

파이썬 콘솔을 실행한 뒤 말뭉치를 내려받고 읽어들일 수 있습니다.

### 말뭉치 다운로드

한국어 혐오 데이터셋을 로컬에 내려 받는 파이썬 예제는 다음과 같습니다.

```python
from Korpora import Korpora
Korpora.fetch("korean_hate_speech")
```

```note
기본적으로 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리에 말뭉치를 내려 받습니다(`~/Korpora`). 다른 경로에 말뭉치를 다운로드 받고 싶다면 
fetch 함수 실행시 `root_dir=custom_path`라는 인자를 추가하세요.
```

```tip
fetch 함수 실행시 `force_download=True`라는 인자를 줄 경우 해당 말뭉치가 이미 로컬에 있더라도 이를 무시하고 다시 내려 받습니다. 기본값은 `False`입니다.
```


### 말뭉치 읽어들이기

한국어 혐오 데이터셋을 파이썬 콘솔에서 읽어들이는 예제는 다음과 같습니다.
말뭉치가 로컬에 없다면 다운로드도 함께 수행합니다.

```python
from Korpora import Korpora
corpus = Korpora.load("korean_hate_speech")
```

다음과 같이 실행해도 한국어 혐오 데이터셋을 읽어들일 수 있습니다.
수행 결과는 위의 코드와 동일합니다.

```python
from Korpora import KoreanHateSpeechKorpus
corpus = KoreanHateSpeechKorpus()
```

위 코드 둘 중 하나를 택해 실행하면 `corpus`라는 변수에 말뭉치를 로드합니다.
`train`은 한국어 혐오 데이터셋의 train 데이터로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
>>> corpus.train[0]
KoreanHateSpeechLabeledExample(text='(현재 호텔주인 심정) 아18...', title='"밤새 조문 행렬...', gender_bias='False', bias='others', hate='hate')
>>> corpus.train[0].text
(현재 호텔주인 심정) 아18...(현재 호텔주인 심정) 아18...
>>> corpus.train[0].title
"밤새 조문 행렬...
>>> corpus.train[0].gender_bias
False
>>> corpus.train[0].bias
others
>>> corpus.train[0].hate
hate
```

`dev`, `test`, `unlabeled`는 각각 한국어 혐오 데이터셋의 dev, test, unlabeled 데이터로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
>>> korean_hate_speech.dev[0]
KoreanHateSpeechLabeledExample(text='송중기 시대극은 믿고본다...', title='"'아스달 연대기\'...', gender_bias='False', bias='none', hate='none')
>>> korean_hate_speech.test[0]
SentencePair(text='ㅋㅋㅋㅋ 그래도 조아해주는 팬들 많아서 좋겠다 ㅠㅠ 니들은 온유가 안만져줌 ㅠㅠ', pair='"샤이니 온유, 클럽 강제추행 \'무혐의\' 처분 받았다"')
>>> korean_hate_speech.unlabeled[0]
SentencePair(text='"[단독] 지드래곤♥이주연, 제주도 데이트...', pair='"[단독] 지드래곤♥이주연, 제주도 데이트...')
```

`get_all_texts`라는 메소드를 실행하면 한국어 혐오 데이터셋의 모든 text(뉴스 댓글)를 확인할 수 있습니다.

```
>>> corpus.get_all_texts()
['송중기 시대극은 믿고본다. 첫회 신선하고 좋았다.', ... ]
```

`train`, `dev`, `test`, `unlabeled` 각각에 대해서도 `get_all_texts` 메소드 실행이 가능합니다.

```
>>> corpus.train.get_all_texts()
['(현재 호텔주인 심정) 아18 난 마른하늘에 날벼락맞고 호텔망하게생겼는데 누군 계속 추모받네....', ... ]
>>> corpus.dev.get_all_texts()
['송중기 시대극은 믿고본다. 첫회 신선하고 좋았다.', ... ]
>>> corpus.test.get_all_texts()
['ㅋㅋㅋㅋ 그래도 조아해주는 팬들 많아서 좋겠다 ㅠㅠ 니들은 온유가 안만져줌 ㅠㅠ', ... ]
>>> corpus.unlabeled.get_all_texts()
['"[단독] 지드래곤♥이주연, 제주도 데이트…2018년 1호 커플 탄생"', ... ]
```


## 2. 터미널에서 사용하기

파이썬 콘솔 실행 없이 바로 말뭉치를 다운받을 수 있습니다.
다음과 같이 실행하면 됩니다.

```bash
korpora fetch --corpus korean_hate_speech
```

```note
기본적으로 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리에 말뭉치를 내려 받습니다(`~/Korpora`). 다른 경로에 말뭉치를 다운로드 받고 싶다면 
터미널에서 fetch 함수 실행시 `--root_dir custom_path`라는 인자를 추가하세요.
```

```tip
터미널에서 fetch 함수 실행시 `--force_download`라는 인자를 줄 경우 해당 말뭉치가 이미 로컬에 있더라도 이를 무시하고 다시 내려 받습니다.
```
