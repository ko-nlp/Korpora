---
sort: 18
---

# Modu: Web

Modu: Web is a dataset released by National Institute of Korean Language.
Data specification is as follows.

- author: National Institute of Korean Language
- repository: [https://corpus.korean.go.kr](https://corpus.korean.go.kr)
- references: [document](https://rlkujwkk7.toastcdn.net/NIKL_WEB(v1.0).pdf)
- size:
  - train: 2,107,076 examples

```warning
Due to the licensing issue of Modu corpus, `Korpora` does not provide any download functions for this corpus. Rather, it only offers a load function.
If you wish to use this corpus, please complete the authentication process required by the National Institue of Korean Language and manually download the corpus.
```

You can load the corpus from your Python console as follows.

```python
from Korpora import Korpora
corpus = Korpora.load("modu_web")
```

```warning
The code assumes that the corpus has already been unzipped into NIKL_WRITTEN directory within `~/Korpora` (`~/Korpora/NIKL_WRITTEN`).
If the root directory is not `~/Korpora`, add `root_dir=custom_path` argument to the `load` method.
```

You can also load the corpus as follows.
The output of these codes is identical to that of previous codes.

```python
from Korpora import ModuWebKorpus
corpus = ModuWebKorpus()
```

```warning
The codes assumes that the corpus has already been unzipped into `~/Korpora/NIKL_WRITTEN` within the current user's local root.
If the corpus exists in another directory, add `root_dir_or_paths=custom_path` argument in `ModuWebKorpus` class declaration.
```

If you use either one of these previous examples, you can load the corpus into the variable `corpus`.
`train` refers to the training dataset of the corpus, and you can check its first training instance as follows.

```
>>> corpus.train[0]
오메가3와 비타민C, 달맞이꽃종자유 등을 사려고 몇 시간을 검색하며 공부했다 ...
```
