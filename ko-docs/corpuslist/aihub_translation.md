---
sort: 20
---

# AI Hub 한국어-영어 번역 말뭉치

AI Hub 한국어-영어 번역 말뭉치는 AI Hub가 공개한 데이터입니다.
데이터 정보는 다음과 같습니다.

- author: AI Hub
- repository: [https://aihub.or.kr/aidata/87](https://aihub.or.kr/aidata/87)
- references: [document](https://aihub.or.kr/sites/default/files/dataGuideline/01.%20%ED%95%9C%EC%98%81%20%EB%B2%88%EC%97%AD%20%EB%A7%90%EB%AD%89%EC%B9%98%20AI%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EA%B5%AC%EC%B6%95%20%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8.pdf)
- size:

| 데이터 종류 | 속성 | 데이터 갯수 |
| --- | --- | --- |
| 구어(spoken) | train | 400,000 |
| 대화(conversation) | train | 100,000 |
| 뉴스(news) | train | 801,387 |
| 한국 문화(Korean culture) | train | 100,646 |
| 조례(decree) | train | 100,298 |
| 지자체웹사이트(government website) | train | 100,087 |
| TOTAL | train | 1,602,418 |

```warning
AI Hub 한국어-영어 번역 말뭉치는 라이센스 문제로 `Korpora` 패키지에서는 다운로드 기능을 제공하지 않고 로드 기능만 제공합니다. 
해당 말뭉치를 사용하고 싶다면 [AI Hub](https://www.aihub.or.kr) 안내대로 인증 과정을 거쳐 수작업으로 말뭉치를 내려받아야 합니다. 
한편 AI Hub 에서 제공하는 번역데이터는 압축파일 또는 엑셀파일 (확장자: xlsx) 형식입니다. 
압축 해제 시 파일 이름이 한글로 되어 있습니다. 
파일 이름을 한글로 기록할 경우 OS에 따라 예상치 못한 문제들이 발생할 수 있습니다. 
`Korpora` 패키지에서는 말뭉치를 다운로드 받은 뒤 각 파일의 이름을 아래처럼 영어로 변경하였다고 가정합니다.

| 한글 파일 이름 | 영어 파일 이름 |
| --- | --- |
| 1_구어체(1)_200226.xlsx | 1_spoken(1)_200226.xlsx |
| 1_구어체(2)_200226.xlsx | 1_spoken(2)_200226.xlsx |
| 2_대화체_200226.xlsx | 2_conversation_200226.xlsx |
| 3_문어체_뉴스(1)_200226.xlsx | 3_news(1)_200226.xlsx |
| 3_문어체_뉴스(2)_200226.xlsx | 3_news(2)_200226.xlsx |
| 3_문어체_뉴스(3)_200226.xlsx | 3_news(3)_200226.xlsx |
| 3_문어체_뉴스(4)_200226.xlsx | 3_news(4)_200226.xlsx |
| 4_문어체_한국문화_200226.xlsx | 4_korean_culture_200226.xlsx |
| 5_문어체_조례_200226.xlsx | 5_decree_200226.xlsx |
| 6_문어체_지자체웹사이트_200226.xlsx | 6_government_website_200226.xlsx |
```

## 전체 데이터를 한번에 모두 읽기

AI Hub 한국어-영어 번역 말뭉치 전체를 파이썬 콘솔에서 읽어들이는 예제는 다음과 같습니다.

```python
from Korpora import Korpora
corpus = Korpora.load("aihub_translation")
```

```warning
위의 코드 예제는 해당 말뭉치가 `~/Korpora/AIHub_translation`에 압축이 해제된 상태로 존재하는 걸 전제로 작동합니다. 
만일 루트 다렉토리가 `~/Korpora`와 다를 경우 `load` 함수 호출시 `root_dir=custom_path` 인자를 추가하시기 바랍니다.
```

다음과 같이 실행해도 AI Hub 한국어-영어 번역 말뭉치 전체를 읽어들일 수 있습니다.
수행 결과는 위의 코드와 동일합니다.

```python
from Korpora import AIHubTranslationKorpus
corpus = AIHubTranslationKorpus()
```

```warning
위의 코드는 해당 말뭉치가 사용자의 로컬 컴퓨터 루트 하위의 `~/Korpora/AIHub_translation` 디렉토리에 압축이 해제된 상태로 존재하는 걸 전제로 작동합니다. 
만일 다른 디렉토리에 말뭉치가 존재한다면 `AIHubTranslationKorpus` 클래스 선언시 `root_dir=custom_path` 인자를 추가하시기 바랍니다.
```

위 코드 둘 중 하나를 택해 실행하면 `corpus`라는 변수에 말뭉치를 로드합니다.
`train`은 AI Hub 한국어-영어 번역 말뭉치의 train 데이터로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
>>> corpus.train[0]
SentencePair(text="'Bible Coloring'은 성경의 아름다운 이야기를 체험 할 수 있는 컬러링 앱입니다.", pair="Bible Coloring' is a coloring application that allows you to experience beautiful stories in the Bible.")
>>> corpus.train[0].text
'Bible Coloring'은 성경의 아름다운 이야기를 체험 할 수 있는 컬러링 앱입니다.
>>> corpus.train[0].pair
Bible Coloring' is a coloring application that allows you to experience beautiful stories in the Bible.
```

## 구어 데이터만 읽기

AI Hub 한국어-영어 번역 말뭉치 가운데 구어 데이터를 파이썬 콘솔에서 읽어들이는 예제는 다음과 같습니다.

```python
from Korpora import Korpora
corpus = Korpora.load("aihub_spoken_translation")
```

```warning
위의 코드 예제는 해당 말뭉치가 `~/Korpora/AIHub_translation`에 압축이 해제된 상태로 존재하는 걸 전제로 작동합니다. 
만일 루트 다렉토리가 `~/Korpora`와 다를 경우 `load` 함수 호출시 `root_dir=custom_path` 인자를 추가하시기 바랍니다.
```

다음과 같이 실행해도 AI Hub 한국어-영어 번역 말뭉치 가운데 구어 데이터를 읽어들일 수 있습니다.
수행 결과는 위의 코드와 동일합니다.

```python
from Korpora import AIHubSpokenTranslationKorpus
corpus = AIHubSpokenTranslationKorpus()
```

```warning
위의 코드는 해당 말뭉치가 사용자의 로컬 컴퓨터 루트 하위의 `~/Korpora/AIHub_translation` 디렉토리에 압축이 해제된 상태로 존재하는 걸 전제로 작동합니다. 
만일 다른 디렉토리에 말뭉치가 존재한다면 `AIHubSpokenTranslationKorpus` 클래스 선언시 `root_dir=custom_path` 인자를 추가하시기 바랍니다.
```

위 코드 둘 중 하나를 택해 실행하면 `corpus`라는 변수에 말뭉치를 로드합니다.
`train`은 AI Hub 한국어-영어 번역 말뭉치 가운데 구어 데이터의 train으로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
>>> corpus.train[0]
SentencePair(text="'Bible Coloring'은 성경의 아름다운 이야기를 체험 할 수 있는 컬러링 앱입니다.", pair="Bible Coloring' is a coloring application that allows you to experience beautiful stories in the Bible.")
>>> corpus.train[0].text
'Bible Coloring'은 성경의 아름다운 이야기를 체험 할 수 있는 컬러링 앱입니다.
>>> corpus.train[0].pair
Bible Coloring' is a coloring application that allows you to experience beautiful stories in the Bible.
```

## 대화 데이터만 읽기

AI Hub 한국어-영어 번역 말뭉치 가운데 대화 데이터를 파이썬 콘솔에서 읽어들이는 예제는 다음과 같습니다.

```python
from Korpora import Korpora
corpus = Korpora.load("aihub_conversation_translation")
```

```warning
위의 코드 예제는 해당 말뭉치가 `~/Korpora/AIHub_translation`에 압축이 해제된 상태로 존재하는 걸 전제로 작동합니다. 
만일 루트 다렉토리가 `~/Korpora`와 다를 경우 `load` 함수 호출시 `root_dir=custom_path` 인자를 추가하시기 바랍니다.
```

다음과 같이 실행해도 AI Hub 한국어-영어 번역 말뭉치 가운데 대화 데이터를 읽어들일 수 있습니다.
수행 결과는 위의 코드와 동일합니다.

```python
from Korpora import AIHubConversationTranslationKorpus
corpus = AIHubConversationTranslationKorpus()
```

```warning
위의 코드는 해당 말뭉치가 사용자의 로컬 컴퓨터 루트 하위의 `~/Korpora/AIHub_translation` 디렉토리에 압축이 해제된 상태로 존재하는 걸 전제로 작동합니다. 
만일 다른 디렉토리에 말뭉치가 존재한다면 `AIHubConversationTranslationKorpus` 클래스 선언시 `root_dir=custom_path` 인자를 추가하시기 바랍니다.
```

위 코드 둘 중 하나를 택해 실행하면 `corpus`라는 변수에 말뭉치를 로드합니다.
`train`은 AI Hub 한국어-영어 번역 말뭉치 가운데 대화 데이터의 train으로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
>>> corpus.train[0]
SentencePair(text='이번 신제품 출시에 대한 시장의 반응은 어떤가요?', pair="How is the market's reaction to the newly released product?")
>>> corpus.train[0].text
번 신제품 출시에 대한 시장의 반응은 어떤가요?
>>> corpus.train[0].pair
How is the market's reaction to the newly released product?
```


## 뉴스 데이터만 읽기

AI Hub 한국어-영어 번역 말뭉치 가운데 뉴스 데이터를 파이썬 콘솔에서 읽어들이는 예제는 다음과 같습니다.

```python
from Korpora import Korpora
corpus = Korpora.load("aihub_news_translation")
```

```warning
위의 코드 예제는 해당 말뭉치가 `~/Korpora/AIHub_translation`에 압축이 해제된 상태로 존재하는 걸 전제로 작동합니다. 
만일 루트 다렉토리가 `~/Korpora`와 다를 경우 `load` 함수 호출시 `root_dir=custom_path` 인자를 추가하시기 바랍니다.
```

다음과 같이 실행해도 AI Hub 한국어-영어 번역 말뭉치 가운데 뉴스 데이터를 읽어들일 수 있습니다.
수행 결과는 위의 코드와 동일합니다.

```python
from Korpora import AIHubNewsTranslationKorpus
corpus = AIHubNewsTranslationKorpus()
```

```warning
위의 코드는 해당 말뭉치가 사용자의 로컬 컴퓨터 루트 하위의 `~/Korpora/AIHub_translation` 디렉토리에 압축이 해제된 상태로 존재하는 걸 전제로 작동합니다. 
만일 다른 디렉토리에 말뭉치가 존재한다면 `AIHubNewsTranslationKorpus` 클래스 선언시 `root_dir=custom_path` 인자를 추가하시기 바랍니다.
```

위 코드 둘 중 하나를 택해 실행하면 `corpus`라는 변수에 말뭉치를 로드합니다.
`train`은 AI Hub 한국어-영어 번역 말뭉치 가운데 뉴스 데이터의 train으로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
>>> corpus.train[0]
SentencePair(text='스키너가 말한 보상은 대부분 눈으로 볼 수 있는 현물이다.', pair="Skinner's reward is mostly eye-watering.")
>>> corpus.train[0].text
스키너가 말한 보상은 대부분 눈으로 볼 수 있는 현물이다.
>>> corpus.train[0].pair
Skinner's reward is mostly eye-watering.
```


## 한국문화 데이터만 읽기

AI Hub 한국어-영어 번역 말뭉치 가운데 한국문화 데이터를 파이썬 콘솔에서 읽어들이는 예제는 다음과 같습니다.

```python
from Korpora import Korpora
corpus = Korpora.load("aihub_korean_culture_translation")
```

```warning
위의 코드 예제는 해당 말뭉치가 `~/Korpora/AIHub_translation`에 압축이 해제된 상태로 존재하는 걸 전제로 작동합니다. 
만일 루트 다렉토리가 `~/Korpora`와 다를 경우 `load` 함수 호출시 `root_dir=custom_path` 인자를 추가하시기 바랍니다.
```

다음과 같이 실행해도 AI Hub 한국어-영어 번역 말뭉치 가운데 한국문화 데이터를 읽어들일 수 있습니다.
수행 결과는 위의 코드와 동일합니다.

```python
from Korpora import AIHubKoreanCultureTranslationKorpus
corpus = AIHubKoreanCultureTranslationKorpus()
```

```warning
위의 코드는 해당 말뭉치가 사용자의 로컬 컴퓨터 루트 하위의 `~/Korpora/AIHub_translation` 디렉토리에 압축이 해제된 상태로 존재하는 걸 전제로 작동합니다. 
만일 다른 디렉토리에 말뭉치가 존재한다면 `AIHubKoreanCultureTranslationKorpus` 클래스 선언시 `root_dir=custom_path` 인자를 추가하시기 바랍니다.
```

위 코드 둘 중 하나를 택해 실행하면 `corpus`라는 변수에 말뭉치를 로드합니다.
`train`은 AI Hub 한국어-영어 번역 말뭉치 가운데 한국문화 데이터의 train으로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
>>> corpus.train[0]
SentencePair(text='강릉 기생 매화가 등장하는 판소리 열두마당의 하나인 「강릉매화전」은 판소리 특유의 해학이 담겨져 있기도 하다.', pair="<Gangneung Maehwajeon>, one of the twelve madang of pansori that Gangneung's gisaeng Maehwa appears, also contains a unique humor of pansori.")
>>> corpus.train[0].text
강릉 기생 매화가 등장하는 판소리 열두마당의 하나인 「강릉매화전」은 판소리 특유의 해학이 담겨져 있기도 하다.
>>> corpus.train[0].pair
<Gangneung Maehwajeon>, one of the twelve madang of pansori that Gangneung's gisaeng Maehwa appears, also contains a unique humor of pansori.
```


## 조례 데이터만 읽기

AI Hub 한국어-영어 번역 말뭉치 가운데 조례 데이터를 파이썬 콘솔에서 읽어들이는 예제는 다음과 같습니다.

```python
from Korpora import Korpora
corpus = Korpora.load("aihub_decree_translation")
```

```warning
위의 코드 예제는 해당 말뭉치가 `~/Korpora/AIHub_translation`에 압축이 해제된 상태로 존재하는 걸 전제로 작동합니다. 
만일 루트 다렉토리가 `~/Korpora`와 다를 경우 `load` 함수 호출시 `root_dir=custom_path` 인자를 추가하시기 바랍니다.
```

다음과 같이 실행해도 AI Hub 한국어-영어 번역 말뭉치 가운데 조례 데이터를 읽어들일 수 있습니다.
수행 결과는 위의 코드와 동일합니다.

```python
from Korpora import AIHubDecreeTranslationKorpus
corpus = AIHubDecreeTranslationKorpus()
```

```warning
위의 코드는 해당 말뭉치가 사용자의 로컬 컴퓨터 루트 하위의 `~/Korpora/AIHub_translation` 디렉토리에 압축이 해제된 상태로 존재하는 걸 전제로 작동합니다. 
만일 다른 디렉토리에 말뭉치가 존재한다면 `AIHubDecreeTranslationKorpus` 클래스 선언시 `root_dir=custom_path` 인자를 추가하시기 바랍니다.
```

위 코드 둘 중 하나를 택해 실행하면 `corpus`라는 변수에 말뭉치를 로드합니다.
`train`은 AI Hub 한국어-영어 번역 말뭉치 가운데 조례 데이터의 train으로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
>>> corpus.train[0]
SentencePair(text='의원의 회의규칙 제47조제1항', pair="Article 47(1) of the Members' Meeting Rules")
>>> corpus.train[0].text
의원의 회의규칙 제47조제1항
>>> corpus.train[0].pair
Article 47(1) of the Members' Meeting Rules
```


## 지자체웹사이트 데이터만 읽기

AI Hub 한국어-영어 번역 말뭉치 가운데 지자체웹사이트 데이터를 파이썬 콘솔에서 읽어들이는 예제는 다음과 같습니다.

```python
from Korpora import Korpora
corpus = Korpora.load("aihub_government_website_translation")
```

```warning
위의 코드 예제는 해당 말뭉치가 `~/Korpora/AIHub_translation`에 압축이 해제된 상태로 존재하는 걸 전제로 작동합니다. 
만일 루트 다렉토리가 `~/Korpora`와 다를 경우 `load` 함수 호출시 `root_dir=custom_path` 인자를 추가하시기 바랍니다.
```

다음과 같이 실행해도 AI Hub 한국어-영어 번역 말뭉치 가운데 지자체웹사이트 데이터를 읽어들일 수 있습니다.
수행 결과는 위의 코드와 동일합니다.

```python
from Korpora import AIHubGovernmentWebsiteTranslationKorpus
corpus = AIHubGovernmentWebsiteTranslationKorpus()
```

```warning
위의 코드는 해당 말뭉치가 사용자의 로컬 컴퓨터 루트 하위의 `~/Korpora/AIHub_translation` 디렉토리에 압축이 해제된 상태로 존재하는 걸 전제로 작동합니다. 
만일 다른 디렉토리에 말뭉치가 존재한다면 `AIHubGovernmentWebsiteTranslationKorpus` 클래스 선언시 `root_dir=custom_path` 인자를 추가하시기 바랍니다.
```

위 코드 둘 중 하나를 택해 실행하면 `corpus`라는 변수에 말뭉치를 로드합니다.
`train`은 AI Hub 한국어-영어 번역 말뭉치 가운데 지자체웹사이트 데이터의 train으로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
>>> corpus.train[0]
SentencePair(text='"경기도가 말산업 육성을 위해 총예산 245,193천원으로 2013년 경기도 용인시 남사면 소재의 축산위생연구소 가축연구팀 부지에 경기도말시험사육장을 신축하고, 올해 2월 승용마 8두를 입식하여 본격적인 승용마 시험 연구에 돌입하였다고 밝혔다."', pair='"The Gyeonggi provincial government announced that it has established a Gyeonggi-do test farm on the site of the livestock research team of livestock sanitation Institute in Namsa-myeon, Yongin, Gyeonggji province in 2013 with a total budget of 245 million and 193 thousand won to foster the horse industry, and that it has begun full-fledged testing of eight riding horses in February this year."')
>>> corpus.train[0].text
"경기도가 말산업 육성을 위해 총예산 245,193천원으로 2013년 경기도 용인시 남사면 소재의 축산위생연구소 가축연구팀 부지에 경기도말시험사육장을 신축하고, 올해 2월 승용마 8두를 입식하여 본격적인 승용마 시험 연구에 돌입하였다고 밝혔다."
>>> corpus.train[0].pair
"The Gyeonggi provincial government announced that it has established a Gyeonggi-do test farm on the site of the livestock research team of livestock sanitation Institute in Namsa-myeon, Yongin, Gyeonggji province in 2013 with a total budget of 245 million and 193 thousand won to foster the horse industry, and that it has begun full-fledged testing of eight riding horses in February this year."
```
