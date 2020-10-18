# Korpora: Korean Corpora Archives

`Korpora`는 오픈소스 말뭉치들의 다운로드와 전처리 기능을 제공하는 파이썬 라이브러리입니다.
오픈소스 말뭉치들을 보다 쉽게 사용할 수 있도록 돕기 위해 만들었습니다.
말뭉치들을 공유해 주신 분들께 감사드립니다.


## Corpus List

- Korpora 패키지가 제공하는 말뭉치 목록은 다음과 같습니다.

|말뭉치 이름|설명|링크|
|---|---|---|
|korean_chatbot_data|챗봇 트레이닝용 문답 페어|[https://github.com/songys/Chatbot_data](https://github.com/songys/Chatbot_data)|
|kcbert|KcBERT 모델 학습용 댓글 데이터|[https://github.com/Beomi/KcBERT](https://github.com/Beomi/KcBERT)|
|korean_hate_speech|한국어 혐오 데이터셋|[https://github.com/kocohub/korean-hate-speech](https://github.com/kocohub/korean-hate-speech)|
|korean_petitions|청와대 국민 청원|[https://github.com/lovit/petitions_archive](https://github.com/lovit/petitions_archive)|
|kornli|Korean NLI|[https://github.com/kakaobrain/KorNLUDatasets](https://github.com/kakaobrain/KorNLUDatasets)|
|korsts|Korean STS|[https://github.com/kakaobrain/KorNLUDatasets](https://github.com/kakaobrain/KorNLUDatasets)|
|namuwikitext|나무위키 텍스트|[https://github.com/lovit/namuwikitext](https://github.com/lovit/namuwikitext)|
|naver_changwon_ner|네이버 x 창원대 개체명 인식 데이터셋|[https://github.com/naver/nlp-challenge/tree/master/missions/ner](https://github.com/naver/nlp-challenge/tree/master/missions/ner)|
|nsmc|NAVER Sentiment Movie Corpus|[https://github.com/e9t/nsmc](https://github.com/e9t/nsmc)|
|question_pair|한국어 질문쌍 데이터셋|[https://github.com/songys/Question_pair](https://github.com/songys/Question_pair)|
|modu_news|모두의 말뭉치: 신문|[https://corpus.korean.go.kr](https://corpus.korean.go.kr)|
|modu_messenger|모두의 말뭉치: 메신저|[https://corpus.korean.go.kr](https://corpus.korean.go.kr)|
|modu_mp|모두의 말뭉치: 형태 분석|[https://corpus.korean.go.kr](https://corpus.korean.go.kr)|
|modu_ne|모두의 말뭉치: 개체명 분석|[https://corpus.korean.go.kr](https://corpus.korean.go.kr)|
|modu_spoken|모두의 말뭉치: 구어|[https://corpus.korean.go.kr](https://corpus.korean.go.kr)|
|modu_web|모두의 말뭉치: 웹|[https://corpus.korean.go.kr](https://corpus.korean.go.kr)|
|modu_written|모두의 말뭉치: 문어|[https://corpus.korean.go.kr](https://corpus.korean.go.kr)|
|aihub_translation|한국어-영어 번역 말뭉치|[https://aihub.or.kr/aidata/87](https://aihub.or.kr/aidata/87)|
|open_substitles|영화 자막 한영 병렬 말뭉치|[http://opus.nlpl.eu/OpenSubtitles-v2018.php](http://opus.nlpl.eu/OpenSubtitles-v2018.php)|


## License

- Korpora 라이센스는 Creative Commons License(CCL) 4.0의 [CC-BY](https://creativecommons.org/licenses/by/4.0)입니다. 이 라이센스는 Korpora 패키지 및 그 부속물에 한정됩니다.
- 이용자는 다음의 권리를 갖습니다.
  - 공유 : 복제, 배포, 전시, 공연 및 공중 송신(포맷 변경도 포함) 등을 자유롭게 할 수 있습니다.
  - 변경 : 리믹스, 변형, 2차적 저작물의 작성이 가능합니다. 영리 목적으로도 이용이 가능합니다.
- 이용자는 다음의 의무가 있습니다. 아래 의무를 지키는 한 위의 권리가 유효합니다.
  - 저작자표시 : Korpora를 이용했다는 정보를 표시해야 합니다. 
  - 추가제한금지 : 이용자는 Korpora를 활용한 저작물에 [CC-BY](https://creativecommons.org/licenses/by/4.0)보다 엄격한 라이센스를 부가할 수 없습니다.

```warning
말뭉치 라이센스는 말뭉치별로 별도 적용됩니다. 자신이 사용할 말뭉치의 라이센스가 어떤 내용인지 활용 전에 반드시 확인하세요!
```


## Contributor

다음은 이 프로젝트에 기여한 분들입니다. 진심으로 감사드립니다. 여러분의 참여를 기다립니다.

<ul class="list-style-none">
{% for contributor in site.github.contributors %}
  <li class="d-inline-block mr-1">
     <a href="{{ contributor.html_url }}"><img src="{{ contributor.avatar_url }}" width="32" height="32" alt="{{ contributor.login }}"/></a>
  </li>
{% endfor %}
</ul>