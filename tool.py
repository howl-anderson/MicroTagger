'''
    tool.py
    This is a tool for scoring posTag algorithm.
    Just scoring an algorithm with:
        > driver(trainLines, testLines, trainFunction, posTagFunction):
    And this tool will print a report of accuracy.
    Note: There are 19484 sentences in data set 'data.txt'.

    Zhang Zhiyuan ,EECS Peking Univ. 2017/02/23
'''


class dataType:
    def __init__(self):
        self.__fd = open('data.txt', 'r')
        self.__total = 0
        self.__correct = 0

    def getTrainLine(self):
        while True:
            bufferLine = self.__fd.readline().strip()
            if len(bufferLine) > 0:
                return bufferLine

    def getTestLine(self):
        while True:
            self.__buffer = self.__fd.readline().strip()
            line = self.__buffer
            for word in line.split():
                line = line.replace(word, word.split('/')[0])
            if len(line) > 0:
                return line

    def testLine(self, line):
        lineList = line.split()
        bufferList = self.__buffer.split()
        l = len(lineList)
        for i in range(l):
            self.__total += 1
            if lineList[i].split('/')[1] == bufferList[i].split('/')[1]:
                self.__correct += 1

    def report(self):
        print('Accuracy = %.5f' % (self.__correct / self.__total))


def driver(trainLines, testLines, trainFunction, posTagFunction):
    totalLines = 19484
    if trainLines + testLines > totalLines:
        print('Too many lines!')
        return
    data = dataType()
    for i in range(trainLines):
        line = data.getTrainLine()
        trainFunction(line)
    for i in range(testLines):
        data.testLine(posTagFunction(data.getTestLine()))
    data.report()
