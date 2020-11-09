---
sort: 15
---

# Modu: Morphemes

Modu: Morphemes is a dataset released by National Institute of Korean Language.
Data specification is as follows.

- author: National Institute of Korean Language
- repository: [https://corpus.korean.go.kr](https://corpus.korean.go.kr)
- references: [document](https://rlkujwkk7.toastcdn.net/NIKL_MP(v1.0).pdf)
- size:
  - train: 371,571 examples

```warning
Due to the licensing issue of Modu corpus, `Korpora` does not provide any download functions for this corpus. Rather, it only offers a load function.
If you wish to use this corpus, please complete the authentication process required by the National Institue of Korean Language and manually download the corpus. 
```

You can load the corpus from your Python console as follows.

```python
from Korpora import Korpora
corpus = Korpora.load("modu_mp")
```

```warning
The code assumes that the corpus has already been unzipped into NIKL_MP directory within `~/Korpora` (`~/Korpora/NIKL_MP`).
If the root directory is not `~/Korpora`, add `root_dir=custom_path` argument to the `load` method.
```

You can also load the corpus as follows.
The output of these codes is identical to that of previous codes.

```python
from Korpora import ModuMorphemeKorpus
corpus = ModuMorphemeKorpus()
```

```warning
The codes assumes that the corpus has already been unzipped into `~/Korpora/NIKL_MP` within the current user's local root. 
If the corpus exists in another directory, add `root_dir_or_paths=custom_path` argument in `ModuMorphemeKorpus` class declaration.
```

If you use either one of these previous examples, you can load the corpus into the variable `corpus`.
`train` refers to the training dataset of the corpus, and you can check its first training instance as follows.

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
