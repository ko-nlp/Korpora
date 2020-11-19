---
sort: 14
---

# Modu: Messenger

Modu: Messenger is a dataset released by National Institute of Korean Language.
Data specification is as follows.

- author: National Institute of Korean Language
- repository: [https://corpus.korean.go.kr](https://corpus.korean.go.kr)
- references: [document](https://rlkujwkk7.toastcdn.net/NIKL_MESSENGER(v1.0).pdf)
- size:
  - train: 4,203 examples

Data structure is as follows:

|Attributes|Property|
| --- | --- |
| document_id | Unique id of the conversation |
| form | text of the conversation |
| original_form | original text of the conversation |
| speaker_id | speaker (in non-numerical format) |
| time | `yyyymmdd hh:mm` format |

```warning
Due to the licensing issue of Modu corpus, `Korpora` does not provide any download functions for this corpus. Rather, it only offers a load function.
If you wish to use this corpus, please complete the authentication process required by the National Institue of Korean Language and manually download the corpus. 
```

You can load the corpus from your Python console as follows.

```python
from Korpora import Korpora
corpus = Korpora.load("modu_messenger")
```

```warning
The code assumes that the corpus has already been unzipped into NIKL_MESSENGER directory within `~/Korpora` (`~/Korpora/NIKL_MESSENGER`).
If the root directory is not `~/Korpora`, add `root_dir=custom_path` argument to the `load` method.
```

You can also load the corpus as follows.
The output of these codes is identical to that of previous codes.

```python
from Korpora import ModuMessengerKorpus
corpus = ModuMessengerKorpus()
```

```warning
The codes assumes that the corpus has already been unzipped into `~/Korpora/NIKL_MESSENGER` within the current user's local root. 
If the corpus exists in another directory, add `root_dir=custom_path` argument in `ModuMessengerKorpus` class declaration.
```

If you use either one of these previous examples, you can load the corpus into the variable `corpus`.
`train` refers to the training dataset of the corpus, and you can check its first training instance as follows.

```
>>> corpus.train[0]
Conversation(id=MDRW1900000002.1, len=70, attributes=(form(str), original_form(str), speaker_id(str), time(str)))
>>> corpus.train[0].form
('누나 모해??', 'ㅋㅋㅋㅋ 일하고 있지ㅠㅠ', ... )
>>> corpus.train[0].speaker_id
('1', '2', ... )
```
