---
sort: 18
---

# 모두의 말뭉치: 웹 

모두의 말뭉치(웹)는 국립국어원이 공개한 데이터입니다.
데이터 정보는 다음과 같습니다.

- author: 국립국어원
- repository: [https://corpus.korean.go.kr](https://corpus.korean.go.kr)
- references: [document](https://rlkujwkk7.toastcdn.net/NIKL_WEB(v1.0).pdf)
- size:
  - train: 2,107,076 examples

```warning
국립국어원에서 제공하는 '모두의 말뭉치'는 라이센스 문제로 `Korpora` 패키지에서는 다운로드 기능을 제공하지 않고 로드 기능만 제공합니다. 
해당 말뭉치를 사용하고 싶다면 국립국어원 안내대로 인증 과정을 거쳐 수작업으로 말뭉치를 내려받아야 합니다. 
```

모두의 말뭉치(형태 분석)를 파이썬 콘솔에서 읽어들이는 예제는 다음과 같습니다.

```python
from Korpora import Korpora
corpus = Korpora.load("modu_web")
```

```warning
위의 코드는 해당 말뭉치가 `~/Korpora` 아래에 NIKL_WEB이라는 디렉토리(`~/Korpora/NIKL_WEB`)에 압축이 해제된 상태로 존재하는 걸 전제로 작동합니다. 
만일 루트 다렉토리가 `~/Korpora`와 다를 경우 `load` 함수 호출시 `root_dir=custom_path` 인자를 추가하시기 바랍니다.
```

다음과 같이 실행해도 모두의 말뭉치(웹)를 읽어들일 수 있습니다.
수행 결과는 위의 코드와 동일합니다.

```python
from Korpora import ModuWebKorpus
corpus = ModuWebKorpus()
```

```warning
위의 코드는 해당 말뭉치가 사용자의 로컬 컴퓨터 루트 하위의 `~/Korpora/NIKL_WEB` 디렉토리에 압축이 해제된 상태로 존재하는 걸 전제로 작동합니다. 
만일 다른 디렉토리에 말뭉치가 존재한다면 `ModuWebKorpus` 클래스 선언시 `root_dir=custom_path` 인자를 추가하시기 바랍니다.
```

위 코드 둘 중 하나를 택해 실행하면 `corpus`라는 변수에 말뭉치를 로드합니다.
`train`은 모두의 말뭉치(웹)의 train 데이터로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
>>> corpus.train[0]
오메가3와 비타민C, 달맞이꽃종자유 등을 사려고 몇 시간을 검색하며 공부했다 ...
```
