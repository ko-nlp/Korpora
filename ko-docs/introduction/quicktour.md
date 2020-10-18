---
sort: 3
---

# 빠른 사용법

`Korpora` 패키지의 핵심 기능을 빠르게 살펴봅니다.

## 파이썬에서 사용하기

`Korpora`는 오픈소스 파이썬 패키지입니다.
기본적으로 파이썬 콘솔(console)에서 동작합니다. 

### 말뭉치 목록 확인

`Korpora` 패키지가 제공하는 말뭉치 목록을 확인하는 파이썬 예제는 다음과 같습니다.

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

### 말뭉치 다운로드

KcBERT 학습데이터를 내려 받는 파이썬 예제는 다음과 같습니다.
다른 데이터를 받고 싶다면 위에서 확인한 말뭉치 이름을 인자로 주면 됩니다.

```python
from Korpora import Korpora
Korpora.fetch("kcbert")
```

```note
기본적으로 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리에 말뭉치를 내려 받습니다(`~/Korpora`). 다른 경로에 말뭉치를 다운로드 받고 싶다면 
fetch 함수 실행시 `root_dir=custom_path`라는 인자를 추가하세요.
```

```tip
fetch 함수 실행시 `force_download=True`라는 인자를 줄 경우 해당 말뭉치가 이미 로컬에 있더라도 이를 무시하고 다시 내려 받습니다. 기본값은 `False`입니다.
```

`Korpora`가 제공하는 모든 말뭉치를 내려받고 싶다면 다음과 같이 실행하세요.

```python
from Korpora import Korpora
Korpora.fetch('all')
```

```warning
국립국어원에서 제공하는 '모두의 말뭉치'와 AIHub 관련 데이터는 라이센스 문제로 `Korpora` 패키지에서는 다운로드 기능을 제공하지 않습니다. 
해당 말뭉치를 사용하고 싶다면 해당 기관의 안내대로 인증 과정을 거쳐 수작업으로 말뭉치를 내려받아야 합니다.
```

### 말뭉치 읽어들이기

KcBERT 학습데이터를 파이썬 콘솔에서 읽어들이는 예제는 다음과 같습니다.
다른 데이터를 읽고 싶다면 위에서 확인한 말뭉치 이름을 인자로 주면 됩니다.

```python
from Korpora import Korpora
corpus = Korpora.load("kcbert")
```

위 코드를 실행하면 `corpus`라는 파이썬 변수에 말뭉치 데이터가 담기게 됩니다.
만일 로컬에 데이터가 없다면 다운로드까지 한번에 수행합니다.
한편 `corpus`는 말뭉치별로 그 내용과 구조가 다릅니다.
데이터 내용과 구조에 관해서는 이 페이지의 각 말뭉치 설명 란을 참고하세요.


## 터미널에서 사용하기

`Korpora`는 터미널에서도 동작합니다(Command Line Interface, CLI).
파이썬 콘솔 실행 없이 `Korpora`를 사용할 수 있습니다. 다음과 같습니다.
 

### 말뭉치 다운로드

터미널에서 KcBERT 학습데이터 하나를 다운받는 예제는 다음과 같습니다.

```bash
korpora fetch --corpus kcbert
```

```note
기본적으로 사용자의 로컬 컴퓨터 루트 하위의 Korpora라는 디렉토리에 말뭉치를 내려 받습니다(`~/Korpora`). 다른 경로에 말뭉치를 다운로드 받고 싶다면 
터미널에서 fetch 함수 실행시 `--root_dir custom_path`라는 인자를 추가하세요.
```

```tip
fetch 함수 실행시 `--force_download`라는 인자를 줄 경우 해당 말뭉치가 이미 로컬에 있더라도 이를 무시하고 다시 내려 받습니다.
```

터미널에서 KcBERT 학습데이터와 챗봇 문답 데이터 두 개를 동시에 다운로드 받는 예제는 다음과 같습니다.
이같은 방식으로 3개 이상의 데이터도 동시에 내려받을 수 있습니다.

```bash
korpora fetch --corpus kcbert korean_chatbot_data
```

터미널에서 `Korpora`가 제공하는 모든 말뭉치를 내려받는 예제는 다음과 같습니다.

```bash
korpora fetch --corpus all
```

```warning
국립국어원에서 제공하는 '모두의 말뭉치'와 AIHub 관련 데이터는 라이센스 문제로 `Korpora` 패키지에서는 다운로드 기능을 제공하지 않습니다. 
해당 말뭉치를 사용하고 싶다면 해당 기관의 안내대로 인증 과정을 거쳐 수작업으로 말뭉치를 내려받아야 합니다.
```


### 말뭉치를 전처리 하기

터미널에서 언어모델(Language Model) 학습용 데이터를 만들 수 있습니다. 
언어모델 학습용 데이터 구축이라고 함은, `Korpora`가 제공하는 코퍼스에서 문장만을 떼어서 텍스트 파일로 덤프하는 걸 가리킵니다. 
기본 예제 코드는 다음과 같습니다. 
다음 코드는 `Korpora`가 제공하는 모든 코퍼스(`all`)를 언어모델 학습용 말뭉치로 일괄 처리하는 역할을 합니다.
다운로드와 전처리를 동시에 수행합니다.
결과물은 `all.train`이라는 파일 하나입니다. 
`output_dir`에 생성됩니다.

```bash
korpora lmdata \
  --corpus all \
  --output_dir ~/works/lmdata
```

```warning
국립국어원에서 제공하는 '모두의 말뭉치'와 AIHub 관련 데이터는 라이센스 문제로 언어모델 학습데이터 처리 기능을 제공하지 않습니다.
```

몇 가지 인자(argument)로 추가 기능을 수행할 수 있습니다. 
각 인자의 역할 및 기본값은 다음과 같습니다.

- **corpus** : 언어모델용 데이터 구축 대상 말뭉치 이름. 코포라가 제공하는 말뭉치 목록은 [이곳](https://ko-nlp.github.io/Korpora/ko-docs/introduction/quicktour.html#%EB%A7%90%EB%AD%89%EC%B9%98-%EB%AA%A9%EB%A1%9D-%ED%99%95%EC%9D%B8)에서 확인 가능합니다. 기본값은 없습니다. 반드시 입력해야 합니다.
- **output_dir** : 언어모델용 데이터를 저장해둘 위치. 기본값은 없습니다. 반드시 입력해야 합니다.
- **sampling_ratio** : 말뭉치 원래 문장들 가운데 얼마나 샘플해서 데이터로 만들지 비율(0~1). 기본값은 1입니다.
- **n_first_samples** : 말뭉치에서 몇 번째 인스턴스까지 처리할지 갯수. 기본값은 해당 말뭉치의 인스턴스 갯수입니다.
- **min_length** : 음절 수 기준 최소 길이. 이보다 짧은 문장은 처리에서 제외합니다. 기본값은 None(최소 길이 제외 처리 안함)입니다.
- **max_length** : 음절 수 기준 최대 길이. 이보다 긴 문장은 처리에서 제외합니다. 기본값은 None(최대 길이 제외 처리 안함)입니다.
- **seed** : 랜덤 시드값. 샘플링을 하기 위해 쓰입니다. 기본값은 None(시드 없음)입니다.
- **root_dir** : 코포라가 제공하는 말뭉치를 내려받는 경로의 루트 위치. 기본값은 `/root/Korpora`입니다.
- **force_download** : 말뭉치를 강제로 내려받는지 여부. `False`이고 `root_dir` 이하에 관련 말뭉치가 이미 있다면 다운로드를 스킵합니다. `True`라면 존재 여부 관계없이 다시 내려받습니다. 기본값은 `False`입니다.
- **multilingual** : 외국어 말뭉치를 섞어서 데이터를 만들지 여부. 기본값은 `False`입니다.
- **save_each** : 처리한 데이터를 코포라가 제공하는 말뭉치별로 따로 저장할지 여부. `False`일 경우 `all.train`이라는 파일 하나로 덤프합니다. 기본값은 `False`입니다.
