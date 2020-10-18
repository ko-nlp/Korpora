---
sort: 21
---

# 영화 자막 한영 병렬 말뭉치

영화 자막 한영 병렬 말뭉치는 TRAC에서 공개한 데이터입니다.
데이터 정보는 다음과 같습니다.

- author: TRAC ([https://trac.edgewall.org](https://trac.edgewall.org))
- repository: [http://opus.nlpl.eu/OpenSubtitles-v2018.php](http://opus.nlpl.eu/OpenSubtitles-v2018.php)
- references: P. Lison and J. Tiedemann, 2016, OpenSubtitles2016: Extracting Large Parallel Corpora from Movie and TV Subtitles. In Proceedings of the 10th International Conference on Language Resources and Evaluation (LREC 2016)
- size:
  - train: 1,269,683 pairs

데이터 구조는 다음과 같습니다.

|속성명|내용|
|---|---|
|text|한국어 문장|
|pair|text와 쌍을 이루는 영어 문장|


## 1. 파이썬에서 사용하기

파이썬 콘솔을 실행한 뒤 말뭉치를 내려받고 읽어들일 수 있습니다.

### 말뭉치 다운로드

영화 자막 한영 병렬 말뭉치를 로컬에 내려 받는 파이썬 예제는 다음과 같습니다.

```python
from Korpora import Korpora
Korpora.fetch("open_substitles")
```

```note
기본적으로 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리에 말뭉치를 내려 받습니다(`~/Korpora`). 다른 경로에 말뭉치를 다운로드 받고 싶다면 
fetch 함수 실행시 `root_dir=custom_path`라는 인자를 추가하세요.
```

```tip
fetch 함수 실행시 `force_download=True`라는 인자를 줄 경우 해당 말뭉치가 이미 로컬에 있더라도 이를 무시하고 다시 내려 받습니다. 기본값은 `False`입니다.
```


### 말뭉치 읽어들이기

영화 자막 한영 병렬 말뭉치를 파이썬 콘솔에서 읽어들이는 예제는 다음과 같습니다.
말뭉치가 로컬에 없다면 다운로드도 함께 수행합니다.

```python
from Korpora import Korpora
corpus = Korpora.load("open_substitles")
```

다음과 같이 실행해도 영화 자막 한영 병렬 말뭉치를 읽어들일 수 있습니다.
수행 결과는 위의 코드와 동일합니다.

```python
from Korpora import OpenSubstitleKorpus
corpus = OpenSubstitleKorpus()
```

위 코드 둘 중 하나를 택해 실행하면 `corpus`라는 변수에 말뭉치를 로드합니다.
`train`은 영화 자막 한영 병렬 말뭉치의 train 데이터로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
>>> corpus.train[0]
SentencePair(text='폭설이 내리고 우박, 진눈깨비가 퍼부어도 눈보라가 몰아쳐도 강풍이 불고 비바람이 휘몰아쳐도', pair='Through the snow and sleet and hail, through the blizzard, through the gales, through the wind and through the rain, over mountain, over plain, through the blinding lightning flash, and the mighty thunder crash,')
>>> corpus.train[0].text
폭설이 내리고 우박, 진눈깨비가 퍼부어도 눈보라가 몰아쳐도 강풍이 불고 비바람이 휘몰아쳐도
>>> corpus.train[0].pair
Through the snow and sleet and hail, through the blizzard, through the gales, through the wind and through the rain, over mountain, over plain, through the blinding lightning flash, and the mighty thunder crash,
```

`get_all_texts`라는 메소드를 실행하면 영화 자막 한영 병렬 말뭉치의 모든 text(한국어 문장)를 확인할 수 있습니다.

```
>>> corpus.get_all_texts()
['폭설이 내리고 우박, 진눈깨비가 퍼부어도 눈보라가 몰아쳐도 강풍이 불고 비바람이 휘몰아쳐도', ... ]
```

`get_all_pairs`라는 메소드를 실행하면 영화 자막 한영 병렬 말뭉치의 모든 pair(text와 쌍을 이루는 영어 문장)를 확인할 수 있습니다.

```
>>> corpus.get_all_pairs()
['Through the snow and sleet and hail, through the blizzard, through the gales, through the wind and through the rain, over mountain, over plain, through the blinding lightning flash, and the mighty thunder crash,', ... ]
```



## 2. 터미널에서 사용하기

파이썬 콘솔 실행 없이 바로 말뭉치를 다운받을 수 있습니다.
다음과 같이 실행하면 됩니다.

```bash
korpora fetch --corpus open_substitles
```

```note
기본적으로 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리에 말뭉치를 내려 받습니다(`~/Korpora`). 다른 경로에 말뭉치를 다운로드 받고 싶다면 
터미널에서 fetch 함수 실행시 `--root_dir custom_path`라는 인자를 추가하세요.
```

```tip
터미널에서 fetch 함수 실행시 `--force_download`라는 인자를 줄 경우 해당 말뭉치가 이미 로컬에 있더라도 이를 무시하고 다시 내려 받습니다.
```