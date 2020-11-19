---
sort: 10
---

# NAVER Sentiment Movie Corpus

NAVER Sentiment Movie Corpus(NSMC) is a movie review dataset released by e9t@github.
Data specification is as follows.

- author: e9t@github
- repository: https://github.com/e9t/nsmc
- references: www.lucypark.kr/docs/2015-pyconkr/#39
- size:
  - train: 150,000 examples
  - test: 50,000 examples

Data structure is as follows:

|Attributes|Properties|
|---|---|
|text|movie review comments|
|label|sentiment labels on the movie (positive 1, negative 0)|

## 1. Using in Python

You can download and load the corpus after executing your Python console.

### Downloading the corpus

You can download NSMC into your local directory with the following Python codes.

```python
from Korpora import Korpora
Korpora.fetch("nsmc")
```

```note
By default, the corpus is downloaded to a Korpora directory within the user's root directory (`~/Korpora`). If you wish to download the corpus to another directory,
add `root_dir=custom_path` argument to the fetch method.
```

```tip
When the fetch method is executed with `force_download=True` argument, it ignores the existing corpus in the local directory and re-downloads the corpus. The default value of `force_download` is `False`.
```


### Loading the corpus

You can load NSMC from your Python console with the following codes.
If the corpus does not exist in the local directory, it is also downloaded as well.

```python
from Korpora import Korpora
corpus = Korpora.load("nsmc")
```

You can also load the corpus as follows.
The output of these codes is identical to that of previous codes.

```python
from Korpora import NSMCKorpus
corpus = NSMCKorpus()
```

If you use either one of these previous examples, you can load the corpus into the variable `corpus`.
`train` refers to the training dataset of NSMC, and you can check its first training instance as follows.

```
>>> corpus.train[0]
LabeledSentence(text='아 더빙.. 진짜 짜증나네요 목소리', label=0)
>>> corpus.train[0].text
아 더빙.. 진짜 짜증나네요 목소리
>>> corpus.train[0].label
0
```

By executing the `get_all_texts` method, you can access all texts (movie review comments) within NSMC.

```
>>> corpus.get_all_texts()
['아 더빙.. 진짜 짜증나네요 목소리', ... ]
```

By executing the `get_all_labels` method, you can access all labels (either positive or negative) within NSMC.

```
>>> corpus.get_all_labels()
[0, ... ]
```



## 2. Using in a terminal

You can directly download the corpus without executing Python console.
To do so, use the following command.

```bash
korpora fetch --corpus nsmc
```

```note
By default, the corpus is downloaded to a Korpora directory within the user's root directory (`~/Korpora`). If you wish to download the corpus to another directory,
add `--root_dir custom_path` argument to the fetch command.
```

```tip
If you add `--force_download` argument when executing the fetch command in the terminal, it ignores the existing corpus in the local directory and re-downloads the corpus.
```