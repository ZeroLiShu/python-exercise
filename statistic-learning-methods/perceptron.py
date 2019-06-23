import numpy as np

def f(w, x, b):
    """
    This function is the model of perceptron which is a linear classification model.

    param:
        w, weight vector in space Rn
        x, input space or feature space, x[i] in space Rn
        b, bias in space R
    """
    return np.sign(np.dot(w, x) + b)

def train(x, y, h):
    """
    This function uses training set {x, y} to calcualte w and b until there's no misclassification points

    param:
        x, feature space, x[i] in Rn
        y, output space, y[i] in {-1, 1}
        h, learing rate, 0 < h <= 1 
    """
    w = np.zeros(y.shape)
    b = 0
    f = np.dot(w, x) + b
    L = y * f
    idx = np.where(L <= 0)
    
