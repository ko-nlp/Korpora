# Korpora: Korean Corpora Archives

This package provides easy-download and easy-usage for various Korean corpora

## Install

From source

```
git clone https://github.com/lovit/Korpora
python setup.py install
```

Using pip

```
pip install Korpora
```

## Usage

```python
from Korpora import Korpora

nsmc = Korpora.load('nsmc')
# nsmc = Korpora.load('nsmc', root_dir='path/to/Korpora')
# nsmc = Korpora.load('nsmc', root_dir='path/to/Korpora', force_download=True)
len(nsmc.train.texts)   # 150000
len(nsmc.train.labels)  # 50000
```

```python
from Korpora import NSMC

nsmc = NSMC()
nsmc = NSMC(root_dir='./Korpora/')
nsmc = NSMC(force_download=True)
```

## Naming

All corpus follows `corpus_name.mode.type`
- mode: one of [train, dev, test, all]
- type: one of [texts, labels, ...]
- normalization: one of [normed, raw]
- tokenization: one of [.bpe, .mecab, ...]

```python
nsmc.train.texts
```

File structure `Korpora/corpus_name/mode.type[.normalization][.tokenization]`.

```
Korpora/nsmc/rating_train.txt
Korpora/nsmc/rating_train.txt.texts
Korpora/nsmc/train.texts.raw
Korpora/nsmc/train.texts.normed
Korpora/nsmc/train.labels
Korpora/nsmc/train.texts.normed.mecab
Korpora/nsmc/test.texts.normed.mecab
```