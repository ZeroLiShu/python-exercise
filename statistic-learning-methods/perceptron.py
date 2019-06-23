#!

import numpy as np
import pysnooper
import random

def predict(w, x, b):
    """
    This function is the model of perceptron which is a linear classification model.

    param:
        w, weight vector in space Rn
        x, input space or feature space, x[i] in space Rn
        b, bias in space R
    """
    return np.sign(np.dot(w, x) + b)

@pysnooper.snoop()
def train(x, y, h):
    """
    This function uses training set {x, y} to calcualte w and b until there's no misclassification points

    param:
        x, feature space, x[i] in Rn
        y, output space, y[i] in {-1, 1}
        h, learing rate, 0 < h <= 1 
    """
    [rows, cols] = x.shape
    w = np.zeros((rows, 1))
    b = 0

    while (True):
        f = np.dot(w.T, x) + b
        L = y * f
        idx = np.where(L <= 0)

        sz = len(idx[0])
        if sz <= 0:
            break
        
        i = random.randint(1, sz)
        w = w + h * y[0][i-1] * x[:2, i-1:i]
        b = b + h * y[0][i-1]



    #iterator

if __name__ == "__main__":
    #x' shape is 2 rows, 3 columns, n=2, N=3
    x = np.array([[1,1,1], [2,2,2]])

    #y'shape is 1 row, 3 columns, n=1, N=3
    y = np.array([[1,-1,-1]])
    h = 0.1
    train(x, y, h)