---
sort: 4
---

# Korean Petitions

Korean Petitions is the data collected from the Blue House National Petition (2017.08 ~ 2019.03), released by lovit@github.
Data specification is as follows:

- author: lovit@github
- repository: https://github.com/lovit/petitions_archive
- size:
  - train: 433,631 examples

Data structure is as:

|Attributes|Property|
|---|---|
|text|Content of petition|
|category|Category of petition|
|num_agree|Number of agreements|
|begin|Date petition began|
|end|Date petition ended|
|title|Title of petition|

## 1. In Python

Execute Python console, download the corpus, and read it.

### Downloading the corpus

You can download the Korean Petitions in the local by the following procedure.

```python
from Korpora import Korpora
Korpora.fetch("korean_petitions")
```

```note
First, download the corpus to Korpora, a directory under the user's local computer root (`~/Korpora`).
If you want to download it in other path, please assign `root_dir=custom_path` when you execute fetch function.
```

```tip
If you assign `force_download=True` when you execute the fetch function, the corpus is downloaded again regardless of its presence in the local. The default is `False`.
```


### Reading the corpus

You can read the Korean Petitions in Python console with the following scheme.
If the corpus is not in the local, the downloading is accompanied.

```python
from Korpora import Korpora
corpus = Korpora.load("korean_petitions")
```

You can read the Korean Petitions as below;
the result is the same as the above operation.

```python
from Korpora import KoreanPetitionsKorpus
corpus = KoreanPetitionsKorpus()
```

Execute one of the above, and the copus is assigned to the variable `corpus`.
`train` denotes the train data of Korean Petitions, and you can check the first instance as:

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

The method `get_all_texts` lets you check all the texts (Content of petition) in Korean Petitions.
The method `get_all_categories` lets you check all the categories (Category of petition) in Korean Petitions.
The method `get_all_num_agrees` lets you check all the num_agree (Number of agreements) in Korean Petitions.
The method `get_all_titles` lets you check all the titles (Title of petition) in Korean Petitions.

## 2. In terminal 

You can download the corpus without executing Python console.
The command is as below.

```bash
korpora fetch --corpus korean_petitions
```

```note
First, download the corpus to Korpora, a directory under the user's local computer root (`~/Korpora`).
If you want to download it in other path, please assign `--root_dir custom_path` when you execute fetch function in the terminal.
```

```tip
If you assign `--force_download` when you execute fetch function in the terminal, the corpus is downloaded again regardless of its presence in the local.
```

