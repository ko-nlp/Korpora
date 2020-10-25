---
sort: 2
---

# KcBERT Pre-Training Corpus

KcBERT Pre-Training Corpus is the training data for KcBERT, Korean comments BERT, released by beomi@github.
The data specification is as follows:

- author: beomi@github
- repository: https://github.com/Beomi/KcBERT
- size:
  - train: 86,246,285 examples

## 1. In Python

Execute Python console, download the corpus, and read it.

### Downloading the corpus

You can download KcBERT Pre-Training Corpus in the local by the following procedure.

```python
from Korpora import Korpora
Korpora.fetch("kcbert")
```

```note
First, download the corpus to Korpora, a directory under the user's local computer root (`~/Korpora`). If you want to download it in other path, please assign `root_dir=custom_path` when you execute fetch function.
```

```tip
If you assign `force_download=True` when you execute the fetch function, the corpus is downloaded again regardless of its presence in the local. The default is `False`.
```


### Reading the corpus

You can read KcBERT Pre-Training Corpus in Python console with the following scheme.
If the corpus is not in the local, the downloading is accompanied.

```python
from Korpora import Korpora
corpus = Korpora.load("kcbert")
```

You can read KcBERT Pre-Training Corpus as below;
the result is the same as the above operation.

```python
from Korpora import KcBERTKorpus
corpus = KcBERTKorpus()
```

Execute one of the above, and the copus is assigned to the variable `corpus`.
`train` denotes the train data of KcBERT Pre-Training Corpus, and you can check the first instance as:


```
>>> corpus.train[0]
우리에게 북한은 꼭 없애야 할 적일뿐
```

The method `get_all_texts` lets you check all the texts (news comments) in KcBERT Pre-Training Corpus.

```
>>> corpus.get_all_texts()
```


## 2. In terminal

You can download the corpus without executing Python console.
The command is as below.

```bash
korpora fetch --corpus kcbert
```

```note
First, download the corpus to Korpora, a directory under the user's local computer root (`~/Korpora`). If you want to download it in other path, please assign `--root_dir custom_path` when you execute fetch function in the terminal.
```

```tip
If you assign `--force_download` when you execute fetch function in the terminal, the corpus is downloaded again regardless of its presence in the local.
```
