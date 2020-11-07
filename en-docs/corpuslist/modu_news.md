---
sort: 13
---

# Modu: Newspaper

Modu: Newspaper is a dataset released by National Institute of Korean Language.
Data specification is as follows.

- author: National Institute of Korean Language
- repository: [https://corpus.korean.go.kr](https://corpus.korean.go.kr)
- references: [document](https://rlkujwkk7.toastcdn.net/NIKL_NEWSPAPER(v1.0).pdf)
- size:
  - train: about 3,500,000 examples

Data structure is as follows:

|Attributes|Property|
| --- | --- |
| document_id | Unique id of the article|
| title | Title of the metadata (not the actual title of the article) |
| author | author of the article |
| publisher | newspaper publisher |
| date | published date |
| topic | topic of the article (politics, business, social affairs, lifestyle, IT/science, entertainment, sports, culture, beauty/health) |
| original_topic | original topic categorized by the newpaper publishers |
| paragraph | body of the article (the first line seems to the title of the article) |

```warning
Due to the licensing issue of Modu corpus, `Korpora` does not provide any download functions for this corpus. Rather, it only offers a load function.
If you wish to use this corpus, please complete the authentication process required by the National Institue of Korean Language and manually download the corpus.
```

You can load the corpus from your Python console as follows.

```python
from Korpora import Korpora
corpus = Korpora.load("modu_news")
```

```warning
The code assumes that the corpus has already been unzipped into NIKL_WRITTEN directory within `~/Korpora` (`~/Korpora/NIKL_WRITTEN`).
If the root directory is not `~/Korpora`, add `root_dir=custom_path` argument to the `load` method.
```

You can also load the corpus as follows.
The output of these codes is identical to that of previous codes.

```python
from Korpora import ModuNewsKorpus
corpus = ModuNewsKorpus()
```

```warning
The codes assumes that the corpus has already been unzipped into `~/Korpora/NIKL_WRITTEN` within the current user's local root. 
If the corpus exists in another directory, add `root_dir_or_paths=custom_path` argument in `ModuNewsKorpus` class declaration.
```

```tip
If `load_light=True`, only the paragraphs and document_id are loaded. If it it set as `False`, all metadata are loaded as well. The default value of `load_light` is `True`.
```

If you use either one of these previous examples, you can load the corpus into the variable `corpus`.
`train` refers to the training dataset of the corpus, and you can check its first training instance as follows.

```
>>> corpus.train[0]
ModuNews(document_id='NPRW1900000010.1', title='한국경제 2018년 기사', author='김현석', publisher='한국경제신문사', date='20180101', topic='생활', original_topic='국제', paragraph=['"라니냐로 겨울 가뭄 온다"…', '...'])
```

By executing the `get_all_texts` method, you can access all paragraphs (bodies of all articles) within the corpus.

```
>>> corpus.get_all_texts()
[''"라니냐로 겨울 가뭄 온다"...', ... ]
```
