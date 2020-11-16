---
sort: 7
---

# Korean WikiText

"Korean WikiText" is a wikitext format dataset which consists of only the headers and texts of wikipedia.
The dataset is refined and released by lovit@github.
Data specification is as follows:

- author: lovit@github
- repository: [https://github.com/lovit/kowikitext](https://github.com/lovit/kowikitext)
- size:
  - train : 26794425 lines (877754 articles, 1.7G)
  - dev : 130419 lines (4433 articles, 7.7M)
  - test : 134340 lines (4434 articles, 8.4M)

Data structure is as follows:

|Attributes|Property|
|---|---|
|text|Section body|
|pair|Section title|


## 1. In Python

Execute Python console, download the corpus, and read it.

### Downloading the corpus

You can download Korean WikiText in the local by the following procedure.

```python
from Korpora import Korpora
Korpora.fetch("kowikitext")
```

```note
First, download the corpus to Korpora, a directory under the user's local computer root (`~/Korpora`).
If you want to download it in another path, please assign `root_dir=custom_path` when you execute fetch function.
```

```tip
If you assign `force_download=True` when you execute the fetch function, the corpus is downloaded again regardless of its presence in the local. The default is `False`.
```


### Reading the corpus

You can read Korean WikiText in Python console with the following scheme.
If the corpus is not in the local, the downloading is accompanied.

```python
from Korpora import Korpora
corpus = Korpora.load("kowikitext")
```

You can read Korean WikiText as below;
the result is the same as the above operation.

```python
from Korpora import KowikiTextKorpus
corpus = KowikiTextKorpus()
```

Execute one of the above, and the copus is assigned to the variable `corpus`.
`train` denotes the train data of Korean WikiText, and you can check the first instance as:

```
>>> corpus.train[0]
SentencePair(text='외교부장\n외교부장', pair=' = 분류:중화인민공화국의 외교부장 =')
>>> corpus.train[0].text
'외교부장\n외교부장'
>>> corpus.train[0].pair
= 분류:중화인민공화국의 외교부장 =
```

`dev` and `test` denote dev and test data of Korean WikiText, respectively, and you can check the first instance as:

```
>>> corpus.dev[0]
SentencePair(text='스폴리아텔레(, )는 이탈리아의 후식으로서 ...', pair=' = 스폴리아텔레 =')
>>> corpus.test[0]
SentencePair(text='기타', pair=' = 분류:러시아의 기타 연주자 =')
```

The method `get_all_texts` lets you check all the texts (Section body) in Korean WikiText.

```
>>> corpus.get_all_texts()
['외교부장\n외교부장', ... ]
```

The method `get_all_pairs` lets you check all the pairs (Section title) in Korean WikiText.

```
>>> corpus.get_all_pairs()
['= 분류:중화인민공화국의 외교부장 =', ... ]
```


## 2. In terminal

You can download the corpus without executing Python console.
The command is as below.

```bash
korpora fetch --corpus kowikitext
```

```note
First, download the corpus to Korpora, a directory under the user's local computer root (`~/Korpora`).
If you want to download it in other path, please assign `--root_dir custom_path` when you execute fetch function in the terminal.
```

```tip
If you assign `--force_download` when you execute fetch function in the terminal, the corpus is downloaded again regardless of its presence in the local.
```
