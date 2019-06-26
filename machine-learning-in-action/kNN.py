#!

import numpy as np
import pysnooper
import operator

@pysnooper.snoop()
def createDataSet():
    group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

@pysnooper.snoop()
def calcDistance(inX, dataSet):
    rows = dataSet.shape[0]
    diffMat = np.tile(inX, (rows, 1))
    diffMat = diffMat - dataSet
    sqMat = diffMat ** 2
    sqDist = sqMat.sum(axis=1)
    distance = sqDist ** 0.5

    #sort in ascending order, output is the index of array
    idxDistance = distance.argsort()

    return idxDistance

@pysnooper.snoop()
def voteForClasses(idxDistance, k, labels):
    #count for given class labels
    classCountMap = {}
    #choose nearest k distances
    for i in range(k):
        idx = idxDistance[i]
        label = labels[idx]
        classCountMap[label] = classCountMap.get(label, 0) + 1
    
    #sort per count
    orderClassCount = sorted(classCountMap.items(), key=operator.itemgetter(1), reverse=True)

    #the maximum count of class
    return orderClassCount[0][0]

if __name__ == "__main__":
    features, labels = createDataSet()
    idx = calcDistance([0, 0], features)
    classLabel = voteForClasses(idx, 2, labels)