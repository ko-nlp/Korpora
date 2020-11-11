---
sort: 9
---

# NAVER x Changwon NER

NAVER x Changwon NER is a dataset released by lovit@github. It provides the Korean Wikipedia in a text format.
Data specification is as follows.

- author: Naver + Changwon National University
- repository: [https://github.com/naver/nlp-challenge/tree/master/missions/ner](https://github.com/naver/nlp-challenge/tree/master/missions/ner)
- reference: [http://air.changwon.ac.kr/?page_id=10](http://air.changwon.ac.kr/?page_id=10)
- size:
  - train: 90,000 examples

Data structure is as follows:

|Attributes|Property|
|---|---|
|text|a string of space delimited words|
|words|a word sequence|
|tags|a sequence of entity tags of words|


## 1. Using in Python

You can download and load the corpus after executing your Python console.

### Downloading the corpus

You can download NAVER x Changwon NER corpus into your local directory with the following Python codes.

```python
from Korpora import Korpora
Korpora.fetch("naver_changwon_ner")
```

```note
By default, the corpus is downloaded to a Korpora directory within the user's root directory (`~/Korpora`). If you wish to download the corpus to another directory,
add `root_dir=custom_path` argument to the fetch method.
```

```tip
When the fetch method is executed with `force_download=True` argument, it ignores the existing corpus in the local directory and re-downloads the corpus. The default value of `force_download` is `False`.
```


### Loading the corpus

You can load NAVER x Changwon NER corpus from your Python console with the following codes.
If the corpus does not exist in the local directory, it is also downloaded as well.

```python
from Korpora import Korpora
corpus = Korpora.load("naver_changwon_ner")
```

You can also load the corpus as follows.
The output of these codes is identical to that of previous codes.

```python
from Korpora import NaverChangwonNERKorpus
corpus = NaverChangwonNERKorpus()
```

If you use either one of these previous examples, you can load the corpus into the variable `corpus`.
`train` refers to the training dataset of NAVER x Changwon NER corpus, and you can check its first training instance as follows.

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

By executing the `get_all_words` method, you can access all words (word sequences) within NAVER x Changwon NER corpus.

```
>>> corpus.get_all_words()
[['비토리오', '양일', '만에', '영사관', '감호', '용퇴,', '항룡', '압력설', '의심만', '가율'], ... ]
```

By executing the `get_all_tags` method, you can access all tags (a sequence of entity tags of words) within the corpus.

```
>>> corpus.get_all_tags()
[['PER_B', 'DAT_B', '-', 'ORG_B', 'CVL_B', '-', '-', '-', '-', '-'], ... ]
```

By executing the `get_all_texts` method, you can access all texts (a string of space delimited words) within the corpus.

```
>>> corpus.get_all_texts()
['비토리오 양일 만에 영사관 감호 용퇴, 항룡 압력설 의심만 가율 ', ... ]
```



## 2. Using in a terminal

You can directly download the corpus without executing Python console.
To do so, use the following command.

```bash
korpora fetch --corpus naver_changwon_ner
```

```note
By default, the corpus is downloaded to a Korpora directory within the user's root directory (`~/Korpora`). If you wish to download the corpus to another directory,
add `--root_dir custom_path` argument to the fetch command.
```

```tip
If you add `--force_download` argument when executing the fetch command in the terminal, it ignores the existing corpus in the local directory and re-downloads the corpus.
```