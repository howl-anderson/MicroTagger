#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from MicroHMM.hmm import HMMModel

current_dir = os.path.dirname(os.path.abspath(__file__))

model_data_dir = os.path.join(current_dir, 'hmm_model_data')


class HMMTagger(object):
    def __init__(self, hmm_model=None):
        self.hmm_model = HMMModel() if hmm_model is None else hmm_model

    def train_one_line(self, line):
        list_of_word_tag_pair = []
        for word_pinyin_tag in line.split():
            # extract
            word, tag = word_pinyin_tag.split('/')
            list_of_word_tag_pair.append((word, tag))

        self.hmm_model.train_one_line(list_of_word_tag_pair)

    def predict(self, line, output_graphml_file=None):
        word_list = [i.strip() for i in line.split()]

        word_tag_pair = self.hmm_model.predict(word_list, output_graphml_file)
        word_tag = ["{}/{}".format(i[0], i[1]) for i in word_tag_pair]

        word_tag_str = "  ".join(word_tag)  # using two space char for better visible for human just as origin does

        return word_tag_str

    @classmethod
    def load(cls):
        hmm_model = HMMModel.load_model(model_data_dir)

        return cls(hmm_model)


if __name__ == "__main__":
    hmm_tagger = HMMTagger()
    hmm_tagger.train_one_line("我/A 是/B 中国人/C")
    hmm_tagger.train_one_line("你/A 打/B 人/C")
    result = hmm_tagger.predict("你 打 人")
    print(result)
