---
sort: 21
---

# OpenSubtitles2016

OpenSubtitles2016 is a dataset released by TRAC.
Data specification is as follows.

- author: TRAC ([https://trac.edgewall.org](https://trac.edgewall.org))
- repository: [http://opus.nlpl.eu/OpenSubtitles-v2018.php](http://opus.nlpl.eu/OpenSubtitles-v2018.php)
- references: P. Lison and J. Tiedemann, 2016, OpenSubtitles2016: Extracting Large Parallel Corpora from Movie and TV Subtitles. In Proceedings of the 10th International Conference on Language Resources and Evaluation (LREC 2016)
- size:
  - train: 1,269,683 pairs

Data structure is as follows:

|Attributes|Property|
|---|---|
|text|a Korean sentence|
|pair|an English sentence that is paired with the text|


## 1. Using in Python

You can download and load the corpus after executing your Python console.

### Downloading the corpus

You can download the OpenSubtitles2016 corpus into your local directory with the following Python codes.

```python
from Korpora import Korpora
Korpora.fetch("open_substitles")
```

```note
By default, the corpus is downloaded to a Korpora directory within the user's root directory (`~/Korpora`). If you wish to download the corpus to another directory,
add `root_dir=custom_path` argument to the fetch method.
```

```tip
When the fetch method is executed with `force_download=True` argument, it ignores the existing corpus in the local directory and re-downloads the corpus. The default value of `force_download` is `False`.
```


### Loading the corpus

You can load the OpenSubtitles2016 corpus from your Python console with the following codes.
If the corpus does not exist in the local directory, it is also downloaded as well.

```python
from Korpora import Korpora
corpus = Korpora.load("open_substitles")
```

You can also load the corpus as follows.
The output of these codes is identical to that of previous codes.

```python
from Korpora import OpenSubstitleKorpus
corpus = OpenSubstitleKorpus()
```

If you use either one of these previous examples, you can load the corpus into the variable `corpus`.
`train` refers to the training dataset of the OpenSubtitles2016 corpus, and you can check its first training instance as follows.

```
>>> corpus.train[0]
SentencePair(text='폭설이 내리고 우박, 진눈깨비가 퍼부어도 눈보라가 몰아쳐도 강풍이 불고 비바람이 휘몰아쳐도', pair='Through the snow and sleet and hail, through the blizzard, through the gales, through the wind and through the rain, over mountain, over plain, through the blinding lightning flash, and the mighty thunder crash,')
>>> corpus.train[0].text
폭설이 내리고 우박, 진눈깨비가 퍼부어도 눈보라가 몰아쳐도 강풍이 불고 비바람이 휘몰아쳐도
>>> corpus.train[0].pair
Through the snow and sleet and hail, through the blizzard, through the gales, through the wind and through the rain, over mountain, over plain, through the blinding lightning flash, and the mighty thunder crash,
```

By executing the `get_all_texts` method, you can access all texts (Korean sentences) within the OpenSubtitles2016 corpus.

```
>>> corpus.get_all_texts()
['폭설이 내리고 우박, 진눈깨비가 퍼부어도 눈보라가 몰아쳐도 강풍이 불고 비바람이 휘몰아쳐도', ... ]
```

By executing the `get_all_pairs` method, you can access all pairs (English sentences that are paired with the texts) within the corpus.

```
>>> corpus.get_all_pairs()
['Through the snow and sleet and hail, through the blizzard, through the gales, through the wind and through the rain, over mountain, over plain, through the blinding lightning flash, and the mighty thunder crash,', ... ]
```



## 2. Using in a terminal

You can directly download the corpus wWithout executing Python console.
To do so, use the following command.

```bash
korpora fetch --corpus open_substitles
```

```note
By default, the corpus is downloaded to a Korpora directory within the user's root directory (`~/Korpora`). If you wish to download the corpus to another directory,
add `--root_dir custom_path` argument to the fetch command.
```

```tip
If you add `--force_download` argument when executing the fetch command in the terminal, it ignores the existing corpus in the local directory and re-downloads the corpus.
```