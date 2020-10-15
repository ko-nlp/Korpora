---
sort: 15
---

# 모두의 말뭉치: 형태 분석

모두의 말뭉치(형태 분석)는 국립국어원이 공개한 데이터입니다.
데이터 정보는 다음과 같습니다.

- author: 국립국어원
- repository: [https://corpus.korean.go.kr](https://corpus.korean.go.kr)
- references: [document](https://rlkujwkk7.toastcdn.net/NIKL_MP(v1.0).pdf)
- size:
  - train: 371,571 examples

```warning
국립국어원에서 제공하는 '모두의 말뭉치'는 라이센스 문제로 `Korpora` 패키지에서는 다운로드 기능을 제공하지 않고 로드 기능만 제공합니다. 
해당 말뭉치를 사용하고 싶다면 국립국어원 안내대로 인증 과정을 거쳐 수작업으로 말뭉치를 내려받아야 합니다. 
```

모두의 말뭉치(형태 분석)를 파이썬 콘솔에서 읽어들이는 예제는 다음과 같습니다.

```python
from Korpora import Korpora
corpus = Korpora.load("modu_mp")
```

```warning
위의 코드는 해당 말뭉치가 `~/Korpora` 아래에 NIKL_MP라는 디렉토리(`~/Korpora/NIKL_MP`)에 압축이 해제된 상태로 존재하는 걸 전제로 작동합니다. 
만일 루트 다렉토리가 `~/Korpora`와 다를 경우 `load` 함수 호출시 `root_dir=custom_path` 인자를 추가하시기 바랍니다.
```

다음과 같이 실행해도 모두의 말뭉치(형태 분석)를 읽어들일 수 있습니다.
수행 결과는 위의 코드와 동일합니다.

```python
from Korpora import ModuMorphemeKorpus
corpus = ModuMorphemeKorpus()
```

```warning
위의 코드는 해당 말뭉치가 사용자의 로컬 컴퓨터 루트 하위의 `~/Korpora/NIKL_MP` 디렉토리에 압축이 해제된 상태로 존재하는 걸 전제로 작동합니다. 
만일 다른 디렉토리에 말뭉치가 존재한다면 `ModuMorphemeKorpus` 클래스 선언시 `root_dir_or_paths=custom_path` 인자를 추가하시기 바랍니다.
```

위 코드 둘 중 하나를 택해 실행하면 `corpus`라는 변수에 말뭉치를 로드합니다.
`train`은 모두의 말뭉치(형태 분석)의 train 데이터로 첫번째 인스턴스는 다음과 같이 확인할 수 있습니다.

```
>>> corpus.train[0]
Morphemes(
    id=NWRW1800000022.417.1.1,
    sentence=[제주·서울] "세계환경수도 조성위해 10개년 실천계획 만들겠다" 김태환 지사 밝혀,
    tags=('[', '제주', '·', '서울', ']', '"', '세계', '환경', '수도', '조성', '위하', '아', '10', '개년', '실천', '계획', '만들', '겠', '다', '"', '김태환', '지사', '밝히', '어'),
    positions=('SS', 'NNP', 'SP', 'NNP', 'SS', 'SS', 'NNG', 'NNG', 'NNG', 'NNG', 'VV', 'EC', 'SN', 'NNB', 'NNG', 'NNG', 'VV', 'EP', 'EF', 'SS', 'NNP', 'NNG', 'VV', 'EF'),
    eojeol_id=(0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 6, 7, 8, 8)
)
>>> corpus.train[0].tags
('SS', 'NNP', 'SP', 'NNP', 'SS', 'SS', 'NNG', 'NNG', 'NNG', 'NNG', 'VV', 'EC', 'SN', 'NNB', 'NNG', 'NNG', 'VV', 'EP', 'EF', 'SS', 'NNP', 'NNG', 'VV', 'EF')
```
