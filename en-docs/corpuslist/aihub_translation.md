---
sort: 20
---

# AI Hub Ko-En Parallel Corpus

AI Hub Ko-En Parallel Corpus is the data released by AI Hub.
Data specification is as follows:

- author: AI Hub
- repository: [https://aihub.or.kr/aidata/87](https://aihub.or.kr/aidata/87)
- references: [document](https://aihub.or.kr/sites/default/files/dataGuideline/01.%20%ED%95%9C%EC%98%81%20%EB%B2%88%EC%97%AD%20%EB%A7%90%EB%AD%89%EC%B9%98%20AI%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EA%B5%AC%EC%B6%95%20%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8.pdf)
- size:

| Data | Property | Volume |
| --- | --- | --- |
| Spoken language | train | 400,000 |
| Conversation | train | 100,000 |
| News | train | 801,387 |
| Korean culture | train | 100,646 |
| Decree | train | 100,298 |
| Government website | train | 100,087 |
| TOTAL | train | 1,602,418 |

```warning
Due to the license issue, in `Korpora' package, only the loading is provided for AI Hub Ko-En Parallel Corpus, not the downloading.
If you want to use the corpus, it should be downloaded manually from [AI Hub](https://www.aihub.or.kr), guided by the verification process.
Also, the translation data from AI Hub is in the file format of compressed or excel (.xlsx).
If the files are unzipped, the names are in Hangul, the letter for the Korean language.
Hangul in the file names might incur unexpected problems depending on the operating systems.
Thus, in `Korpora`, it is assumed that the corpus is downloaded and all the file names are modified to Latin alphabet as below.

| Hangul file name | Latin alphabet file name |
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

## Reading the whole data at once

The example script for reading the whole AI Hub Ko-En Parallel Corpus in Python console is as follows:

```python
from Korpora import Korpora
corpus = Korpora.load("aihub_translation")
```

```warning
The code above operates given the corpus is present unzipped in `~/Korpora/AIHub_translation`.
If the root directory differs from `~/Korpora`, please add `root_dir=custom_path` as you call `load` function.
```

You can also read AI Hub Ko-En Parallel Corpus as below;
the result is the same as the above operation.

```python
from Korpora import AIHubTranslationKorpus
corpus = AIHubTranslationKorpus()
```

```warning
The code above operates given the corpus is present unzipped in the directory `~/Korpora/AIHub_translation` which is under the user's local computer root.
If the corpus exists in other directory, please add `root_dir_or_paths=custom_path` as you declare the class `AIHubTranslationKorpus`.
```

Select and execute one between the above two codes, and the copus is assigned to the variable `corpus`.
`train` denotes the train data of AI Hub Ko-En Parallel Corpus, and you can check the first instance as:

```
>>> corpus.train[0]
SentencePair(text="'Bible Coloring'은 성경의 아름다운 이야기를 체험 할 수 있는 컬러링 앱입니다.", pair="Bible Coloring' is a coloring application that allows you to experience beautiful stories in the Bible.")
>>> corpus.train[0].text
'Bible Coloring'은 성경의 아름다운 이야기를 체험 할 수 있는 컬러링 앱입니다.
>>> corpus.train[0].pair
Bible Coloring' is a coloring application that allows you to experience beautiful stories in the Bible.
```

## Reading only Spoken language data

The example script for reading Spoken language data from AI Hub Ko-En Parallel Corpus in Python console is as follows:

```python
from Korpora import Korpora
corpus = Korpora.load("aihub_spoken_translation")
```

```warning
The code above operates given the corpus is present unzipped in `~/Korpora/AIHub_translation`.
If the root directory differs from `~/Korpora`, please add `root_dir=custom_path` as you call `load` function.
```

You can also read Spoken language data from AI Hub Ko-En Parallel Corpus as below;
the result is the same as the above operation.

```python
from Korpora import AIHubSpokenTranslationKorpus
corpus = AIHubSpokenTranslationKorpus()
```

```warning
The code above operates given the corpus is present unzipped in the directory `~/Korpora/AIHub_translation` which is under the user's local computer root.
If the corpus exists in other directory, please add `root_dir_or_paths=custom_path` as you declare the class `AIHubSpokenTranslationKorpus`.
```

Select and execute one between the above two codes, and the copus is assigned to the variable `corpus`.
`train` denotes the train data of Spoken language data from AI Hub Ko-En Parallel Corpus, and you can check the first instance as:

```
>>> corpus.train[0]
SentencePair(text="'Bible Coloring'은 성경의 아름다운 이야기를 체험 할 수 있는 컬러링 앱입니다.", pair="Bible Coloring' is a coloring application that allows you to experience beautiful stories in the Bible.")
>>> corpus.train[0].text
'Bible Coloring'은 성경의 아름다운 이야기를 체험 할 수 있는 컬러링 앱입니다.
>>> corpus.train[0].pair
Bible Coloring' is a coloring application that allows you to experience beautiful stories in the Bible.
```

## Reading only Conversation data

The example script for reading Conversation data from AI Hub Ko-En Parallel Corpus in Python console is as follows:

```python
from Korpora import Korpora
corpus = Korpora.load("aihub_conversation_translation")
```

```warning
The code above operates given the corpus is present unzipped in `~/Korpora/AIHub_translation`.
If the root directory differs from `~/Korpora`, please add `root_dir=custom_path` as you call `load` function.
```

You can also read Conversation data from AI Hub Ko-En Parallel Corpus as below;
the result is the same as the above operation.

```python
from Korpora import AIHubConversationTranslationKorpus
corpus = AIHubConversationTranslationKorpus()
```

```warning
The code above operates given the corpus is present unzipped in the directory `~/Korpora/AIHub_translation` which is under the user's local computer root.
If the corpus exists in other directory, please add `root_dir_or_paths=custom_path` as you declare the class `AIHubConversationTranslationKorpus`.
```

Select and execute one between the above two codes, and the copus is assigned to the variable `corpus`.
`train` denotes the train data of Conversation data from AI Hub Ko-En Parallel Corpus, and you can check the first instance as:

```
>>> corpus.train[0]
SentencePair(text='이번 신제품 출시에 대한 시장의 반응은 어떤가요?', pair="How is the market's reaction to the newly released product?")
>>> corpus.train[0].text
번 신제품 출시에 대한 시장의 반응은 어떤가요?
>>> corpus.train[0].pair
How is the market's reaction to the newly released product?
```


## Reading only News data

The example script for reading News data from AI Hub Ko-En Parallel Corpus in Python console is as follows:

```python
from Korpora import Korpora
corpus = Korpora.load("aihub_news_translation")
```

```warning
The code above operates given the corpus is present unzipped in `~/Korpora/AIHub_translation`.
If the root directory differs from `~/Korpora`, please add `root_dir=custom_path` as you call `load` function.
```

You can also read News data from AI Hub Ko-En Parallel Corpus as below;
the result is the same as the above operation.

```python
from Korpora import AIHubNewsTranslationKorpus
corpus = AIHubNewsTranslationKorpus()
```

```warning
The code above operates given the corpus is present unzipped in the directory `~/Korpora/AIHub_translation` which is under the user's local computer root.
If the corpus exists in other directory, please add `root_dir_or_paths=custom_path` as you declare the class `AIHubNewsTranslationKorpus`.
```

Select and execute one between the above two codes, and the copus is assigned to the variable `corpus`.
`train` denotes the train data of News data from AI Hub Ko-En Parallel Corpus, and you can check the first instance as:

```
>>> corpus.train[0]
SentencePair(text='스키너가 말한 보상은 대부분 눈으로 볼 수 있는 현물이다.', pair="Skinner's reward is mostly eye-watering.")
>>> corpus.train[0].text
스키너가 말한 보상은 대부분 눈으로 볼 수 있는 현물이다.
>>> corpus.train[0].pair
Skinner's reward is mostly eye-watering.
```


## Reading only Korean culture data

The example script for reading Korean culture data from AI Hub Ko-En Parallel Corpus in Python console is as follows:

```python
from Korpora import Korpora
corpus = Korpora.load("aihub_korean_culture_translation")
```

```warning
The code above operates given the corpus is present unzipped in `~/Korpora/AIHub_translation`.
If the root directory differs from `~/Korpora`, please add `root_dir=custom_path` as you call `load` function.
```

You can also read Korean culture data from AI Hub Ko-En Parallel Corpus as below;
the result is the same as the above operation.

```python
from Korpora import AIHubKoreanCultureTranslationKorpus
corpus = AIHubKoreanCultureTranslationKorpus()
```

```warning
The code above operates given the corpus is present unzipped in the directory `~/Korpora/AIHub_translation` which is under the user's local computer root.
If the corpus exists in other directory, please add `root_dir_or_paths=custom_path` as you declare the class `AIHubKoreanCultureTranslationKorpus`.
```

Select and execute one between the above two codes, and the copus is assigned to the variable `corpus`.
`train` denotes the train data of Korean culture data from AI Hub Ko-En Parallel Corpus, and you can check the first instance as:

```
>>> corpus.train[0]
SentencePair(text='강릉 기생 매화가 등장하는 판소리 열두마당의 하나인 「강릉매화전」은 판소리 특유의 해학이 담겨져 있기도 하다.', pair="<Gangneung Maehwajeon>, one of the twelve madang of pansori that Gangneung's gisaeng Maehwa appears, also contains a unique humor of pansori.")
>>> corpus.train[0].text
강릉 기생 매화가 등장하는 판소리 열두마당의 하나인 「강릉매화전」은 판소리 특유의 해학이 담겨져 있기도 하다.
>>> corpus.train[0].pair
<Gangneung Maehwajeon>, one of the twelve madang of pansori that Gangneung's gisaeng Maehwa appears, also contains a unique humor of pansori.
```


## Reading only Decree data

The example script for reading Decree data from AI Hub Ko-En Parallel Corpus in Python console is as follows:

```python
from Korpora import Korpora
corpus = Korpora.load("aihub_decree_translation")
```

```warning
The code above operates given the corpus is present unzipped in `~/Korpora/AIHub_translation`.
If the root directory differs from `~/Korpora`, please add `root_dir=custom_path` as you call `load` function.
```

You can also read Decree data from AI Hub Ko-En Parallel Corpus as below;
the result is the same as the above operation.

```python
from Korpora import AIHubDecreeTranslationKorpus
corpus = AIHubDecreeTranslationKorpus()
```

```warning
The code above operates given the corpus is present unzipped in the directory `~/Korpora/AIHub_translation` which is under the user's local computer root.
If the corpus exists in other directory, please add `root_dir_or_paths=custom_path` as you declare the class `AIHubDecreeTranslationKorpus`.
```

Select and execute one between the above two codes, and the copus is assigned to the variable `corpus`.
`train` denotes the train data of Decree data from AI Hub Ko-En Parallel Corpus, and you can check the first instance as:

```
>>> corpus.train[0]
SentencePair(text='의원의 회의규칙 제47조제1항', pair="Article 47(1) of the Members' Meeting Rules")
>>> corpus.train[0].text
의원의 회의규칙 제47조제1항
>>> corpus.train[0].pair
Article 47(1) of the Members' Meeting Rules
```


## Reading only Government website data

The example script for reading Government website data from AI Hub Ko-En Parallel Corpus in Python console is as follows:

```python
from Korpora import Korpora
corpus = Korpora.load("aihub_government_website_translation")
```

```warning
The code above operates given the corpus is present unzipped in `~/Korpora/AIHub_translation`.
If the root directory differs from `~/Korpora`, please add `root_dir=custom_path` as you call `load` function.
```

You can also read Government website data from AI Hub Ko-En Parallel Corpus as below;
the result is the same as the above operation.

```python
from Korpora import AIHubGovernmentWebsiteTranslationKorpus
corpus = AIHubGovernmentWebsiteTranslationKorpus()
```

```warning
The code above operates given the corpus is present unzipped in the directory `~/Korpora/AIHub_translation` which is under the user's local computer root.
If the corpus exists in other directory, please add `root_dir_or_paths=custom_path` as you declare the class `AIHubGovernmentWebsiteTranslationKorpus`.
```

Select and execute one between the above two codes, and the copus is assigned to the variable `corpus`.
`train` denotes the train data of Government website data from AI Hub Ko-En Parallel Corpus, and you can check the first instance as:

```
>>> corpus.train[0]
SentencePair(text='"경기도가 말산업 육성을 위해 총예산 245,193천원으로 2013년 경기도 용인시 남사면 소재의 축산위생연구소 가축연구팀 부지에 경기도말시험사육장을 신축하고, 올해 2월 승용마 8두를 입식하여 본격적인 승용마 시험 연구에 돌입하였다고 밝혔다."', pair='"The Gyeonggi provincial government announced that it has established a Gyeonggi-do test farm on the site of the livestock research team of livestock sanitation Institute in Namsa-myeon, Yongin, Gyeonggji province in 2013 with a total budget of 245 million and 193 thousand won to foster the horse industry, and that it has begun full-fledged testing of eight riding horses in February this year."')
>>> corpus.train[0].text
"경기도가 말산업 육성을 위해 총예산 245,193천원으로 2013년 경기도 용인시 남사면 소재의 축산위생연구소 가축연구팀 부지에 경기도말시험사육장을 신축하고, 올해 2월 승용마 8두를 입식하여 본격적인 승용마 시험 연구에 돌입하였다고 밝혔다."
>>> corpus.train[0].pair
"The Gyeonggi provincial government announced that it has established a Gyeonggi-do test farm on the site of the livestock research team of livestock sanitation Institute in Namsa-myeon, Yongin, Gyeonggji province in 2013 with a total budget of 245 million and 193 thousand won to foster the horse industry, and that it has begun full-fledged testing of eight riding horses in February this year."
```

