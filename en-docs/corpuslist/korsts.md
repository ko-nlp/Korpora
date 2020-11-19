---
sort: 6
---

# KorSTS

KorSTS is the data created and released by KakaoBrain.
Data specification is as follows:

- author: KakaoBrain
- repository: [https://github.com/kakaobrain/KorNLUDatasets](https://github.com/kakaobrain/KorNLUDatasets)
- references: Ham, J., Choe, Y. J., Park, K., Choi, I., & Soh, H. (2020). [KorNLI and KorSTS: New Benchmark Datasets for Korean Natural Language Understanding.](https://arxiv.org/abs/2004.03289) arXiv preprint arXiv:2004.03289.
- size:
  - train: 5,749 examples
  - dev: 1,500 examples
  - test: 1,379 examples

Data structure is as:

|Attributes|Property|
|---|---|
|text|Sentence|
|pair|Sentence that makes up a pair with the text|
|label|Relation between the text and pair|
|Others|Additional information regarding the data|


## 1. In Python

Execute Python console, download the corpus, and read it.

### Downloading the corpus

You can download KorSTS in the local by the following procedure.

```python
from Korpora import Korpora
Korpora.fetch("korsts")
```

```note
First, download the corpus to Korpora, a directory under the user's local computer root (`~/Korpora`).
If you want to download it in other path, please assign `root_dir=custom_path` when you execute fetch function.
```

```tip
If you assign `force_download=True` when you execute the fetch function, the corpus is downloaded again regardless of its presence in the local. The default is `False`.
```


### Reading the corpus

You can read KorSTS in Python console with the following scheme.
If the corpus is not in the local, the downloading is accompanied.

```python
from Korpora import Korpora
corpus = Korpora.load("korsts")
```

You can read KorSTS as below;
the result is the same as the above operation.

```python
from Korpora import KorSTSKorpus
corpus = KorSTSKorpus()
```

Execute one of the above, and the copus is assigned to the variable `corpus`.
`train` denotes the train data of KorSTS, and you can check the first instance as:

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

`dev` and `test` denote dev and test data of KorSTS, respectively, and you can check the first instance as:

```
>>> corpus.dev[0]
# KorSTSExample(text='안전모를 가진 한 남자가 춤을 추고 있다.', pair='안전모를 쓴 한 남자가 춤을 추고 있다.', label=5.0, genre='main-captions', filename='MSRvid', year='2012test')
>>> corpus.test[0]
# KorSTSExample(text='한 소녀가 머리를 스타일링하고 있다.', pair='한 소녀가 머리를 빗고 있다.', label=2.5, genre='main-captions', filename='MSRvid', year='2012test')
```


The method `get_all_texts` lets you check all the texts (Sentence) in KorSTS.

```
>>> corpus.get_all_texts()
['비행기가 이륙하고 있다.', '한 남자가 큰 플루트를 연주하고 있다.', ... ]
```

The method `get_all_pairs` lets you check all the pairs (Sentence that makes up a pair with the text) in KorSTS.

```
>>> corpus.get_all_pairs()
[SentencePair(text='비행기가 이륙하고 있다.', pair='비행기가 이륙하고 있다.'), ... ]
```

The method `get_all_labels` lets you check all the labels (Relation between the text and pair) in KorSTS.

```
>>> corpus.get_all_labels()
['5.000', '3.800', ... ]
```

## 2. In terminal

You can download the corpus without executing Python console.
The command is as below.

```bash
korpora fetch --corpus korsts
```

```note
First, download the corpus to Korpora, a directory under the user's local computer root (`~/Korpora`).
If you want to download it in other path, please assign `--root_dir custom_path` when you execute fetch function in the terminal.
```

```tip
If you assign `--force_download` when you execute fetch function in the terminal, the corpus is downloaded again regardless of its presence in the local.
```
