#!/usr/bin/env python
"""
Most Frequent Class Baseline
"""

import tool

dic = {}


def train(line):
    for wordTag in line.split():
        word, tag = wordTag.split('/')
        if word in dic:
            if tag in dic[word]:
                dic[word][tag] += 1
            else:
                dic[word][tag] = 1
        else:
            dic[word] = {tag: 1}


def posTag(line):
    lineList = line.split()
    l = len(lineList)
    for i in range(l):
        word = lineList[i]
        if word in dic:
            bestTag = ''
            bestTagreq = 0
            for tag in dic[word]:
                if dic[word][tag] > bestTagreq:
                    bestTagreq = dic[word][tag]
                    bestTag = tag
            lineList[i] = lineList[i] + '/' + bestTag
        else:
            lineList[i] = lineList[i] + '/' + 'unknow'
    return ' '.join(lineList)


tool.driver(10000, 5000, train, posTag)
