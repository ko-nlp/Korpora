# Korpora: Korean Corpora Archives

Korpora 는 다른 분들이 연구 목적으로 공유해주신 말뭉치들을 손쉽게 다운로드, 사용할 수 있는 기능만을 제공합니다.

말뭉치들을 공유해 주신 분들에게 감사드리며, 각 말뭉치 별 설명과 라이센스는 말뭉치 별 클래스에 기술하였습니다.
말뭉치마다 데이터를 로딩할 때 설명과 라이센스가 화면에 출력됩니다.
해당 말뭉치에 대해 자세히 알고 싶으신 분은 출력되는 description 을 참고하세요.
해당 말뭉치를 연구/상용의 목적으로 이용하실 때에는 아래의 라이센스를 참고해 주시기 바랍니다.

This package provides easy-download and easy-usage for various Korean corpora.

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
|kowikitext|한국어 위키피디아 텍스트|https://github.com/lovit/kowikitext|
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
 'korean_parallel_koen_news': 'jungyeul@github 님이 만드신 병렬 말뭉치',
 'korean_petitions': 'lovit@github 님이 만드신 2017.08 ~ 2019.03 청와대 청원데이터',
 'kornli': 'KakaoBrain 에서 제공하는 Natural Language Inference (NLI) 데이터',
 'korsts': 'KakaoBrain 에서 제공하는 Semantic Textual Similarity (STS) 데이터',
 'kowikitext': 'lovit@github 님이 만드신 wikitext 형식의 한국어 위키피디아 데이터',
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

## Usage

### 챗봇 트레이닝용 문답 페어
- author: songys@github
- repository: https://github.com/songys/Chatbot_data
- size:
  - train: 11,876 examples
- example
```python
from Korpora import Korpora, KoreanChatbotKorpus

chatbot_corpus = KoreanChatbotKorpus() # or
chatbot_corpus = Korpora.load('korean_chatbot_data')

chatbot_corpus.train[0]
# LabeledSentencePair(text='12시 땡!', pair='하루가 또 가네요.', label=0)
chatbot_corpus.train[0].text
# 12시 땡!
chatbot_corpus.train[0].pair
# 하루가 또 가네요.
chatbot_corpus.train[0].label
# 0
```

- data structure

|속성명|내용|
|---|---|
|text|질문|
|pair|답변|
|label|일상다반사 0, 이별(부정) 1, 사랑(긍정) 2|


### KcBERT dataset
- author: beomi@github
- repository: https://github.com/Beomi/KcBERT
- size:
  - train: 86,246,285 examples
- example
```python
from Korpora import Korpora, KcBERTKorpus

kcbert_corpus = KcBERTKorpus() # or
kcbert_corpus = Korpora.load("kcbert")

kcbert_corpus.train[0]
# 우리에게 북한은 꼭 없애야 할 적일뿐
```


### Korean Hate Speech
- author: inmoonlight@github, warnikchow@github, beomi@github
- repository: https://github.com/kocohub/korean-hate-speech
- size:
  - train: 7,896 examples
  - dev: 471 examples
  - test: 974 examples
  - unlabeled: 2,033,893 examples
- example
```python
from Korpora import Korpora, KoreanHateSpeech

korean_hate_speech = KoreanHateSpeech() # or
korean_hate_speech = Korpora.load('korean_hate_speech')

korean_hate_speech.train[0]
# KoreanHateSpeechLabeledExample(text='(현재 호텔주인 심정) 아18...', title='"밤새 조문 행렬...', gender_bias='False', bias='others', hate='hate')
korean_hate_speech.train[0].text
# (현재 호텔주인 심정) 아18...(현재 호텔주인 심정) 아18...
korean_hate_speech.train[0].title
# "밤새 조문 행렬...
korean_hate_speech.train[0].gender_bias
# False
korean_hate_speech.train[0].bias
# others
korean_hate_speech.train[0].hate
# hate
korean_hate_speech.dev[0]
# KoreanHateSpeechLabeledExample(text='송중기 시대극은 믿고본다...', title='"\'아스달 연대기\'...', gender_bias='False', bias='none', hate='none')
korean_hate_speech.test[0]
# SentencePair(text='ㅋㅋㅋㅋ 그래도 조아해주는 팬들 많아서 좋겠다 ㅠㅠ 니들은 온유가 안만져줌 ㅠㅠ', pair='"샤이니 온유, 클럽 강제추행 \'무혐의\' 처분 받았다"')
korean_hate_speech.unlabeled[0]
# SentencePair(text='"[단독] 지드래곤♥이주연, 제주도 데이트...', pair='"[단독] 지드래곤♥이주연, 제주도 데이트...')
```

- data structure

|속성명|내용|
|---|---|
|text|뉴스 댓글|
|title/pair|뉴스 제목|
|gender_bias|성적 차별 여부(True/False)|
|bias|차별 종류(종교 인종 나이 외모 등)|
|hate|특정 계층 혐오 여부(hate/none)|


### 청와대 국민청원 (2017.08 ~ 2019.03)
- author: lovit@github
- repository: https://github.com/lovit/petitions_archive
- size:
  - train: 433,631 examples
- example
```python
from Korpora import Korpora, KoreanPetitions

petitions = KoreanPetitions()  # or
petitions = Korpora.load('korean_petitions')

petitions.train[0]
# KoreanPetition(text="안녕하세요. 현재 사대, ...", category='육아/교육', num_agree=88, begin='2017-08-25', end='2017-09-24', title='학교는 ...')
petitions.train[0].text
# 안녕하세요. 현재 사대, ...
petitions.train[0].category
# 육아/교육
petitions.train[0].num_agree
# 88
petitions.train[0].begin
# 2017-08-25
petitions.train[0].end
# 2017-09-24
petitions.train[0].title
# 학교는 ...
```
- data structure

|속성명|내용|
|---|---|
|text|청원 내용|
|category|청원 범주|
|num_agree|청원 동의 수|
|begin|청원 시작일|
|end|청원 종료일|
|title|청원 제목|

### KorNLI
- author: KakaoBrain
- repository: https://github.com/kakaobrain/KorNLUDatasets
- references: Ham, J., Choe, Y. J., Park, K., Choi, I., & Soh, H. (2020). [KorNLI and KorSTS: New Benchmark Datasets for Korean Natural Language Understanding.](https://arxiv.org/abs/2004.03289) arXiv preprint arXiv:2004.03289.
- size:
  - multinli_train: 392,702 examples
  - snli_train: 550,152 examples
  - xnli_dev: 2,490 examples
  - xnli_test: 5,010 examples
- example
```python
from Korpora import Korpora, KorNLI

kornli = KorNLI() # or
kornli = Korpora.load('kornli')

kornli.multinli_train[0]
# LabeledSentencePair(text='개념적으로 크림 스키밍은 제품과 지리라는 두 가지 기본 차원을 가지고 있다.', pair='제품과 지리학은 크림 스키밍을 작동시키는 것이다.', label='neutral')
kornli.multinli_train[0].text
# 개념적으로 크림 스키밍은 제품과 지리라는 두 가지 기본 차원을 가지고 있다.
kornli.multinli_train[0].pair
# 제품과 지리학은 크림 스키밍을 작동시키는 것이다.
kornli.multinli_train[0].label
# neutral
kornli.snli_train[0]
# LabeledSentencePair(text='말을 탄 사람이 고장난 비행기 위로 뛰어오른다.', pair='한 사람이 경쟁을 위해 말을 훈련시키고 있다.', label='neutral')
kornli.xnli_dev[0]
# LabeledSentencePair(text='그리고 그가 말했다, "엄마, 저 왔어요."', pair='그는 학교 버스가 그를 내려주자마자 엄마에게 전화를 걸었다.', label='neutral')
kornli.xnli_test[0]
# LabeledSentencePair(text='글쎄, 나는 그것에 관해 생각조차 하지 않았지만...', pair='나는 그와 다시 이야기하지 않았다.', label='contradiction')
```

- data structure

|속성명|내용|
|---|---|
|text|문장|
|pair|text와 쌍이 되는 문장|
|label|text, pair 사이의 관계|


### KorSTS
- author: KakaoBrain
- repository: https://github.com/kakaobrain/KorNLUDatasets
- references: Ham, J., Choe, Y. J., Park, K., Choi, I., & Soh, H. (2020). [KorNLI and KorSTS: New Benchmark Datasets for Korean Natural Language Understanding.](https://arxiv.org/abs/2004.03289) arXiv preprint arXiv:2004.03289.
- size:
  - train: 5,749 examples
  - dev: 1,500 examples
  - test: 1,379 examples
- example
```python
from Korpora import Korpora, KorSTS

korsts = KorSTS() # or
korsts = Korpora.load('korsts')
korsts.train[0]
# KorSTSExample(text='비행기가 이륙하고 있다.', pair='비행기가 이륙하고 있다.', label=5.0, genre='main-captions', filename='MSRvid', year='2012test')
korsts.train[0].text
# 비행기가 이륙하고 있다.
korsts.train[0].pair
# 비행기가 이륙하고 있다.
korsts.train[0].label
# 5.0
korsts.dev[0]
# KorSTSExample(text='안전모를 가진 한 남자가 춤을 추고 있다.', pair='안전모를 쓴 한 남자가 춤을 추고 있다.', label=5.0, genre='main-captions', filename='MSRvid', year='2012test')
korsts.test[0]
# KorSTSExample(text='한 소녀가 머리를 스타일링하고 있다.', pair='한 소녀가 머리를 빗고 있다.', label=2.5, genre='main-captions', filename='MSRvid', year='2012test')
```

- data structure

|속성명|내용|
|---|---|
|text|문장|
|pair|text와 쌍이 되는 문장|
|label|text, pair 사이의 관계|
|기타|데이터 관련 추가 정보|


### kowikitext
- author: lovit@github
- repository: https://github.com/lovit/kowikitext
- size:
  - train : 26794425 lines (877754 articles, 1.7G)
  - dev : 130419 lines (4433 articles, 7.7M)
  - test : 134340 lines (4434 articles, 8.4M)
- example
```python
from Korpora import Korpora, KowikiTextKorpus

kowiki = KowikiTextKorpus() # or
kowiki = Korpora.load('kowikitext')

kowiki.train[0]
# SentencePair(text='외교부장\n외교부장', pair=' = 분류:중화인민공화국의 외교부장 =')
kowiki.train[0].text
# '외교부장\n외교부장'
kowiki.train[0].pair
#  = 분류:중화인민공화국의 외교부장 =
kowiki.dev[0]
# SentencePair(text='스폴리아텔레(, )는 이탈리아의 후식으로서 ...', pair=' = 스폴리아텔레 =')
kowiki.test[0]
# SentencePair(text='기타', pair=' = 분류:러시아의 기타 연주자 =')
```
- data structure

|속성명|내용|
|---|---|
|text|섹션 본문|
|pair|섹션 타이틀|


### 나무위키텍스트
- author: lovit@github
- repository: https://github.com/lovit/namuwikitext
- size:
  - train: 38,278,040 lines (500,104 docs, 5.3G)
  - dev: 197,723 lines (2,525 docs, 28M)
  - test: 193,614 lines (2,525 docs, 29M)
- example
```python
from Korpora import Korpora, NamuwikiTextKorpus

namuwiki = NamuwikiTextKorpus() # or
namuwiki = Korpora.load('namuwikitext')

namuwiki.train[0]
# SentencePair(text='상위 문서: 아스날 FC\n2009-10 시즌 2011-12 시즌\n2010 -11 시즌...', pair=' = 아스날 FC/2010-11 시즌 =')
namuwiki.train[0].text
# 상위 문서: 아스날 FC\n2009-10 시즌 2011-12 시즌\n2010 -11 시즌...
namuwiki.train[0].pair
# = 아스날 FC/2010-11 시즌 =
namuwiki.dev[0]
# SentencePair(text='상위 항목: 축구 관련 인물, 외국인 선수/역대 프로축구\n...', pair=' = 소말리아(축구선수) =')
namuwiki.test[0]
# SentencePair(text='', pair=' = 덴덴타운 =')
```
- data structure

|속성명|내용|
|---|---|
|text|섹션 본문|
|pair|섹션 타이틀|


### 네이버, 창원대가 함께하는 NLP Challenge (NER)
- author: 네이버 + 창원대
- repository: https://github.com/naver/nlp-challenge/tree/master/missions/ner
- reference: http://air.changwon.ac.kr/?page_id=10
- size:
  - train: 90,000 examples
- example
```python
from Korpora import Korpora, NaverChangwonNERKorpus

ner = NaverChangwonNERKorpus() # or
ner = Korpora.load('naver_changwon_ner')

ner.train[0]
# WordTag(text='비토리오 양일 만에 영사관 감호 용퇴, 항룡 압력설 의심만 가율 ', words=['비토리오', '양일', '만에', '영사관', '감호', '용퇴,', '항룡', '압력설', '의심만', '가율'], tags=['PER_B', 'DAT_B', '-', 'ORG_B', 'CVL_B', '-', '-', '-', '-', '-'])
ner.train[0].text
# 비토리오 양일 만에 영사관 감호 용퇴, 항룡 압력설 의심만 가율 
ner.train[0].words
# ['비토리오', '양일', '만에', '영사관', '감호', '용퇴,', '항룡', '압력설', '의심만', '가율']
ner.train[0].tags
# ['PER_B', 'DAT_B', '-', 'ORG_B', 'CVL_B', '-', '-', '-', '-', '-']
```
- data structure

|속성명|내용|
|---|---|
|text|words를 공백으로 이어 붙인 string|
|words|단어 시퀀스|
|tags|words에 대응하는 개체명 태그 시퀀스|


### Naver sentiment movie corpus v1.0
- author: e9t@github
- repository: https://github.com/e9t/nsmc
- references: www.lucypark.kr/docs/2015-pyconkr/#39
- size:
  - train: 150,000 examples
  - test: 50,000 examples
- example
```python
from Korpora import Korpora, NSMC

nsmc = NSMC() # or
nsmc = Korpora.load('nsmc')

nsmc.train[0]
# LabeledSentence(text='아 더빙.. 진짜 짜증나네요 목소리', label=0)
nsmc.train[0].text
# 아 더빙.. 진짜 짜증나네요 목소리
nsmc.train[0].label
# 0
nsmc.test[0]
# LabeledSentence(text='굳 ㅋ', label=1)
```

- data structure

|속성명|내용|
|---|---|
|text|영화 리뷰 댓글|
|label|영화에 대한 평가 (긍정 1, 부정 0)|


### 한국어 질문쌍 (Paired Question v.2)
- author: songys@github
- repository: https://github.com/songys/Question_pair
- size:
  - train: 6,888 examples
  - test: 688 examples
- example
```python
from Korpora import Korpora, QuestionPairKorpus

question_pair = QuestionPairKorpus() # or
question_pair = Korpora.load('question_pair')

question_pair.train[0]
# LabeledSentencePair(text='1000일 만난 여자친구와 이별', pair='10년 연예의끝', label='1')
question_pair.train[0].text
# 1000일 만난 여자친구와 이별
question_pair.train[0].pair
# 10년 연예의끝
question_pair.train[0].label
# 1
question_pair.test[0]
# LabeledSentencePair(text='21살의 사랑에 대해', pair='사랑을 노력한다는게 말이 되나요?', label='1')
```
- data structure

|속성명|내용|
|---|---|
|text|문장|
|pair|text와 쌍을 이루는 문장|
|label|text와 pair가 같은 질문이면 0, 다른 질문이면 1|

### Korean Parallel Corpus
- author: jungyeul@github
- repository: https://github.com/jungyeul/korean-parallel-corpora
- size:
  - train: 94,123 pairs
  - dev: 1,000 pairs
  - test: 2,000 pairs
- example
```python
from Korpora import Korpora, KoreanParallelKOENNewsKorpus

koen_news = KoreanParallelKOENNewsKorpus() # or
koen_news = Korpora.load('korean_parallel_koen_news')

koen_news.train[0]
# SentencePair(text='개인용 컴퓨터 사용의 상당 부분은 "이것보다 뛰어날 수 있느냐?"', pair='Much of personal computing is about "can you top this?"')
koen_news.train[0].text
# 개인용 컴퓨터 사용의 상당 부분은 "이것보다 뛰어날 수 있느냐?"
koen_news.train[0].pair
# Much of personal computing is about "can you top this?"
koen_news.test[0]
# SentencePair(text='토론에 참여한 사람들은 법 집행과 국가 ...', pair='Those involved in the discussions do take seriously ...')
koen_news.dev[0]
# SentencePair(text='세계 에서 가장 강력한 수퍼컴퓨터를 1년...', pair="After keeping the world's most powerful supercomputer ...")
```
- data structure

|속성명|내용|
|---|---|
|text|`ko` 문장|
|pair|`en` 문장|
