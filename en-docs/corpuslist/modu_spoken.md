---
sort: 17
---

# Modu: Spoken

Modu: Spoken is a dataset released by National Institute of Korean Language.
Data specification is as follows.

- author: National Institute of Korean Language
- repository: [https://corpus.korean.go.kr](https://corpus.korean.go.kr)
- references: [document](https://rlkujwkk7.toastcdn.net/NIKL_SPOKEN(v1.0).pdf)
- size:
  - train: 27,920 examples

```warning
Due to the licensing issue of Modu corpus, `Korpora` does not provide any download functions for this corpus. Rather, it only offers a load function.
If you wish to use this corpus, please complete the authentication process required by the National Institue of Korean Language and manually download the corpus.
```

You can load the corpus from your Python console as follows.

```python
from Korpora import Korpora
corpus = Korpora.load("modu_spoken")
```

```warning
The code assumes that the corpus has already been unzipped into NIKL_SPOKEN directory within `~/Korpora` (`~/Korpora/NIKL_SPOKEN`).
If the root directory is not `~/Korpora`, add `root_dir=custom_path` argument to the `load` method.
```

You can also load the corpus as follows.
The output of these codes is identical to that of previous codes.

```python
from Korpora import ModuSpokenKorpus
corpus = ModuSpokenKorpus()
```

```warning
The codes assumes that the corpus has already been unzipped into `~/Korpora/NIKL_SPOKEN` within the current user's local root. 
If the corpus exists in another directory, add `root_dir_or_paths=custom_path` argument in `ModuSpokenKorpus` class declaration.
```

If you use either one of these previous examples, you can load the corpus into the variable `corpus`.
`train` refers to the training dataset of the corpus, and you can check its first training instance as follows.

```
>>> corpus.train[0]
요즘처럼 추운 날씨에는 따뜻한 라테 한잔 찾는 분들 많으실 텐데요...
```
