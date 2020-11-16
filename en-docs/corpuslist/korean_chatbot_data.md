---
sort: 1
---

# Korean Chatbot Data

Korean Chatbot Data is the QA-style chatting data created by songys@github.
Data specification is as follows:

- author: songys@github
- repository: https://github.com/songys/Chatbot_data
- size:
  - train: 11,876 examples

Data structure is as follows:

|Attributes|Property|
|---|---|
|text|Question|
|pair|Answer|
|label|Daily life 0, Farewell (Negative) 1, Love (Positive) 2|


## 1. In Python

Execute Python console, download the corpus, and read it.

### Downloading the corpus

You can download Korean Chatbot Data in the local by the following procedure.

```python
from Korpora import Korpora
Korpora.fetch("korean_chatbot_data")
```

```note
First, download the corpus to Korpora, a directory under the user's local computer root (`~/Korpora`).
If you want to download it in another path, please assign `root_dir=custom_path` when you execute fetch function.
```

```tip
If you assign `force_download=True` when you execute the fetch function, the corpus is downloaded again regardless of its presence in the local. The default is `False`.
```


### Reading the corpus

You can read Korean Chatbot Data in Python console with the following scheme.
If the corpus is not in the local, the downloading is accompanied.

```python
from Korpora import Korpora
corpus = Korpora.load("korean_chatbot_data")
```

You can read Korean Chatbot Data as below;
the result is the same as the above operation.

```python
from Korpora import KoreanChatbotKorpus
corpus = KoreanChatbotKorpus()
```

Execute one of the above, and the copus is assigned to the variable `corpus`.
`train` denotes the train data of Korean Chatbot Data, and you can check the first instance as:

```
>>> corpus.train[0]
LabeledSentencePair(text='12시 땡!', pair='하루가 또 가네요.', label=0)
>>> corpus.train[0].text
12시 땡!
>>> corpus.train[0].pair
하루가 또 가네요.
>>> corpus.train[0].label
0
```

The method `get_all_texts` lets you check all the texts (Question) in Korean Chatbot Data.

```
>>> corpus.get_all_texts()
['12시 땡!', '1지망 학교 떨어졌어', ... ]
```

The method `get_all_pairs` lets you check all the pairs (Answer) in Korean Chatbot Data.

```
>>> corpus.get_all_pairs()
['하루가 또 가네요.', '위로해 드립니다.', ... ]
```

The method `get_all_labels` lets you check all the labels in Korean Chatbot Data.

```
>>> corpus.get_all_labels()
[0, 0, ... ]
```

## 2. In terminal

You can download the corpus without executing Python console.
The command is as below.

```bash
korpora fetch --corpus korean_chatbot_data
```

```note
First, download the corpus to Korpora, a directory under the user's local computer root (`~/Korpora`).
If you want to download it in other path, please assign `--root_dir custom_path` when you execute fetch function in the terminal.
```

```tip
If you assign `--force_download` when you execute fetch function in the terminal, the corpus is downloaded again regardless of its presence in the local.
```
