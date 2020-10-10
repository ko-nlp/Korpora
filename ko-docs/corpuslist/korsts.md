---
sort: 5
---

# KorSTS

KorSTS는 카카브레인에서 만들어 공개한 데이터입니다.
데이터 정보는 다음과 같습니다.

- author: KakaoBrain
- repository: [https://github.com/kakaobrain/KorNLUDatasets](https://github.com/kakaobrain/KorNLUDatasets)
- references: Ham, J., Choe, Y. J., Park, K., Choi, I., & Soh, H. (2020). [KorNLI and KorSTS: New Benchmark Datasets for Korean Natural Language Understanding.](https://arxiv.org/abs/2004.03289) arXiv preprint arXiv:2004.03289.
- size:
  - train: 5,749 examples
  - dev: 1,500 examples
  - test: 1,379 examples

데이터 구조는 다음과 같습니다.

|속성명|내용|
|---|---|
|text|문장|
|pair|text와 쌍이 되는 문장|
|label|text, pair 사이의 관계|
|기타|데이터 관련 추가 정보|


## 1. 파이썬에서 사용하기

파이썬 콘솔을 실행한 뒤 말뭉치를 내려받고 읽어들일 수 있습니다.

### 말뭉치 다운로드

KorSTS를 로컬에 내려 받는 파이썬 예제는 다음과 같습니다.

```python
from Korpora import Korpora
Korpora.fetch("korsts")
```

```note
기본적으로 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리에 말뭉치를 내려 받습니다(`~/Korpora`). 다른 경로에 말뭉치를 다운로드 받고 싶다면 
fetch 함수 실행시 `root_dir=custom_path`라는 인자를 추가하세요.
```

```tip
fetch 함수 실행시 `force_download=True`라는 인자를 줄 경우 해당 말뭉치가 이미 로컬에 있더라도 이를 무시하고 다시 내려 받습니다. 기본값은 `False`입니다.
```


### 말뭉치 읽어들이기

KorSTS를 파이썬 콘솔에서 읽어들이는 예제는 다음과 같습니다.
말뭉치가 로컬에 없다면 다운로드도 함께 수행합니다.

```python
from Korpora import Korpora
corpus = Korpora.load("korsts")
```

다음과 같이 실행해도 KorSTS를 읽어들일 수 있습니다.
수행 결과는 위의 코드와 동일합니다.

```python
from Korpora import KorSTSKorpus
corpus = KorSTSKorpus()
```

위 코드 둘 중 하나를 택해 실행하면 `corpus`라는 변수에 말뭉치를 로드합니다.
`train`은 KorSTS의 train 데이터로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
>>> corpus.train[0]
KorSTSExample(text='비행기가 이륙하고 있다.', pair='비행기가 이륙하고 있다.', label=5.0, genre='main-captions', filename='MSRvid', year='2012test')
>>> corpus.train[0].text
비행기가 이륙하고 있다.
>>> corpus.train[0].pair
비행기가 이륙하고 있다.
>>> corpus.train[0].label
5.0
```

`dev`, `test`는 각각 KorSTS의 dev, test 데이터로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
>>> corpus.dev[0]
# KorSTSExample(text='안전모를 가진 한 남자가 춤을 추고 있다.', pair='안전모를 쓴 한 남자가 춤을 추고 있다.', label=5.0, genre='main-captions', filename='MSRvid', year='2012test')
>>> corpus.test[0]
# KorSTSExample(text='한 소녀가 머리를 스타일링하고 있다.', pair='한 소녀가 머리를 빗고 있다.', label=2.5, genre='main-captions', filename='MSRvid', year='2012test')
```


`get_all_texts`라는 메소드를 실행하면 KorNLI의 모든 text(문장)를 확인할 수 있습니다.

```
>>> corpus.get_all_texts()
['비행기가 이륙하고 있다.', '한 남자가 큰 플루트를 연주하고 있다.', ... ]
```

`get_all_pairs`라는 메소드를 실행하면 KorNLI의 모든 pair(text와 쌍이 되는 문장)를 확인할 수 있습니다.

```
>>> corpus.get_all_pairs()
[SentencePair(text='비행기가 이륙하고 있다.', pair='비행기가 이륙하고 있다.'), ... ]
```

`get_all_labels`라는 메소드를 실행하면 KorNLI의 모든 label(text, pair 사이의 관계)을 확인할 수 있습니다.

```
>>> corpus.get_all_labels()
['5.000', '3.800', ... ]
```

## 2. 터미널에서 사용하기

파이썬 콘솔 실행 없이 바로 말뭉치를 다운받을 수 있습니다.
다음과 같이 실행하면 됩니다.

```bash
korpora fetch --corpus korsts
```

```note
기본적으로 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리에 말뭉치를 내려 받습니다(`~/Korpora`). 다른 경로에 말뭉치를 다운로드 받고 싶다면 
터미널에서 fetch 함수 실행시 `--root_dir custom_path`라는 인자를 추가하세요.
```

```tip
터미널에서 fetch 함수 실행시 `--force_download`라는 인자를 줄 경우 해당 말뭉치가 이미 로컬에 있더라도 이를 무시하고 다시 내려 받습니다.
```