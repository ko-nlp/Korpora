---
sort: 9
---

# 네이버 x 창원대 NER 데이터

네이버 x 창원대 NER 데이터는 lovit@github 님이 한국어 위키백과를 텍스트 형태로 가공해 공개한 데이터입니다.
데이터 정보는 다음과 같습니다.

- author: 네이버 + 창원대
- repository: [https://github.com/naver/nlp-challenge/tree/master/missions/ner](https://github.com/naver/nlp-challenge/tree/master/missions/ner)
- reference: [http://air.changwon.ac.kr/?page_id=10](http://air.changwon.ac.kr/?page_id=10)
- size:
  - train: 90,000 examples

데이터 구조는 다음과 같습니다.

|속성명|내용|
|---|---|
|text|words를 공백으로 이어 붙인 string|
|words|단어 시퀀스|
|tags|words에 대응하는 개체명 태그 시퀀스|


## 1. 파이썬에서 사용하기

파이썬 콘솔을 실행한 뒤 말뭉치를 내려받고 읽어들일 수 있습니다.

### 말뭉치 다운로드

네이버 x 창원대 NER 데이터를 로컬에 내려 받는 파이썬 예제는 다음과 같습니다.

```python
from Korpora import Korpora
Korpora.fetch("naver_changwon_ner")
```

```note
기본적으로 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리에 말뭉치를 내려 받습니다(`~/Korpora`). 다른 경로에 말뭉치를 다운로드 받고 싶다면 
fetch 함수 실행시 `root_dir=custom_path`라는 인자를 추가하세요.
```

```tip
fetch 함수 실행시 `force_download=True`라는 인자를 줄 경우 해당 말뭉치가 이미 로컬에 있더라도 이를 무시하고 다시 내려 받습니다. 기본값은 `False`입니다.
```


### 말뭉치 읽어들이기

네이버 x 창원대 NER 데이터를 파이썬 콘솔에서 읽어들이는 예제는 다음과 같습니다.
말뭉치가 로컬에 없다면 다운로드도 함께 수행합니다.

```python
from Korpora import Korpora
corpus = Korpora.load("naver_changwon_ner")
```

다음과 같이 실행해도 한국어 위키 텍스트를 읽어들일 수 있습니다.
수행 결과는 위의 코드와 동일합니다.

```python
from Korpora import NaverChangwonNERKorpus
corpus = NaverChangwonNERKorpus()
```

위 코드 둘 중 하나를 택해 실행하면 `corpus`라는 변수에 말뭉치를 로드합니다.
`train`은 네이버 x 창원대 NER 데이터의 train 데이터로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
>>> corpus.train[0]
WordTag(text='비토리오 양일 만에 영사관 감호 용퇴, 항룡 압력설 의심만 가율 ', words=['비토리오', '양일', '만에', '영사관', '감호', '용퇴,', '항룡', '압력설', '의심만', '가율'], tags=['PER_B', 'DAT_B', '-', 'ORG_B', 'CVL_B', '-', '-', '-', '-', '-'])
>>> corpus.train[0].text
비토리오 양일 만에 영사관 감호 용퇴, 항룡 압력설 의심만 가율 
>>> corpus.train[0].words
['비토리오', '양일', '만에', '영사관', '감호', '용퇴,', '항룡', '압력설', '의심만', '가율']
>>> corpus.train[0].tags
['PER_B', 'DAT_B', '-', 'ORG_B', 'CVL_B', '-', '-', '-', '-', '-']
```

`get_all_words`라는 메소드를 실행하면 네이버 x 창원대 NER 데이터의 모든 word(단어 시퀀스)를 확인할 수 있습니다.

```
>>> corpus.get_all_words()
[['비토리오', '양일', '만에', '영사관', '감호', '용퇴,', '항룡', '압력설', '의심만', '가율'], ... ]
```

`get_all_tags`라는 메소드를 실행하면 네이버 x 창원대 NER 데이터의 모든 tag(words에 대응하는 개체명 태그 시퀀스)를 확인할 수 있습니다.

```
>>> corpus.get_all_tags()
[['PER_B', 'DAT_B', '-', 'ORG_B', 'CVL_B', '-', '-', '-', '-', '-'], ... ]
```

`get_all_texts`라는 메소드를 실행하면 네이버 x 창원대 NER 데이터의 모든 text(words를 공백으로 이어 붙인 string)를 확인할 수 있습니다.

```
>>> corpus.get_all_texts()
['비토리오 양일 만에 영사관 감호 용퇴, 항룡 압력설 의심만 가율 ', ... ]
```



## 2. 터미널에서 사용하기

파이썬 콘솔 실행 없이 바로 말뭉치를 다운받을 수 있습니다.
다음과 같이 실행하면 됩니다.

```bash
korpora fetch --corpus naver_changwon_ner
```

```note
기본적으로 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리에 말뭉치를 내려 받습니다(`~/Korpora`). 다른 경로에 말뭉치를 다운로드 받고 싶다면 
터미널에서 fetch 함수 실행시 `--root_dir custom_path`라는 인자를 추가하세요.
```

```tip
터미널에서 fetch 함수 실행시 `--force_download`라는 인자를 줄 경우 해당 말뭉치가 이미 로컬에 있더라도 이를 무시하고 다시 내려 받습니다.
```