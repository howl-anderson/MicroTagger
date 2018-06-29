#!/usr/bin/env python

import tool
from hmm import HMMTagger

hmm_tagger = HMMTagger()


tool.driver(10001, 100, hmm_tagger.train_one_line, hmm_tagger.predict)
