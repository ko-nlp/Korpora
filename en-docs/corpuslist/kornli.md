---
sort: 5
---

# KorNLI

KorNLI is the data created and released by KakaoBrain.
Data specification is as follows:

- author: KakaoBrain
- repository: [https://github.com/kakaobrain/KorNLUDatasets](https://github.com/kakaobrain/KorNLUDatasets)
- references: Ham, J., Choe, Y. J., Park, K., Choi, I., & Soh, H. (2020). [KorNLI and KorSTS: New Benchmark Datasets for Korean Natural Language Understanding.](https://arxiv.org/abs/2004.03289) arXiv preprint arXiv:2004.03289.
- size:
  - multinli_train: 392,702 examples
  - snli_train: 550,152 examples
  - xnli_dev: 2,490 examples
  - xnli_test: 5,010 examples

Data structure is as:

|Attributes|Property|
|---|---|
|text|Sentence|
|pair|Sentence that makes up a pair with the text|
|label|Relation between the text and pair|


## 1. In Python

Execute Python console, download the corpus, and read it.

### Downloading the corpus

You can download KorNLI in the local by the following procedure.

```python
from Korpora import Korpora
Korpora.fetch("kornli")
```

```note
First, download the corpus to Korpora, a directory under the user's local computer root (`~/Korpora`).
If you want to download it in other path, please assign `root_dir=custom_path` when you execute fetch function.
```

```tip
If you assign `force_download=True` when you execute the fetch function, the corpus is downloaded again regardless of its presence in the local. The default is `False`.
```


### 말뭉치 읽어들이기

You can read KorNLI in Python console with the following scheme.
If the corpus is not in the local, the downloading is accompanied.

```python
from Korpora import Korpora
corpus = Korpora.load("kornli")
```

You can read KorNLI as below;
the result is the same as the above operation.

```python
from Korpora import KorNLIKorpus
corpus = KorNLIKorpus()
```

Execute one of the above, and the copus is assigned to the variable `corpus`.
`multinli_train` denotes the multinli_train data of KorNLI, and you can check the first instance as:

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

`snli_train`, `xnli_dev`, and `xnli_test` denote snli_train, xnli_dev, and xnli_test data of KorNLI, respectively, and you can check the first instance as:

```
>>> corpus.snli_train[0]
LabeledSentencePair(text='말을 탄 사람이 고장난 비행기 위로 뛰어오른다.', pair='한 사람이 경쟁을 위해 말을 훈련시키고 있다.', label='neutral')
>>> corpus.xnli_dev[0]
LabeledSentencePair(text='그리고 그가 말했다, "엄마, 저 왔어요."', pair='그는 학교 버스가 그를 내려주자마자 엄마에게 전화를 걸었다.', label='neutral')
>>> corpus.xnli_test[0]
LabeledSentencePair(text='글쎄, 나는 그것에 관해 생각조차 하지 않았지만...', pair='나는 그와 다시 이야기하지 않았다.', label='contradiction')
```


The method `get_all_texts` lets you check all the texts (Sentence) in KorNLI.

```
>>> corpus.get_all_texts()
['개념적으로 크림 스키밍은 제품과 지리라는 두 가지 기본 차원을 가지고 있다.', ... ]
```

The method `get_all_pairs` lets you check all the pairs (Sentence that makes up a pair with the text) in KorNLI.

```
>>> corpus.get_all_pairs()
[SentencePair(text='개념적으로 크림 스키밍은 제품과 지리라는 두 가지 기본 차원을 가지고 있다.', pair='제품과 지리학은 크림 스키밍을 작동시키는 것이다.'), ... ]
```

The method `get_all_labels` lets you check all the labels (Relation between the text and pair) in KorNLI.

```
>>> corpus.get_all_labels()
['neutral', ... ]
```

## 2. In terminal

You can download the corpus without executing Python console.
The command is as below.

```bash
korpora fetch --corpus kornli
```

```note
First, download the corpus to Korpora, a directory under the user's local computer root (`~/Korpora`).
If you want to download it in other path, please assign `--root_dir custom_path` when you execute fetch function in the terminal.
```

```tip
If you assign `--force_download` when you execute fetch function in the terminal, the corpus is downloaded again regardless of its presence in the local.
```
