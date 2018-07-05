# MicroTagger

# Python version
Only test by using Python3

# Usage
```python
#!/usr/bin/env python

from MicroTagger.hmm import HMMTagger

hmm_tagger = HMMTagger.load()

result = hmm_tagger.predict("知识 就是 力量 。")
print(result)
```

Output:
```text
知识/m  就是/d  力量/n  。/wj
```


# Performance

| ID | Model Name                   | Accuracy |
|:---|:-----------------------------|:---------|
| 1  | Most Frequent Class Baseline | 0.83703  |
| 2  | HMM                          | 0.92339  |

# Reference
[Speech and Language Processing > Part-of-Speech Tagging]([](https://web.stanford.edu/~jurafsky/slp3/10.pdf))
