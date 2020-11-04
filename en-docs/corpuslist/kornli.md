---
sort: 5
---

# KorNLI

KorNLI는 카카브레인에서 만들어 공개한 데이터입니다.
데이터 정보는 다음과 같습니다.

- author: KakaoBrain
- repository: [https://github.com/kakaobrain/KorNLUDatasets](https://github.com/kakaobrain/KorNLUDatasets)
- references: Ham, J., Choe, Y. J., Park, K., Choi, I., & Soh, H. (2020). [KorNLI and KorSTS: New Benchmark Datasets for Korean Natural Language Understanding.](https://arxiv.org/abs/2004.03289) arXiv preprint arXiv:2004.03289.
- size:
  - multinli_train: 392,702 examples
  - snli_train: 550,152 examples
  - xnli_dev: 2,490 examples
  - xnli_test: 5,010 examples

데이터 구조는 다음과 같습니다.

|속성명|내용|
|---|---|
|text|문장|
|pair|text와 쌍이 되는 문장|
|label|text, pair 사이의 관계|


## 1. 파이썬에서 사용하기

파이썬 콘솔을 실행한 뒤 말뭉치를 내려받고 읽어들일 수 있습니다.

### 말뭉치 다운로드

KorNLI를 로컬에 내려 받는 파이썬 예제는 다음과 같습니다.

```python
from Korpora import Korpora
Korpora.fetch("kornli")
```

```note
기본적으로 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리에 말뭉치를 내려 받습니다(`~/Korpora`). 다른 경로에 말뭉치를 다운로드 받고 싶다면 
fetch 함수 실행시 `root_dir=custom_path`라는 인자를 추가하세요.
```

```tip
fetch 함수 실행시 `force_download=True`라는 인자를 줄 경우 해당 말뭉치가 이미 로컬에 있더라도 이를 무시하고 다시 내려 받습니다. 기본값은 `False`입니다.
```


### 말뭉치 읽어들이기

KorNLI를 파이썬 콘솔에서 읽어들이는 예제는 다음과 같습니다.
말뭉치가 로컬에 없다면 다운로드도 함께 수행합니다.

```python
from Korpora import Korpora
corpus = Korpora.load("kornli")
```

다음과 같이 실행해도 KorNLI를 읽어들일 수 있습니다.
수행 결과는 위의 코드와 동일합니다.

```python
from Korpora import KorNLIKorpus
corpus = KorNLIKorpus()
```

위 코드 둘 중 하나를 택해 실행하면 `corpus`라는 변수에 말뭉치를 로드합니다.
`multinli_train`은 KorNLI의 multinli_train 데이터로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
>>> corpus.multinli_train[0]
LabeledSentencePair(text='개념적으로 크림 스키밍은 제품과 지리라는 두 가지 기본 차원을 가지고 있다.', pair='제품과 지리학은 크림 스키밍을 작동시키는 것이다.', label='neutral')
>>> corpus.multinli_train[0].text
개념적으로 크림 스키밍은 제품과 지리라는 두 가지 기본 차원을 가지고 있다.
>>> corpus.multinli_train[0].pair
제품과 지리학은 크림 스키밍을 작동시키는 것이다.
>>> corpus.multinli_train[0].label
neutral
```

`snli_train`, `xnli_dev`, `xnli_test`는 각각 KorNLI의 snli_train, xnli_dev, xnli_test 데이터로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
>>> corpus.snli_train[0]
LabeledSentencePair(text='말을 탄 사람이 고장난 비행기 위로 뛰어오른다.', pair='한 사람이 경쟁을 위해 말을 훈련시키고 있다.', label='neutral')
>>> corpus.xnli_dev[0]
LabeledSentencePair(text='그리고 그가 말했다, "엄마, 저 왔어요."', pair='그는 학교 버스가 그를 내려주자마자 엄마에게 전화를 걸었다.', label='neutral')
>>> corpus.xnli_test[0]
LabeledSentencePair(text='글쎄, 나는 그것에 관해 생각조차 하지 않았지만...', pair='나는 그와 다시 이야기하지 않았다.', label='contradiction')
```


`get_all_texts`라는 메소드를 실행하면 KorNLI의 모든 text(문장)를 확인할 수 있습니다.

```
>>> corpus.get_all_texts()
['개념적으로 크림 스키밍은 제품과 지리라는 두 가지 기본 차원을 가지고 있다.', ... ]
```

`get_all_pairs`라는 메소드를 실행하면 KorNLI의 모든 pair(text와 쌍이 되는 문장)를 확인할 수 있습니다.

```
>>> corpus.get_all_pairs()
[SentencePair(text='개념적으로 크림 스키밍은 제품과 지리라는 두 가지 기본 차원을 가지고 있다.', pair='제품과 지리학은 크림 스키밍을 작동시키는 것이다.'), ... ]
```

`get_all_labels`라는 메소드를 실행하면 KorNLI의 모든 label(text, pair 사이의 관계)을 확인할 수 있습니다.

```
>>> corpus.get_all_labels()
['neutral', ... ]
```

## 2. 터미널에서 사용하기

파이썬 콘솔 실행 없이 바로 말뭉치를 다운받을 수 있습니다.
다음과 같이 실행하면 됩니다.

```bash
korpora fetch --corpus kornli
```

```note
기본적으로 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리에 말뭉치를 내려 받습니다(`~/Korpora`). 다른 경로에 말뭉치를 다운로드 받고 싶다면 
터미널에서 fetch 함수 실행시 `--root_dir custom_path`라는 인자를 추가하세요.
```

```tip
터미널에서 fetch 함수 실행시 `--force_download`라는 인자를 줄 경우 해당 말뭉치가 이미 로컬에 있더라도 이를 무시하고 다시 내려 받습니다.
```
