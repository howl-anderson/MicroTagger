#!/usr/bin/env python

from tqdm import tqdm

from tool import dataType

trainLines = 19000
testLines = 1

data = dataType()

from hmm import HMMTagger

hmm_tagger = HMMTagger()

tqdm.write("Training start!")
for i in tqdm(range(trainLines)):
    line = data.getTrainLine()
    hmm_tagger.train_one_line(line)

result = hmm_tagger.predict("知识 就是 力量 。", output_graphml_file="demo.graphml")
print(result)
