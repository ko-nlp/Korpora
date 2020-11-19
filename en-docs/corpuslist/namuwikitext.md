---
sort: 8
---

# NamuWikiText

NamuWikiText is a dataset released by lovit@github. It provides Namu Wikipedia in a text format.
Data specification is as follows.

- author: lovit@github
- repository: [https://github.com/lovit/namuwikitext](https://github.com/lovit/namuwikitext)
- size:
  - train: 31,235,096 lines (500,104 docs, 4.6G)
  - dev: 153,605 lines (2,525 docs, 23M)
  - test: 160,233 lines (2,527 docs, 24M)

Data structure is as follows:

|Attributes|Property|
|---|---|
|text|a body of a section|
|pair|a title of a section|


## 1. Using in Python

You can download and load the corpus after executing your Python console.

### Downloading the corpus

You can download NamuWikiText corpus into your local directory with the following Python codes.

```python
from Korpora import Korpora
Korpora.fetch("namuwikitext")
```

```note
By default, the corpus is downloaded to a Korpora directory within the user's root directory (`~/Korpora`). If you wish to download the corpus to another directory,
add `root_dir=custom_path` argument to the fetch method.
```

```tip
When the fetch method is executed with `force_download=True` argument, it ignores the existing corpus in the local directory and re-downloads the corpus. The default value of `force_download` is `False`.
```


### Loading the corpus

You can load NamuWikiText corpus from your Python console with the following codes.
If the corpus does not exist in the local directory, it is also downloaded as well.

```python
from Korpora import Korpora
corpus = Korpora.load("namuwikitext")
```

You can also load the corpus as follows.
The output of these codes is identical to that of previous codes.

```python
from Korpora import NamuwikiTextKorpus
corpus = NamuwikiTextKorpus()
```

If you use either one of these previous examples, you can load the corpus into the variable `corpus`.
`train` refers to the training dataset of the corpus, and you can check its first training instance as follows.

```
>>> corpus.train[0]
SentencePair(text='상위 문서: 아스날 FC\n2009-10 시즌 2011-12 시즌\n2010 -11 시즌...', pair=' = 아스날 FC/2010-11 시즌 =')
>>> corpus.train[0].text
상위 문서: 아스날 FC\n2009-10 시즌 2011-12 시즌\n2010 -11 시즌...
>>> corpus.train[0].pair
= 아스날 FC/2010-11 시즌 =
```

`dev` and `test` refer to the validation and test datasets of the corpus, respectively. Each of their first instance can be accessed as follows.

```
>>> corpus.dev[0]
SentencePair(text='상위 항목: 축구 관련 인물, 외국인 선수/역대 프로축구\n...', pair=' = 소말리아(축구선수) =')
>>> corpus.test[0]
SentencePair(text='', pair=' = 덴덴타운 =')
```

By executing the `get_all_texts` method, you can access all texts (bodies of sections) within the corpus.

```
>>> corpus.get_all_texts()
['상위 문서: 아스날 FC\n2009-10 시즌 2011-12 시즌\n2010 -11 시즌...', ... ]
```

By executing the `get_all_pairs` method, you can access all pairs (titles of sections) within the corpus.

```
>>> corpus.get_all_pairs()
['= 아스날 FC/2010-11 시즌 =', ... ]
```


## 2. Using in a terminal

You can directly download the corpus without executing Python console.
To do so, use the following command.

```bash
korpora fetch --corpus namuwikitext
```

```note
By default, the corpus is downloaded to a Korpora directory within the user's root directory (`~/Korpora`). If you wish to download the corpus to another directory,
add `--root_dir custom_path` argument to the fetch command.
```

```tip
If you add `--force_download` argument when executing the fetch command in the terminal, it ignores the existing corpus in the local directory and re-downloads the corpus.
```