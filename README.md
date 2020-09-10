# Korpora: Korean Corpora Archives

Korpora 는 다른 분들이 연구 목적으로 공유해주신 말뭉치들을 손쉽게 다운로드, 사용할 수 있는 기능만을 제공합니다.

말뭉치들을 공유해 주신 분들에게 감사드리며, 각 말뭉치 별 설명과 라이센스는 말뭉치 별 클래스에 기술하였습니다.
말뭉치마다 데이터를 로딩할 때 설명과 라이센스가 화면에 출력됩니다.
해당 말뭉치에 대해 자세히 알고 싶으신 분은 출력되는 description 을 참고하세요
해당 말뭉치를 연구/상용의 목적으로 이용하실 때에는 아래의 라이센스를 참고해 주시기 바랍니다.

This package provides easy-download and easy-usage for various Korean corpora

## Install

From source

```
git clone https://github.com/ko-nlp/Korpora
python setup.py install
```

Using pip

```
pip install Korpora
```

## Usage

### 청와대 국민청원 (2017.08 ~ 2019.03)
- author: lovit@github
- repository:  https://github.com/lovit/petitions_archive
- size:
  - train: 433,631 examples

```python
from Korpora import KoreanPetitions

petitions = KoreanPetitions()  # or
petitions = Korpora.load('korean_petitions')

len(petitions.train)
petitions.train[0]
# KoreanPetition(text="안녕하세요. 현재 사대, ...", category='육아/교육', num_agree=88, begin='2017-08-25', end='2017-09-24', title='학교는 ...')

petitions.train[0].text
# 안녕하세요. 현재 사대, ...

for petition in petitions.train:
    category = petition.category
    # do something
```

### KorNLI
- author: KakaoBrain
- repository: https://github.com/kakaobrain/KorNLUDatasets
- references: Ham, J., Choe, Y. J., Park, K., Choi, I., & Soh, H. (2020). [KorNLI and KorSTS: New Benchmark Datasets for Korean Natural Language Understanding.](https://arxiv.org/abs/2004.03289) arXiv preprint arXiv:2004.03289.
- size:
  - multinli_train: 392,702 examples
  - snli_train: 550,152 examples
  - xnli_dev: 2,490 examples
  - xnli_test: 5,010 examples

```python
from Korpora import KorNLI

kornli = KorNLI() # or
kornli = Korpora.load('kornli')

nsmc.snli_train[0]
# LabeledSentencePair(text='말을 탄 사람이 고장난 비행기 위로 뛰어오른다.', pair='한 사람이 경쟁을 위해 말을 훈련시키고 있다.', label='neutral')
```

### KorSTS
- author: KakaoBrain
- repository: https://github.com/kakaobrain/KorNLUDatasets
- references: Ham, J., Choe, Y. J., Park, K., Choi, I., & Soh, H. (2020). [KorNLI and KorSTS: New Benchmark Datasets for Korean Natural Language Understanding.](https://arxiv.org/abs/2004.03289) arXiv preprint arXiv:2004.03289.
- size:
  - train: 5,749 examples
  - dev: 1,500 examples
  - test: 1,379 examples

```python
from Korpora import KorSTS

korsts = KorSTS() # or
korsts = Korpora.load('korsts')
korsts.train[0]
# KorSTSExample(text='비행기가 이륙하고 있다.', pair='비행기가 이륙하고 있다.', label=5.0, genre='main-captions', filename='MSRvid', year='2012test')
```

### 나무위키텍스트
- author: lovit@github
- repository: https://github.com/lovit/namuwikitext
- size:
  - train: 38,278,040 lines (500,104 docs, 5.3G)
  - dev: 197,723 lines (2,525 docs, 28M)
  - test: 193,614 lines (2,525 docs, 29M)

```python
from Korpora import NamuwikiTextKorpus

namuwiki = NamuwikiTextKorpus() # or
namuwiki = Korpora.load('namuwikitext')

namuwiki.dev[0]
# SentencePair(text='상위 문서: 아스날 FC\n2009-10 시즌 2011-12 시즌\n2010 -11 시즌...', pair=' = 아스날 FC/2010-11 시즌 =')
```

### Naver sentiment movie corpus v1.0
- author: e9t@github
- repository: https://github.com/e9t/nsmc
- references: www.lucypark.kr/docs/2015-pyconkr/#39
- size:
  - train: 150,000 examples
  - test: 50,000 examples

```python
from Korpora import NSMC

nsmc = NSMC() # or
nsmc = Korpora.load('nsmc')

nsmc.train[0]
# LabeledSentence(text='아 더빙.. 진짜 짜증나네요 목소리', label=0)
```

### 챗봇 트레이닝용 문답 페어
- author: songys@github
- repository: https://github.com/songys/Chatbot_data
- size:
  - train: 11,876 examples

```python
from Korpora import KoreanChatbotKorpus

chatbot_corpus = KoreanChatbotKorpus() # or
chatbot_corpus = Korpora.load('korean_chatbot_data')

chatbot_corpus.train[0]
# LabeledSentencePair(text='12시 땡!', pair='하루가 또 가네요.', label=0)
```

### 질문쌍 (Paired Question v.2)
- author: songys@github
- repository: https://github.com/songys/Question_pair
- size:
  - train: 6,888 examples
  - test: 688 examples

```python
from Korpora import QuestionPairKorpus


question_pair = QuestionPairKorpus() # or
question_pair = Korpora.load('question_pair')

question_pair.train[0]
# LabeledSentencePair(text='1000일 만난 여자친구와 이별', pair='10년 연예의끝', label='1')
```

### 네이버, 창원대가 함께하는 NLP Challenge (NER)
- author: 네이버 + 창원대
- repository: https://github.com/naver/nlp-challenge/tree/master/missions/ner
- reference: http://air.changwon.ac.kr/?page_id=10
- size:
  - train: 90,000 examples

```python
from Korpora import NaverChangwonNERKorpus

ner = NaverChangwonNERKorpus()
ner = Korpora.load('naver_changwon_ner')

ner.train[0]
# WordTag(text='비토리오 양일 만에 영사관 감호 용퇴, 항룡 압력설 의심만 가율 ', words=['비토리오', '양일', '만에', '영사관', '감호', '용퇴,', '항룡', '압력설', '의심만', '가율'], tags=['PER_B', 'DAT_B', '-', 'ORG_B', 'CVL_B', '-', '-', '-', '-', '-'])
```


## Contribution

[Code / Commit / Branch convention]: https://github.com/ko-nlp/Korpora/issues/27

### Naming rules

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
