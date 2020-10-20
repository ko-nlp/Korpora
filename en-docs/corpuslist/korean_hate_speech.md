---
sort: 3
---

# Korean Hate Speech Dataset

Korean Hate Speech Dataset is created by inmoonlight@github, warnikchow@github, and beomi@github.
Data specification is as follows:

- author: inmoonlight@github, warnikchow@github, beomi@github
- repository: https://github.com/kocohub/korean-hate-speech
- size:
  - train: 7,896 examples
  - dev: 471 examples
  - test: 974 examples
  - unlabeled: 2,033,893 examples

Data structure is as:

|Attributes|Property|
|---|---|
|text|Comments|
|title/pair|Title of article|
|gender_bias|Presence of gender-related bias (True/False)|
|bias|Type of bias (gender-related/other/none)|
|hate|Toxicity of hateful expressions (hate/offensive/none)|


## 1. In Python

Execute Python console, download the corpus, and read it.

### Downloading the corpus

You can download the Korean Hate Speech Corpus in the local by the following procedure.

```python
from Korpora import Korpora
Korpora.fetch("korean_hate_speech")
```

```note
First, download the corpus to Korpora, a directory under the user's local computer root (`~/Korpora`). If you want to download it in other path, please assign `root_dir=custom_path` when you execute fetch function.
```

```tip
If you assign `force_download=True` when you execute the fetch function, the corpus is downloaded again regardless of its presence in the local. The default is `False`.
```


### Reading the corpus

You can read the Korean Hate Speech Corpus in Python console with the following scheme.
If the corpus is not in the local, the downloading is accompanied.

```python
from Korpora import Korpora
corpus = Korpora.load("korean_hate_speech")
```

You can read the Korean Hate Speech Corpus as below;
the result is the same as the above operation.

```python
from Korpora import KoreanHateSpeechKorpus
corpus = KoreanHateSpeechKorpus()
```

Execute one of the above, and the copus is assigned to the variable `corpus`.
`train` denotes the train data of Korean Hate Speech Corpus, and you can check the first instance as:

```
>>> corpus.train[0]
KoreanHateSpeechLabeledExample(text='(현재 호텔주인 심정) 아18...', title='"밤새 조문 행렬...', gender_bias='False', bias='others', hate='hate')
>>> corpus.train[0].text
(현재 호텔주인 심정) 아18...(현재 호텔주인 심정) 아18...
>>> corpus.train[0].title
"밤새 조문 행렬...
>>> corpus.train[0].gender_bias
False
>>> corpus.train[0].bias
others
>>> corpus.train[0].hate
hate
```

`dev`, `test`, `unlabeled` denote dev, test, and unlabeled data of Korean Hate Speech Corpus, and you can check the first instance as:

```
>>> korean_hate_speech.dev[0]
KoreanHateSpeechLabeledExample(text='송중기 시대극은 믿고본다...', title='"'아스달 연대기\'...', gender_bias='False', bias='none', hate='none')
>>> korean_hate_speech.test[0]
SentencePair(text='ㅋㅋㅋㅋ 그래도 조아해주는 팬들 많아서 좋겠다 ㅠㅠ 니들은 온유가 안만져줌 ㅠㅠ', pair='"샤이니 온유, 클럽 강제추행 \'무혐의\' 처분 받았다"')
>>> korean_hate_speech.unlabeled[0]
SentencePair(text='"[단독] 지드래곤♥이주연, 제주도 데이트...', pair='"[단독] 지드래곤♥이주연, 제주도 데이트...')
```

The method `get_all_texts` lets you check all the texts (news comments) in Korean Hate Speech Corpus.

```
>>> corpus.get_all_texts()
['송중기 시대극은 믿고본다. 첫회 신선하고 좋았다.', ... ]
```

You can also execute `get_all_texts` for `train`, `dev`, `test`, and `unlabeled` each.

```
>>> corpus.train.get_all_texts()
['(현재 호텔주인 심정) 아18 난 마른하늘에 날벼락맞고 호텔망하게생겼는데 누군 계속 추모받네....', ... ]
>>> corpus.dev.get_all_texts()
['송중기 시대극은 믿고본다. 첫회 신선하고 좋았다.', ... ]
>>> corpus.test.get_all_texts()
['ㅋㅋㅋㅋ 그래도 조아해주는 팬들 많아서 좋겠다 ㅠㅠ 니들은 온유가 안만져줌 ㅠㅠ', ... ]
>>> corpus.unlabeled.get_all_texts()
['"[단독] 지드래곤♥이주연, 제주도 데이트…2018년 1호 커플 탄생"', ... ]
```


## 2. In terminal

You can download the corpus without executing Python console.
The command is as below.

```bash
korpora fetch --corpus korean_hate_speech
```

```note
First, download the corpus to Korpora, a directory under the user's local computer root (`~/Korpora`). If you want to download it in other path, please assign `--root_dir custom_path` when you execute fetch function in the terminal.
```

```tip
If you assign `--force_download` when you execute fetch function in the terminal, the corpus is downloaded again regardless of its presence in the local. 
```
