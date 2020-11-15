---
sort: 13
---

# 모두의 말뭉치: 신문

모두의 말뭉치(신문)는 국립국어원이 공개한 데이터입니다.
데이터 정보는 다음과 같습니다.

- author: 국립국어원
- repository: [https://corpus.korean.go.kr](https://corpus.korean.go.kr)
- references: [document](https://rlkujwkk7.toastcdn.net/NIKL_NEWSPAPER(v1.0).pdf)
- size:
  - train: about 3,500,000 examples

데이터 구조는 다음과 같습니다.

| 속성명 | 내용 |
| --- | --- |
| document_id | 뉴스 고유 아이디 |
| title | metadata 의 title (기사 제목이 아님) |
| author | 기사 작성자 |
| publisher | 언론사 |
| date | 기사 작성 일자 |
| topic | 통합 분류 ((정치, 경제, 사회, 생활, IT/과학, 연예, 스포츠, 문화, 미용/건강) |
| original_topic | 신문 매체의 자체 주제 분류 |
| paragraph | 뉴스 기사 본문 (첫 줄이 기사의 제목으로 추정) |

```warning
국립국어원에서 제공하는 '모두의 말뭉치'는 라이센스 문제로 `Korpora` 패키지에서는 다운로드 기능을 제공하지 않고 로드 기능만 제공합니다. 
해당 말뭉치를 사용하고 싶다면 국립국어원 안내대로 인증 과정을 거쳐 수작업으로 말뭉치를 내려받아야 합니다. 
```

모두의 말뭉치(신문)를 파이썬 콘솔에서 읽어들이는 예제는 다음과 같습니다.

```python
from Korpora import Korpora
corpus = Korpora.load("modu_news")
```

```warning
위의 코드는 해당 말뭉치가 루트 디렉토리 하위의 `NIKL_NEWSPAPER`에 압축이 해제된 상태로 존재하는 걸 전제로 작동합니다.
루트 디렉토리의 기본값은 `~/Korpora`입니다. 
만일 루트 다렉토리를 바꾸고 싶다면 `load` 함수 호출시 `root_dir=custom_path` 인자를 추가하시기 바랍니다.
```

다음과 같이 실행해도 모두의 말뭉치(신문)를 읽어들일 수 있습니다.
수행 결과는 위의 코드와 동일합니다.

```python
from Korpora import ModuNewsKorpus
corpus = ModuNewsKorpus()
```

```warning
위의 코드는 해당 말뭉치가 `~/Korpora/NIKL_NEWSPAPER` 디렉토리에 압축이 해제된 상태로 존재하는 걸 전제로 작동합니다. 
만일 다른 디렉토리에 말뭉치가 존재한다면 `ModuNewsKorpus` 클래스 선언시 `root_dir=custom_path` 인자를 추가하시기 바랍니다.
```

```tip
`load_light=True`이면 기사 본문과 제목, document_id만 읽어들입니다. `False`라면 모든 메타 정보를 읽습니다. 기본값은 `True`입니다.
```

위 코드 둘 중 하나를 택해 실행하면 `corpus`라는 변수에 말뭉치를 로드합니다.
`train`은 모두의 말뭉치(신문)의 train 데이터로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
>>> corpus.train[0]
ModuNews(document_id='NPRW1900000010.1', title='한국경제 2018년 기사', author='김현석', publisher='한국경제신문사', date='20180101', topic='생활', original_topic='국제', paragraph=['"라니냐로 겨울 가뭄 온다"…', '...'])
```

`get_all_texts`라는 메소드를 실행하면 모두의 말뭉치(신문)의 모든 text(뉴스 본문)를 확인할 수 있습니다.

```
>>> corpus.get_all_texts()
[''"라니냐로 겨울 가뭄 온다"...', ... ]
```
