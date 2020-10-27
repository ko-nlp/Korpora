---
sort: 12
---

# Ko-En Parallel Corpus

Ko-En Parallel Corpus is the data released by jungyeul@github.
Data specification is as follows:

- author: jungyeul@github
- repository: [https://github.com/jungyeul/korean-parallel-corpora](https://github.com/jungyeul/korean-parallel-corpora)
- size:
  - train: 94,123 pairs
  - dev: 1,000 pairs
  - test: 2,000 pairs

Data structure is as:

|Attributes|Property|
|---|---|
|text|Korean sentence|
|pair|English sentence|

## 1. In Python

Execute Python console, download the corpus, and read it.

### Downloading the corpus

You can download the Ko-En Parallel Corpus in the local by the following procedure.

```python
from Korpora import Korpora
Korpora.fetch("korean_parallel_koen_news")
```

```note
First, download the corpus to Korpora, a directory under the user's local computer root (`~/Korpora`).
If you want to download it in other path, please assign `root_dir=custom_path` when you execute fetch function.
```

```tip
If you assign `force_download=True` when you execute the fetch function, the corpus is downloaded again regardless of its presence in the local. The default is `False`.
```


### Reading the corpus

You can read the Ko-En Parallel Corpus in Python console with the following scheme.
If the corpus is not in the local, the downloading is accompanied.

```python
from Korpora import Korpora
corpus = Korpora.load("korean_parallel_koen_news")
```

You can read the Ko-En Parallel Corpus as below;
the result is the same as the above operation.

```python
from Korpora import KoreanParallelKOENNewsKorpus
corpus = KoreanParallelKOENNewsKorpus()
```

Execute one of the above, and the copus is assigned to the variable `corpus`.
`train` denotes the train data of Ko-En Parallel Corpus, and you can check the first instance as:

```
>>> corpus.train[0]
SentencePair(text='개인용 컴퓨터 사용의 상당 부분은 "이것보다 뛰어날 수 있느냐?"', pair='Much of personal computing is about "can you top this?"')
>>> corpus.train[0].text
개인용 컴퓨터 사용의 상당 부분은 "이것보다 뛰어날 수 있느냐?"
>>> corpus.train[0].pair
Much of personal computing is about "can you top this?"
```

`dev`, `test` denote dev and test data of Ko-En Parallel Corpus, and you can check the first instance as:

```
>>> corpus.test[0]
SentencePair(text='토론에 참여한 사람들은 법 집행과 국가 ...', pair='Those involved in the discussions do take seriously ...')
>>> corpus.dev[0]
SentencePair(text='세계 에서 가장 강력한 수퍼컴퓨터를 1년...', pair="After keeping the world's most powerful supercomputer ...")
```

The method `get_all_texts` lets you check all the texts (Korean sentences) in Ko-En Parallel Corpus.

```
>>> corpus.get_all_texts()
['세계 에서 가장 강력한 수퍼컴퓨터를 1년...', ... ]
```

In `corpus.train`, if you execute the method `get_all_texts` and `get_all_pairs` each, you can check all the text (Korean sentenceas) and pair (English sentences) in the train set of Ko-En Parallel Corpus.
This also holds in `corpus.dev` and `corpus.test`.

```
>>> corpus.train.get_all_texts()
['개인용 컴퓨터 사용의 상당 부분은 "이것보다 뛰어날 수 있느냐?"', ... ]
>>> corpus.train.get_all_pairs()
['Much of personal computing is...', ... ]
```


## 2. In terminal

You can download the corpus without executing Python console.
The command is as below.

```bash
korpora fetch --corpus korean_parallel_koen_news
```

```note
First, download the corpus to Korpora, a directory under the user's local computer root (`~/Korpora`).
If you want to download it in other path, please assign `--root_dir custom_path` when you execute fetch function in the terminal.
```

```tip
If you assign `--force_download` when you execute fetch function in the terminal, the corpus is downloaded again regardless of its presence in the local.
```
