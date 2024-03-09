#encoding:utf8
import jieba
import re


class TextUtil:
    re_alpha = "[a-zA-Z]+"
    re_num = "[0-9]+"

    def __init__(self):
        self.tokenizer = jieba.Tokenizer()

    def tokenize_words(self, input_text):
        tokenized_words = self.tokenizer.tokenize(input_text)

        output_words = []
        for word in tokenized_words:
            if len(word) < 2:
                continue
            if re.match(self.re_num, word):
                continue
            if re.match(self.re_alpha, word):
                continue
            output_words.append(word)
        return output_words

    def split_sentences(self, input_text):
        return re.split("。|！|？", input_text)
