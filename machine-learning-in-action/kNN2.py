#!

import numpy as np
import kNN
import pysnooper
import matplotlib.pyplot as plt

#@pysnooper.snoop()
def file2Mat(filename):
    fl = open(filename)
    lines = fl.readlines()
    rows = len(lines)

    #here, assume the number of cols is 3
    returnMat = np.zeros((rows, 3))
    labels = []

    row = 0
    for line in lines:
        #strip useless characters of head and tail
        line = line.strip()
        cols = line.split('\t')
        returnMat[row, :] = cols[0:3]
        labels.append(cols[-1])
        row += 1

    fl.close()

    return returnMat, labels


def scatterTwoFeatures(featureX, featureY):
    fig = plt.figure()
    #111 means row 1, col 1, block 1
    #349 means row 3, col 4, block 9
    #3410 doesn't work, use (3, 4, 10)
    ax = fig.add_subplot(111)
    ax.scatter(featureX, featureY)
    plt.show()

if __name__ == "__main__":
    datingFeatures, datingLabels = file2Mat('datingTestSet.txt')
    scatterTwoFeatures(datingFeatures[:, 1], datingFeatures[:, 2])