#!/usr/bin/env python

from MicroTagger.hmm import HMMTagger

hmm_tagger = HMMTagger.load()

result = hmm_tagger.predict("知识 就是 力量 。")
print(result)
