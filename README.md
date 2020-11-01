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
|open_substitles|[영화 자막 한영 병렬 말뭉치](https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/open_substitles.html)|[http://opus.nlpl.eu/OpenSubtitles-v2018.php](http://opus.nlpl.eu/OpenSubtitles-v2018.php)|


## 안내 페이지

`Korpora` 사용법을 자세히 안내하는 페이지는 다음과 같습니다.

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
pip install Korpora
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
   'open_substitles': 'Open parallel corpus (OPUS) 에서 제공하는 영화 자막 번역 병렬 말뭉치',
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
사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리(`~/Korpora`)에 말뭉치를 내려 받습니다.

```python
from Korpora import Korpora
Korpora.fetch('all')
```

KcBERT 학습데이터를 파이썬 콘솔에서 읽어들이는 예제는 다음과 같습니다.
데이터가 로컬에 없다면 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리(`~/Korpora`)에 말뭉치를 내려 받습니다.
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
사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리(`~/Korpora`)에 말뭉치를 내려 받습니다.

```bash
korpora fetch --corpus kcbert
```

터미널에서 KcBERT 학습데이터와 챗봇 문답 데이터 두 개를 동시에 다운로드 받는 예제는 다음과 같습니다.
이같은 방식으로 3개 이상의 데이터도 동시에 내려받을 수 있습니다.
사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리(`~/Korpora`)에 말뭉치를 내려 받습니다.

```bash
korpora fetch --corpus kcbert korean_chatbot_data
```

터미널에서 `Korpora`가 제공하는 모든 말뭉치를 내려받는 예제는 다음과 같습니다.
사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리(`~/Korpora`)에 말뭉치를 내려 받습니다.

```bash
korpora fetch --corpus all
```

터미널에서 언어모델(Language Model) 학습용 데이터를 만들 수 있습니다. 
언어모델 학습용 데이터 구축이라고 함은, `Korpora`가 제공하는 코퍼스에서 문장만을 떼어서 텍스트 파일로 덤프하는 걸 가리킵니다. 
기본 예제 코드는 다음과 같습니다. 
다음 코드는 `Korpora`가 제공하는 모든 코퍼스(`all`)를 언어모델 학습용 말뭉치로 일괄 처리하는 역할을 합니다.
다운로드와 전처리를 동시에 수행합니다.
로컬에 데이터가 없다면 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리(`~/Korpora`)에 말뭉치를 내려 받습니다.
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
  - 추가제한금지 : 이용자는 Korpora를 활용한 저작물에 [CC-BY](https://creativecommons.org/licenses/by/4.0)보다 엄격한 라이센스를 부가할 수 없습니다.
- 한편 말뭉치의 라이센스는 말뭉치별로 별도 적용됩니다. 자신이 사용할 말뭉치의 라이센스가 어떤 내용인지 활용 전에 반드시 확인하세요!
