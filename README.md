[README written in English](README.en-US.md)
------------------------------

# MicroTagger
一个微型的用于提取 Part-Of-Speech (POS) 的 Python 包

# 安装
```bash
pip install -r requirements.txt
```

# Python 版本
Only test by using Python3

# 使用
```python
#!/usr/bin/env python

from MicroTagger.hmm import HMMTagger

hmm_tagger = HMMTagger.load()

result = hmm_tagger.predict("知识 就是 力量 。")
print(result)
```

输出:
```text
知识/m  就是/d  力量/n  。/wj
```


# 性能

| ID | Model Name                   | Accuracy |
|:---|:-----------------------------|:---------|
| 1  | Most Frequent Class Baseline | 0.83703  |
| 2  | HMM                          | 0.92339  |

# Reference
[Speech and Language Processing > Part-of-Speech Tagging](https://web.stanford.edu/~jurafsky/slp3/10.pdf)
