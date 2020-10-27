---
sort: 4
---

# 청와대 국민청원

청와대 국민청원 데이터는 lovit@github 님이 공개한 청와대 국민청원 데이터(2017.08 ~ 2019.03)입니다.
데이터 정보는 다음과 같습니다.

- author: lovit@github
- repository: https://github.com/lovit/petitions_archive
- size:
  - train: 433,631 examples

데이터 구조는 다음과 같습니다.

|속성명|내용|
|---|---|
|text|청원 내용|
|category|청원 범주|
|num_agree|청원 동의 수|
|begin|청원 시작일|
|end|청원 종료일|
|title|청원 제목|

## 1. 파이썬에서 사용하기

파이썬 콘솔을 실행한 뒤 말뭉치를 내려받고 읽어들일 수 있습니다.

### 말뭉치 다운로드

청와대 국민청원 데이터를 로컬에 내려 받는 파이썬 예제는 다음과 같습니다.

```python
from Korpora import Korpora
Korpora.fetch("korean_petitions")
```

```note
기본적으로 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리에 말뭉치를 내려 받습니다(`~/Korpora`). 다른 경로에 말뭉치를 다운로드 받고 싶다면 
fetch 함수 실행시 `root_dir=custom_path`라는 인자를 추가하세요.
```

```tip
fetch 함수 실행시 `force_download=True`라는 인자를 줄 경우 해당 말뭉치가 이미 로컬에 있더라도 이를 무시하고 다시 내려 받습니다. 기본값은 `False`입니다.
```


### 말뭉치 읽어들이기

청와대 국민청원 데이터를 파이썬 콘솔에서 읽어들이는 예제는 다음과 같습니다.
말뭉치가 로컬에 없다면 다운로드도 함께 수행합니다.

```python
from Korpora import Korpora
corpus = Korpora.load("korean_petitions")
```

다음과 같이 실행해도 청와대 국민청원 데이터를 읽어들일 수 있습니다.
수행 결과는 위의 코드와 동일합니다.

```python
from Korpora import KoreanPetitionsKorpus
corpus = KoreanPetitionsKorpus()
```

위 코드 둘 중 하나를 택해 실행하면 `corpus`라는 변수에 말뭉치를 로드합니다.
`train`은 청와대 국민청원 데이터의 train 데이터로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
>>> corpus.train[0]
KoreanPetition(text="안녕하세요. 현재 사대, ...", category='육아/교육', num_agree=88, begin='2017-08-25', end='2017-09-24', title='학교는 ...')
>>> corpus.train[0].text
안녕하세요. 현재 사대, ...
>>> corpus.train[0].category
육아/교육
>>> corpus.train[0].num_agree
88
>>> corpus.train[0].begin
2017-08-25
>>> corpus.train[0].end
2017-09-24
>>> corpus.train[0].title
학교는 
```

`get_all_texts`라는 메소드를 실행하면 청와대 국민청원 데이터의 모든 text(청원 내용)를 확인할 수 있습니다.
`get_all_categories` 메소드를 실행하면 청와대 국민청원 데이터의 모든 category(청원 범주)를 확인할 수 있습니다.
`get_all_num_agrees` 메소드를 실행하면 청와대 국민청원 데이터의 모든 num_agree(청원 동의 수)를 확인할 수 있습니다.
`get_all_titles` 메소드를 실행하면 청와대 국민청원 데이터의 모든 title(청원 제목)을 확인할 수 있습니다.

## 2. 터미널에서 사용하기

파이썬 콘솔 실행 없이 바로 말뭉치를 다운받을 수 있습니다.
다음과 같이 실행하면 됩니다.

```bash
korpora fetch --corpus korean_petitions
```

```note
기본적으로 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리에 말뭉치를 내려 받습니다(`~/Korpora`). 다른 경로에 말뭉치를 다운로드 받고 싶다면 
터미널에서 fetch 함수 실행시 `--root_dir custom_path`라는 인자를 추가하세요.
```

```tip
터미널에서 fetch 함수 실행시 `--force_download`라는 인자를 줄 경우 해당 말뭉치가 이미 로컬에 있더라도 이를 무시하고 다시 내려 받습니다.
```

