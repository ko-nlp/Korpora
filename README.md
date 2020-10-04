# Korpora: Korean Corpora Archives

Korpora 는 다른 분들이 연구 목적으로 공유해주신 말뭉치들을 손쉽게 다운로드, 사용할 수 있는 기능만을 제공합니다.

말뭉치들을 공유해 주신 분들에게 감사드리며, 각 말뭉치 별 설명과 라이센스는 말뭉치 별 클래스에 기술하였습니다.
말뭉치마다 데이터를 로딩할 때 설명과 라이센스가 화면에 출력됩니다.
해당 말뭉치에 대해 자세히 알고 싶으신 분은 출력되는 description 을 참고하세요.
해당 말뭉치를 연구/상용의 목적으로 이용하실 때에는 아래의 라이센스를 참고해 주시기 바랍니다.

This package provides easy-download and easy-usage for various Korean corpora.

## Page

본 페이지는 [jekyll-rtd-theme](https://github.com/rundocs/jekyll-rtd-theme)을 기반으로 만들었습니다.
진심으로 감사드립니다.

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

## Corpus List

- Korpora 패키지가 제공하는 말뭉치 목록은 다음과 같습니다.

|corpus_name|description|link|
|---|---|---|
|korean_chatbot_data|챗봇 트레이닝용 문답 페어|https://github.com/songys/Chatbot_data|
|kcbert|KcBERT 모델 학습용 댓글 데이터|https://github.com/Beomi/KcBERT|
|korean_hate_speech|한국어 혐오 데이터셋|https://github.com/kocohub/korean-hate-speech|
|korean_petitions|청와대 국민 청원|https://github.com/lovit/petitions_archive|
|kornli|Korean NLI|https://github.com/kakaobrain/KorNLUDatasets|
|korsts|Korean STS|https://github.com/kakaobrain/KorNLUDatasets|
|namuwikitext|나무위키 텍스트|https://github.com/lovit/namuwikitext|
|naver_changwon_ner|네이버 x 창원대 개체명 인식 데이터셋|https://github.com/naver/nlp-challenge/tree/master/missions/ner|
|nsmc|NAVER Sentiment Movie Corpus|https://github.com/e9t/nsmc|
|question_pair|한국어 질문쌍 데이터셋|https://github.com/songys/Question_pair|

- Korpora 패키지가 제공하는 말뭉치 목록을 확인하는 파이썬 예제는 다음과 같습니다.

```python
from Korpora import Korpora

Korpora.corpus_list()
```

```
{'kcbert': 'beomi@github 님이 만드신 KcBERT 학습데이터',
 'korean_chatbot_data': 'songys@github 님이 만드신 챗봇 문답 데이터',
 'korean_hate_speech': '{inmoonlight,warnikchow,beomi}@github 님이 만드신 혐오댓글데이터',
 'korean_petitions': 'lovit@github 님이 만드신 2017.08 ~ 2019.03 청와대 청원데이터',
 'kornli': 'KakaoBrain 에서 제공하는 Natural Language Inference (NLI) 데이터',
 'korsts': 'KakaoBrain 에서 제공하는 Semantic Textual Similarity (STS) 데이터',
 'namuwikitext': 'lovit@github 님이 만드신 wikitext 형식의 나무위키 데이터',
 'naver_changwon_ner': '네이버 + 창원대 NER shared task data',
 'nsmc': 'e9t@github 님이 만드신 Naver sentiment movie corpus v1.0',
 'question_pair': 'songys@github 님이 만드신 질문쌍(Paired Question v.2)'}
```

- 다운로드 + 파이썬 로드 예제를 참고하려면 [Usage](https://github.com/ko-nlp/Korpora#usage) 항목의 각 데이터 설명을, 다운로드만 받고 싶을 경우에는 아래 예제를 참고하세요.
```python
from Korpora import Korpora

Korpora.fetch(corpus_name, force_download=True)
```

- 제공하는 모든 코퍼스를 설치하려면 `corpus_name` 에 'all' 을 입력하세요. 설치된 코퍼스를 재설치 하고 싶은 경우에는 `force_download=True` 를 이용할 수 있습니다.
```python
Korpora.fetch('all')
Korpora.fetch('all', force_download=True)
```