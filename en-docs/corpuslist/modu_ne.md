---
sort: 16
---

# Modu: Named Entity

Modu: Named Entity is a dataset released by National Institute of Korean Language.
Data specification is as follows.


- author: National Institute of Korean Language
- repository: [https://corpus.korean.go.kr](https://corpus.korean.go.kr)
- references: [document](https://rlkujwkk7.toastcdn.net/NIKL_NE(v1.0).pdf)
- size:
  - train: 20,188 examples

```warning
Due to the licensing issue of Modu corpus, `Korpora` does not provide any download functions for this corpus. Rather, it only offers a load function.
If you wish to use this corpus, please complete the authentication process required by the National Institue of Korean Language and manually download the corpus. 
```

You can load the corpus from your Python console as follows.

```python
from Korpora import Korpora
corpus = Korpora.load("modu_ne")
```

```warning
The code assumes that the corpus has already been unzipped into NIKL_NE directory within `~/Korpora` (`~/Korpora/NIKL_NE`).
If the root directory is not `~/Korpora`, add `root_dir=custom_path` argument to the `load` method.
```

You can also load the corpus as follows.
The output of these codes is identical to that of previous codes.

```python
from Korpora import ModuNEKorpus
corpus = ModuNEKorpus()
```

```warning
The codes assumes that the corpus has already been unzipped into `~/Korpora/NIKL_NE` within the current user's local root. 
If the corpus exists in another directory, add `root_dir_or_paths=custom_path` argument in `ModuNEKorpus` class declaration.
```

If you use either one of these previous examples, you can load the corpus into the variable `corpus`.
`train` refers to the training dataset of the corpus, and you can check its first training instance as follows.

```
>>> corpus.train[0]
NamedEntityExample(
    id=NWRW1800000029.315.1.1,
    sentence=[횡설수설/권순활]北 ‘외화벌이’ 뜯어먹기,
    tags=['AF', 'PS', 'LC'],
    positions=[(1, 5), (6, 9), (10, 11)]
)
>>> corpus.train[0].sentence
[횡설수설/권순활]北 ‘외화벌이’ 뜯어먹기
```