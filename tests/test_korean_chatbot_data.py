from Korpora import Korpora
from Korpora import KoreanChatbotKorpus


def test_usage():
    chatbot_data = Korpora.load('korean_chatbot_data')
    assert len(chatbot_data.train) == len(KoreanChatbotKorpus().train)
    assert len(chatbot_data.train.texts) == 11823
    assert len(chatbot_data.train.pairs) == 11823
    assert len(chatbot_data.train.labels) == 11823
    assert len(chatbot_data.get_all_texts()) == 11823
    assert len(chatbot_data.get_all_pairs()) == 11823
    assert len(chatbot_data.get_all_labels()) == 11823
    assert 'Chatbot_data_for_Korean v1.0' in chatbot_data.description
    assert 'CC0 1.0 Universal' in chatbot_data.license
    chatbot_data.train[0]
    print(f'str(korpus)\n{str(chatbot_data)}')
    print(f'str(korpus.train)\n{str(chatbot_data.train)}')
    for example in chatbot_data.train:
        continue
