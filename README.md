# Korpora: Korean Corpora Archives

최근 자연어 처리에 관심이 높아지면서 정부와 기업은 물론 뜻있는 개인에 이르기까지 데이터를 무료로 공개하는 추세입니다. 
하지만 데이터가 곳곳에 산재해 있다보니 품질 좋은 말뭉치임에도 그 존재조차 잘 알려지지 않은 경우가 많습니다. 
파일 포맷과 저장 형식 등이 각기 달라 사용이 쉽지 않습니다. 
개별 사용자들은 다운로드나 전처리 코드를 그때그때 개발해서 써야 하는 수고로움이 있습니다.

`Korpora`는 이 같은 불편함을 조금이나마 덜어드리기 위해 개발한 오픈소스 파이썬 패키지입니다. 
`Korpora`는 말뭉치라는 뜻의 영어 단어 *corpus*의 복수형인 *corpora*에서 착안해 이름 지었습니다. 
`Korpora`는 *Korean Corpora*의 준말입니다. 
`Korpora`가 마중물이 되어 한국어 데이터셋이 더 많이 공개되고 이를 통해 한국어 자연어 처리 수준이 한 단계 업그레이드되기를 희망합니다.


## 말뭉치 목록

`Korpora`가 제공하는 말뭉치 목록은 다음과 같습니다.

|corpus_name|description|link|
|---|---|---|
|korean_chatbot_data|[챗봇 트레이닝용 문답 페어](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/korean_chatbot_data.html)|[https://github.com/songys/Chatbot_data](https://github.com/songys/Chatbot_data)|
|kcbert|[KcBERT 모델 학습용 댓글 데이터](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/korean_comments.html)|[https://github.com/Beomi/KcBERT](https://github.com/Beomi/KcBERT)|
|korean_hate_speech|[한국어 혐오 데이터셋](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/korean_hate_speech.html)|[https://github.com/kocohub/korean-hate-speech](https://github.com/kocohub/korean-hate-speech)|
|korean_petitions|[청와대 국민 청원](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/korean_petitions.html)|[https://github.com/lovit/petitions_archive](https://github.com/lovit/petitions_archive)|
|kornli|[Korean NLI](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/kornli.html)|[https://github.com/kakaobrain/KorNLUDatasets](https://github.com/kakaobrain/KorNLUDatasets)|
|korsts|[Korean STS](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/korsts.html)|[https://github.com/kakaobrain/KorNLUDatasets](https://github.com/kakaobrain/KorNLUDatasets)|
|kowikitext|[한국어 위키 텍스트](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/kowikitext.html)|[https://github.com/lovit/kowikitext/](https://github.com/lovit/kowikitext/)|
|namuwikitext|[나무위키 텍스트](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/namuwikitext.html)|[https://github.com/lovit/namuwikitext](https://github.com/lovit/namuwikitext)|
|naver_changwon_ner|[네이버 x 창원대 개체명 인식 데이터셋](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/naver_changwon_ner.html)|[https://github.com/naver/nlp-challenge/tree/master/missions/ner](https://github.com/naver/nlp-challenge/tree/master/missions/ner)|
|nsmc|[NAVER Sentiment Movie Corpus](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/nsmc.html)|[https://github.com/e9t/nsmc](https://github.com/e9t/nsmc)|
|question_pair|[한국어 질문쌍 데이터셋](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/question_pair.html)|[https://github.com/songys/Question_pair](https://github.com/songys/Question_pair)|
|modu_news|[모두의 말뭉치: 신문](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/modu_news.html)|[https://corpus.korean.go.kr](https://corpus.korean.go.kr)|
|modu_messenger|[모두의 말뭉치: 메신저](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/modu_messenger.html)|[https://corpus.korean.go.kr](https://corpus.korean.go.kr)|
|modu_mp|[모두의 말뭉치: 형태 분석](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/modu_mp.html)|[https://corpus.korean.go.kr](https://corpus.korean.go.kr)|
|modu_ne|[모두의 말뭉치: 개체명 분석](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/modu_ne.html)|[https://corpus.korean.go.kr](https://corpus.korean.go.kr)|
|modu_spoken|[모두의 말뭉치: 구어](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/modu_spoken.html)|[https://corpus.korean.go.kr](https://corpus.korean.go.kr)|
|modu_web|[모두의 말뭉치: 웹](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/modu_web.html)|[https://corpus.korean.go.kr](https://corpus.korean.go.kr)|
|modu_written|[모두의 말뭉치: 문어](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/modu_written.html)|[https://corpus.korean.go.kr](https://corpus.korean.go.kr)|
|aihub_translation|[한국어-영어 번역 말뭉치](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/korean_parallel_koen_news.html)|[https://aihub.or.kr/aidata/87](https://aihub.or.kr/aidata/87)|
|open_subtitles|[영화 자막 한영 병렬 말뭉치](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/open_subtitles.html)|[http://opus.nlpl.eu/OpenSubtitles-v2018.php](http://opus.nlpl.eu/OpenSubtitles-v2018.php)|
|korean_parallel_koen_news|[한국어-영어 병렬 말뭉치](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/korean_parallel_koen_news.html)|[https://github.com/jungyeul/korean-parallel-corpora](https://github.com/jungyeul/korean-parallel-corpora)|


## 안내 페이지

`Korpora` 사용법을 자세히 안내하는 페이지는 다음과 같습니다.
아래의 페이지는 한글과 영어로 기술되어 있습니다.
영어 번역에 힘써주신 Han Kyul Kim ([@hank110](https://github.com/hank110/)) Won Ik Cho ([@warnikchow](https://github.com/warnikchow/)) (Alphabet order) 님에게 감사드립니다.

- [https://ko-nlp.github.io/Korpora](https://ko-nlp.github.io/Korpora)

핵심 기능 위주로 빠르게 살펴보고 싶은 분들은 아래 `빠른 사용법` 파트를 참고하세요.
실행시 주의점, 옵션 추가 및 변경 등은 위 페이지를 보시면 됩니다.


## 빠른 사용법

### 설치

From source

```bash
git clone https://github.com/ko-nlp/Korpora
python setup.py install
```

Using pip

```bash
pip install Korpora==0.2.0rc1
```

### 파이썬에서 사용하기

`Korpora`는 오픈소스 파이썬 패키지입니다.
기본적으로 파이썬 콘솔(console)에서 동작합니다. 
말뭉치 목록을 확인하는 파이썬 예제는 다음과 같습니다.

```python
from Korpora import Korpora
Korpora.corpus_list()
```

```python
{
   'kcbert': 'beomi@github 님이 만드신 KcBERT 학습데이터',
   'korean_chatbot_data': 'songys@github 님이 만드신 챗봇 문답 데이터',
   'korean_hate_speech': '{inmoonlight,warnikchow,beomi}@github 님이 만드신 혐오댓글데이터',
   'korean_petitions': 'lovit@github 님이 만드신 2017.08 ~ 2019.03 청와대 청원데이터',
   'kornli': 'KakaoBrain 에서 제공하는 Natural Language Inference (NLI) 데이터',
   'korsts': 'KakaoBrain 에서 제공하는 Semantic Textual Similarity (STS) 데이터',
   'kowikitext': "lovit@github 님이 만드신 wikitext 형식의 한국어 위키피디아 데이터",
   'namuwikitext': 'lovit@github 님이 만드신 wikitext 형식의 나무위키 데이터',
   'naver_changwon_ner': '네이버 + 창원대 NER shared task data',
   'nsmc': 'e9t@github 님이 만드신 Naver sentiment movie corpus v1.0',
   'question_pair': 'songys@github 님이 만드신 질문쌍(Paired Question v.2)',
   'modu_news': '국립국어원에서 만든 모두의 말뭉치: 뉴스 말뭉치',
   'modu_messenger': '국립국어원에서 만든 모두의 말뭉치: 메신저 말뭉치',
   'modu_mp': '국립국어원에서 만든 모두의 말뭉치: 형태 분석 말뭉치',
   'modu_ne': '국립국어원에서 만든 모두의 말뭉치: 개체명 분석 말뭉치',
   'modu_spoken': '국립국어원에서 만든 모두의 말뭉치: 구어 말뭉치',
   'modu_web': '국립국어원에서 만든 모두의 말뭉치: 웹 말뭉치',
   'modu_written': '국립국어원에서 만든 모두의 말뭉치: 문어 말뭉치',
   'aihub_translation': "AI Hub 에서 제공하는 번역용 병렬 말뭉치 (구어 + 대화 + 뉴스 + 한국문화 + 조례 + 지자체웹사이트)",
   'aihub_spoken_translation': "AI Hub 에서 제공하는 번역용 병렬 말뭉치 (구어)",
   'aihub_conversation_translation': "AI Hub 에서 제공하는 번역용 병렬 말뭉치 (대화)",
   'aihub_news_translation': "AI Hub 에서 제공하는 번역용 병렬 말뭉치 (뉴스)",
   'aihub_korean_culture_translation': "AI Hub 에서 제공하는 번역용 병렬 말뭉치 (한국문화)",
   'aihub_decree_translation': "AI Hub 에서 제공하는 번역용 병렬 말뭉치 (조례)",
   'aihub_government_website_translation': "AI Hub 에서 제공하는 번역용 병렬 말뭉치 (지자체웹사이트)",
   'open_subtitles': 'Open parallel corpus (OPUS) 에서 제공하는 영화 자막 번역 병렬 말뭉치',
}
```

파이썬 콘솔에서 KcBERT 학습데이터를 내려 받는 파이썬 예제는 다음과 같습니다.
사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리(`~/Korpora`)에 말뭉치를 내려 받습니다.
다른 데이터를 받고 싶다면 위에서 확인한 말뭉치 이름을 인자로 주면 됩니다.

```python
from Korpora import Korpora
Korpora.fetch("kcbert")
```

`Korpora`가 제공하는 모든 말뭉치를 내려받고 싶다면 다음과 같이 실행하세요.
`~/Korpora`에 말뭉치를 내려 받습니다.

```python
from Korpora import Korpora
Korpora.fetch('all')
```

KcBERT 학습데이터를 파이썬 콘솔에서 읽어들이는 예제는 다음과 같습니다.
데이터가 로컬에 없다면 `~/Korpora`에 말뭉치를 내려 받습니다.
이후 `corpus`라는 파이썬 변수에 말뭉치 데이터가 담기게 됩니다.
다른 데이터를 읽고 싶다면 위에서 확인한 말뭉치 이름을 인자로 주면 됩니다.

```python
from Korpora import Korpora
corpus = Korpora.load("kcbert")
```

### 터미널에서 사용하기

`Korpora`는 터미널에서도 동작합니다(Command Line Interface, CLI).
파이썬 콘솔 실행 없이 `Korpora`를 사용할 수 있습니다. 
터미널에서 KcBERT 학습데이터 하나를 다운받는 예제는 다음과 같습니다.
`~/Korpora`에 말뭉치를 내려 받습니다.

```bash
korpora fetch --corpus kcbert
```

터미널에서 KcBERT 학습데이터와 챗봇 문답 데이터 두 개를 동시에 다운로드 받는 예제는 다음과 같습니다.
이같은 방식으로 3개 이상의 데이터도 동시에 내려받을 수 있습니다.
`~/Korpora`에 말뭉치를 내려 받습니다.

```bash
korpora fetch --corpus kcbert korean_chatbot_data
```

터미널에서 `Korpora`가 제공하는 모든 말뭉치를 내려받는 예제는 다음과 같습니다.
`~/Korpora`에 말뭉치를 내려 받습니다.

```bash
korpora fetch --corpus all
```

터미널에서 언어모델(Language Model) 학습용 데이터를 만들 수 있습니다. 
언어모델 학습용 데이터 구축이라고 함은, `Korpora`가 제공하는 코퍼스에서 문장만을 떼어서 텍스트 파일로 덤프하는 걸 가리킵니다. 
기본 예제 코드는 다음과 같습니다. 
다음 코드는 `Korpora`가 제공하는 모든 코퍼스(`all`)를 언어모델 학습용 말뭉치로 일괄 처리하는 역할을 합니다.
다운로드와 전처리를 동시에 수행합니다.
로컬에 데이터가 없다면 `~/Korpora`에 말뭉치를 내려 받습니다.
결과물은 `all.train`이라는 파일 하나입니다. 
`output_dir`에 생성됩니다.

```bash
korpora lmdata \
  --corpus all \
  --output_dir ~/works/lmdata
```

## License

- Korpora 라이센스는 Creative Commons License(CCL) 4.0의 [CC-BY](https://creativecommons.org/licenses/by/4.0)입니다. 이 라이센스는 Korpora 패키지 및 그 부속물에 한정됩니다.
- 이용자는 다음의 권리를 갖습니다.
  - 공유 : 복제, 배포, 전시, 공연 및 공중 송신(포맷 변경도 포함) 등을 자유롭게 할 수 있습니다.
  - 변경 : 리믹스, 변형, 2차적 저작물의 작성이 가능합니다. 영리 목적으로도 이용이 가능합니다.
- 이용자는 다음의 의무가 있습니다. 아래 의무를 지키는 한 위의 권리가 유효합니다.
  - 저작자표시 : Korpora를 이용했다는 정보를 표시해야 합니다. 
  - 추가제한금지 : 이용자는 Korpora를 활용한 2차적 저작물에 [CC-BY](https://creativecommons.org/licenses/by/4.0)보다 엄격한 라이센스를 부가할 수 없습니다.
  - 예컨대 Korpora를 내려 받아 단순히 사용하기만 했다면 '저작자표시'만 지키면 됩니다. Korpora를 활용해 모델이나 문서 등 2차 저작물을 만들고 이를 배포할 경우 '저작자표시'뿐 아니라 '추가제한금지' 의무도 지켜야 합니다.
- 한편 말뭉치의 라이센스는 말뭉치별로 별도 적용됩니다. 자신이 사용할 말뭉치의 라이센스가 어떤 내용인지 활용 전에 반드시 확인하세요!


# Korpora: Korean Corpora Archives

Due to the growing interest in natural language processing, governments, businesses, and individuals are disclosing their data for free.
However, even for a high-quality corpus, its existence is often unknown as datasets are scattered in different locations.
Furthermore, each of their file or saved format is often different, making it even more difficult to use them.
Therefore, individuals need to painstakingly create download or preprocessing codes for every instance.

`Korpora` is an open-source Python package that aims to minimize such inconvenience.
The name `Korpora` comes from the word *corpora*, a plural form of the word *corpus*.
`Korpora` is an acronym that stands for *Korean Corpora*.
We hope that `Korpora` will serve as a starting point that encourages more Korean datasets to be released and improve the state of Korean natural language processing to the next level.


## List of corpora

`Korpora` provides following corpora.

|corpus_name|description|link|
|---|---|---|
|korean_chatbot_data|[Question and answer pairs for training a chatbot](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/korean_chatbot_data.html)|[https://github.com/songys/Chatbot_data](https://github.com/songys/Chatbot_data)|
|kcbert|[Comment data used for training KcBERT model](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/korean_comments.html)|[https://github.com/Beomi/KcBERT](https://github.com/Beomi/KcBERT)|
|korean_hate_speech|[Korean hate speech dataset](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/korean_hate_speech.html)|[https://github.com/kocohub/korean-hate-speech](https://github.com/kocohub/korean-hate-speech)|
|korean_petitions|[Petitions to Blue House](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/korean_petitions.html)|[https://github.com/lovit/petitions_archive](https://github.com/lovit/petitions_archive)|
|kornli|[Korean NLI](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/kornli.html)|[https://github.com/kakaobrain/KorNLUDatasets](https://github.com/kakaobrain/KorNLUDatasets)|
|korsts|[Korean STS](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/korsts.html)|[https://github.com/kakaobrain/KorNLUDatasets](https://github.com/kakaobrain/KorNLUDatasets)|
|kowikitext|[Korean Wikipedia text](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/kowikitext.html)|[https://github.com/lovit/kowikitext/](https://github.com/lovit/kowikitext/)|
|namuwikitext|[Namuwiki text](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/namuwikitext.html)|[https://github.com/lovit/namuwikitext](https://github.com/lovit/namuwikitext)|
|naver_changwon_ner|[NAVER x Changwon National University NER dataset](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/naver_changwon_ner.html)|[https://github.com/naver/nlp-challenge/tree/master/missions/ner](https://github.com/naver/nlp-challenge/tree/master/missions/ner)|
|nsmc|[NAVER Sentiment Movie Corpus](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/nsmc.html)|[https://github.com/e9t/nsmc](https://github.com/e9t/nsmc)|
|question_pair|[Korean question and answer pair dataset](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/question_pair.html)|[https://github.com/songys/Question_pair](https://github.com/songys/Question_pair)|
|modu_news|[Modu Corpus: Newspaper](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/modu_news.html)|[https://corpus.korean.go.kr](https://corpus.korean.go.kr)|
|modu_messenger|[Modu Corpus: Messenger](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/modu_messenger.html)|[https://corpus.korean.go.kr](https://corpus.korean.go.kr)|
|modu_mp|[Modu Corpus: Morphemes](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/modu_mp.html)|[https://corpus.korean.go.kr](https://corpus.korean.go.kr)|
|modu_ne|[Modu Corpus: Named Entity](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/modu_ne.html)|[https://corpus.korean.go.kr](https://corpus.korean.go.kr)|
|modu_spoken|[Modu Corpus: Spoken](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/modu_spoken.html)|[https://corpus.korean.go.kr](https://corpus.korean.go.kr)|
|modu_web|[Modu Corpus: Web](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/modu_web.html)|[https://corpus.korean.go.kr](https://corpus.korean.go.kr)|
|modu_written|[Modu Corpus: Written](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/modu_written.html)|[https://corpus.korean.go.kr](https://corpus.korean.go.kr)|
|aihub_translation|[Korean-English translation corpus](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/korean_parallel_koen_news.html)|[https://aihub.or.kr/aidata/87](https://aihub.or.kr/aidata/87)|
|open_subtitles|[Korean-English parallel corpus from movie subtitles](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/open_subtitles.html)|[http://opus.nlpl.eu/OpenSubtitles-v2018.php](http://opus.nlpl.eu/OpenSubtitles-v2018.php)|
|korean_parallel_koen_news|[Korean-English parallel corpus](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/korean_parallel_koen_news.html)|[https://github.com/jungyeul/korean-parallel-corpora](https://github.com/jungyeul/korean-parallel-corpora)|


## Information page

Detailed information on `Korpora` is available from the link below.
The information page is written in both Korean and English.
We like to thank Han Kyul Kim ([@hank110](https://github.com/hank110/)) and Won Ik Cho ([@warnikchow](https://github.com/warnikchow/)) (Alphabet order) for the English translation.

- [https://ko-nlp.github.io/Korpora](https://ko-nlp.github.io/Korpora)

For those who would like to quickly go through the core functions, please refer to the `Quick overview` part below.
For more information about notes on execution or option modifications, please refer to the information page linked above.


## Quick overview

### Installation

From source

```bash
git clone https://github.com/ko-nlp/Korpora
python setup.py install
```

Using pip

```bash
pip install Korpora==0.2.0rc1
```

### Using in Python

`Korpora` is an open-source Python package.
By default, it can be executed in a Python console.
You can check the list of the available corpus with the following Python codes.

```python
from Korpora import Korpora
Korpora.corpus_list()
```

```python
{
   'kcbert': 'beomi@github 님이 만드신 KcBERT 학습데이터',
   'korean_chatbot_data': 'songys@github 님이 만드신 챗봇 문답 데이터',
   'korean_hate_speech': '{inmoonlight,warnikchow,beomi}@github 님이 만드신 혐오댓글데이터',
   'korean_petitions': 'lovit@github 님이 만드신 2017.08 ~ 2019.03 청와대 청원데이터',
   'kornli': 'KakaoBrain 에서 제공하는 Natural Language Inference (NLI) 데이터',
   'korsts': 'KakaoBrain 에서 제공하는 Semantic Textual Similarity (STS) 데이터',
   'kowikitext': "lovit@github 님이 만드신 wikitext 형식의 한국어 위키피디아 데이터",
   'namuwikitext': 'lovit@github 님이 만드신 wikitext 형식의 나무위키 데이터',
   'naver_changwon_ner': '네이버 + 창원대 NER shared task data',
   'nsmc': 'e9t@github 님이 만드신 Naver sentiment movie corpus v1.0',
   'question_pair': 'songys@github 님이 만드신 질문쌍(Paired Question v.2)',
   'modu_news': '국립국어원에서 만든 모두의 말뭉치: 뉴스 말뭉치',
   'modu_messenger': '국립국어원에서 만든 모두의 말뭉치: 메신저 말뭉치',
   'modu_mp': '국립국어원에서 만든 모두의 말뭉치: 형태 분석 말뭉치',
   'modu_ne': '국립국어원에서 만든 모두의 말뭉치: 개체명 분석 말뭉치',
   'modu_spoken': '국립국어원에서 만든 모두의 말뭉치: 구어 말뭉치',
   'modu_web': '국립국어원에서 만든 모두의 말뭉치: 웹 말뭉치',
   'modu_written': '국립국어원에서 만든 모두의 말뭉치: 문어 말뭉치',
   'aihub_translation': "AI Hub 에서 제공하는 번역용 병렬 말뭉치 (구어 + 대화 + 뉴스 + 한국문화 + 조례 + 지자체웹사이트)",
   'aihub_spoken_translation': "AI Hub 에서 제공하는 번역용 병렬 말뭉치 (구어)",
   'aihub_conversation_translation': "AI Hub 에서 제공하는 번역용 병렬 말뭉치 (대화)",
   'aihub_news_translation': "AI Hub 에서 제공하는 번역용 병렬 말뭉치 (뉴스)",
   'aihub_korean_culture_translation': "AI Hub 에서 제공하는 번역용 병렬 말뭉치 (한국문화)",
   'aihub_decree_translation': "AI Hub 에서 제공하는 번역용 병렬 말뭉치 (조례)",
   'aihub_government_website_translation': "AI Hub 에서 제공하는 번역용 병렬 말뭉치 (지자체웹사이트)",
   'open_subtitles': 'Open parallel corpus (OPUS) 에서 제공하는 영화 자막 번역 병렬 말뭉치',
}
```

From the Python console, you can download KcBERT training data with the following Python codes.
The corpus is downloaded to the Korpora directory within the user's root directory (`~/Korpora`).
If you want to download a different dataset, please change the name of the corpus in the argument by the name of the dataset as expressed in the list above.

```python
from Korpora import Korpora
Korpora.fetch("kcbert")
```

If you want to download all corpora provided by `Korpora`, use the following Python codes.
All datasets are downloaded to `~/Korpora`.

```python
from Korpora import Korpora
Korpora.fetch('all')
```

Using the following codes, you can load the KcBERT training dataset from your Python console.
If the corpus does not exist in the local directory, it is downloaded to `~/Korpora` as well.
Then, the corpus data is stored in a Python variable `corpus`.
To load a different dataset, please change the name of the corpus in the argument by the name of the dataset as expressed in the list above.

```python
from Korpora import Korpora
corpus = Korpora.load("kcbert")
```

### Using in a terminal

You can execute `Korpora` through your terminal as well (Command Line Interface, CLI).
`Korpora` can be used without executing your Python console.
You can download the KcBERT training dataset from your terminal with the following command.
The dataset is downloaded to `~/Korpora`.

```bash
korpora fetch --corpus kcbert
```

With the following command, you can simultaneously download the KcBERT training dataset and the chatbot Q&A pair dataset.
With this command, you can also simultaneously download three or more datasets.
Datasets are downloaded to `~/Korpora`.

```bash
korpora fetch --corpus kcbert korean_chatbot_data
```

You can download all corpora provided by `Korpora` from your terminal with the following command.
Datasets are downloaded to `~/Korpora`.

```bash
korpora fetch --corpus all
```

From your terminal, you can also create a dataset for training a language model. 
Creating this training dataset for a language model refers to a process of extracting only the sentences from all corpora provided by `Korpora` and saving them in a text file.
A sample command is as follows.
It simultaneously processes all corpora provided by `Korpora` and creates a single training dataset for a language model.
Downloading the corpus and preprocessing its text occur simultaneously as well.
If the corpus does not exist in the local directory, it is downloaded to `~/Korpora`. 
A single output file named `all.train` will be created. 
It is created within `output_dir`.

```bash
korpora lmdata \
  --corpus all \
  --output_dir ~/works/lmdata
```

## License

- Korpora is licensed under the Creative Commons License(CCL) 4.0 [CC-BY](https://creativecommons.org/licenses/by/4.0). This license covers the Korpora package and all of its components.
- Its users have the following rights.
  - Share : They are free to reproduce, distribute, exhibit, perform and transmit via air (including changes in the format).
  - Adapt : They can remix, transform, and build upon the material for any purpose, even commercially.
- Its users have the following obligations. As long as these obligations are fulfilled, the user rights listed above are valid.
  - Attribution : They must indicate that they have used Korpora. 
  - No additional restrictions : For all derivative works of Korpora, they cannot impose stricter license than [CC-BY](https://creativecommons.org/licenses/by/4.0) permits.
  - For example, if you have downloaded and used Korpora, you need to fulfill only the 'attribution' obligation. However, if you are creating and distributing models, documents or any other derivative works of Korpora, you must fulfill both the 'attribution' and 'no additional restrictions' obligations.
- Each corpus adheres to its own license policy. Please check the license of the corpus before using it!
