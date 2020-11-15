---
sort: 14
---

# 모두의 말뭉치: 메신저

모두의 말뭉치(메신저)는 국립국어원이 공개한 데이터입니다.
데이터 정보는 다음과 같습니다.

- author: 국립국어원
- repository: [https://corpus.korean.go.kr](https://corpus.korean.go.kr)
- references: [document](https://rlkujwkk7.toastcdn.net/NIKL_MESSENGER(v1.0).pdf)
- size:
  - train: 4,203 examples

데이터 구조는 다음과 같습니다.

| 속성명 | 내용 |
| --- | --- |
| document_id | 대화 고유 아이디 |
| form | 대화 텍스트 |
| original_form | 대화 원본 텍스트 |
| speaker_id | 발화자 (숫자가 아님) |
| time | `yyyymmdd hh:mm` 형식 |

```warning
국립국어원에서 제공하는 '모두의 말뭉치'는 라이센스 문제로 `Korpora` 패키지에서는 다운로드 기능을 제공하지 않고 로드 기능만 제공합니다. 
해당 말뭉치를 사용하고 싶다면 국립국어원 안내대로 인증 과정을 거쳐 수작업으로 말뭉치를 내려받아야 합니다. 
```

모두의 말뭉치(메신저)를 파이썬 콘솔에서 읽어들이는 예제는 다음과 같습니다.

```python
from Korpora import Korpora
corpus = Korpora.load("modu_messenger")
```

```warning
위의 코드는 해당 말뭉치가 `~/Korpora/NIKL_MESSENGER`에 압축이 해제된 상태로 존재하는 걸 전제로 작동합니다. 
루트 디렉토리의 기본값은 `~/Korpora`입니다. 
만일 루트 다렉토리를 바꾸고 싶다면 `load` 함수 호출시 `root_dir=custom_path` 인자를 추가하시기 바랍니다.
```

다음과 같이 실행해도 모두의 말뭉치(메신저)를 읽어들일 수 있습니다.
수행 결과는 위의 코드와 동일합니다.

```python
from Korpora import ModuMessengerKorpus
corpus = ModuMessengerKorpus()
```

```warning
위의 코드는 해당 말뭉치가 `~/Korpora/NIKL_MESSENGER` 디렉토리에 압축이 해제된 상태로 존재하는 걸 전제로 작동합니다. 
만일 다른 디렉토리에 말뭉치가 존재한다면 `ModuMessengerKorpus` 클래스 선언시 `root_dir=custom_path` 인자를 추가하시기 바랍니다.
```

위 코드 둘 중 하나를 택해 실행하면 `corpus`라는 변수에 말뭉치를 로드합니다.
`train`은 모두의 말뭉치(메신저)의 train 데이터로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
>>> corpus.train[0]
Conversation(id=MDRW1900000002.1, len=70, attributes=(form(str), original_form(str), speaker_id(str), time(str)))
>>> corpus.train[0].form
('누나 모해??', 'ㅋㅋㅋㅋ 일하고 있지ㅠㅠ', ... )
>>> corpus.train[0].speaker_id
('1', '2', ... )
```
