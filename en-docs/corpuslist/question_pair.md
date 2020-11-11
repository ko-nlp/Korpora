---
sort: 11
---

# Korean Question Pair

Korean Paired Question v.2 is a dataset released by songys@github.
Data specification is as follows.

- author: songys@github
- repository: [https://github.com/songys/Question_pair](https://github.com/songys/Question_pair)
- size:
  - train: 6,888 examples
  - test: 688 examples

Data structure is as follows:

|Attributes|Property|
|---|---|
|text|a sentence|
|pair|another sentence that is paired with the text|
|label|if a text and its pair refer to an identical question, the label is 0. If they are different, it is 1.|

## 1. Using in Python

You can download and load the corpus after executing your Python console.

### Downloading the corpus

You can download the Korean Pair Question corpus into your local directory with the following Python codes.

```python
from Korpora import Korpora
Korpora.fetch("question_pair")
```

```note
By default, the corpus is downloaded to a Korpora directory within the user's root directory (`~/Korpora`). If you wish to download the corpus to another directory,
add `root_dir=custom_path` argument to the fetch method.
```

```tip
When the fetch method is executed with `force_download=True` argument, it ignores the existing corpus in the local directory and re-downloads the corpus. The default value of `force_download` is `False`.
```


### Loading the corpus

You can load the Korean Pair Question corpus from your Python console with the following codes.
If the corpus does not exist in the local directory, it is also downloaded as well.

```python
from Korpora import Korpora
corpus = Korpora.load("question_pair")
```

You can also load the corpus as follows.
The output of these codes is identical to that of previous codes.

```python
from Korpora import QuestionPairKorpus
corpus = QuestionPairKorpus()
```

If you use either one of these previous examples, you can load the corpus into the variable `corpus`.
`train` refers to the training dataset of the Korean Paired Question, and you can check its first training instance as follows.

```
>>> corpus.train[0]
LabeledSentencePair(text='1000일 만난 여자친구와 이별', pair='10년 연예의끝', label='1')
>>> corpus.train[0].text
1000일 만난 여자친구와 이별
>>> corpus.train[0].pair
10년 연예의끝
>>> corpus.train[0].label
1
```

`test` refers to the test dataset of the Korean Paired Question, and you can check its first test instance as follows.

```
>>> corpus.test[0]
LabeledSentencePair(text='21살의 사랑에 대해', pair='사랑을 노력한다는게 말이 되나요?', label='1')
```

By executing the `get_all_texts` method, you can access all texts (sentences) within the Korean Paired Question corpus.

```
>>> corpus.get_all_texts()
['1000일 만난 여자친구와 이별', ... ]
```

By executing the `get_all_pairs` method, you can access all pairs (sentences that are paired with the texts) within the Korean Paired Question corpus.

```
>>> corpus.get_all_pairs()
[SentencePair(text='1000일 만난 여자친구와 이별', pair='10년 연예의끝'), ... ]
```

By executing the `get_all_labels` method, you can check all labels (if a text and a pair refer to a same question, it is 0. Otherwise, 1) within the Korean paired Question corpus.

```
>>> corpus.get_all_labels()
['1', ... ]
```


## 2. Using in a terminal

You can directly download the corpus without executing Python console.
To do so, use the following command.

```bash
korpora fetch --corpus question_pair
```

```note
By default, the corpus is downloaded to a Korpora directory within the user's root directory (`~/Korpora`). If you wish to download the corpus to another directory,
add `--root_dir custom_path` argument to the fetch command.
```

```tip
If you add `--force_download` argument when executing the fetch command in the terminal, it ignores the existing corpus in the local directory and re-downloads the corpus.
```