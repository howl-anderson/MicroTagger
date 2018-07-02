#!/usr/bin/env python
"""
Most Frequent Class Baseline
"""

import tool


class BaseLineModel(object):
    def __init__(self):
        self.dic = {}

    def train(self, line):
        for wordTag in line.split():
            word, tag = wordTag.split('/')
            if word in self.dic:
                if tag in self.dic[word]:
                    self.dic[word][tag] += 1
                else:
                    self.dic[word][tag] = 1
            else:
                self.dic[word] = {tag: 1}

    def posTag(self, line):
        lineList = line.split()
        l = len(lineList)
        for i in range(l):
            word = lineList[i]
            if word in self.dic:
                bestTag = ''
                bestTagreq = 0
                for tag in self.dic[word]:
                    if self.dic[word][tag] > bestTagreq:
                        bestTagreq = self.dic[word][tag]
                        bestTag = tag
                lineList[i] = lineList[i] + '/' + bestTag
            else:
                lineList[i] = lineList[i] + '/' + 'unknow'

        word_tag_str = '  '.join(lineList)  # using two space char for better visible for human just as origin does

        return word_tag_str


if __name__ == "__main__":
    base_line = BaseLineModel()

    # tool.driver(19000, 100, base_line.train, base_line.posTag)
    tool.driver(10000, 100, base_line.train, base_line.posTag)
