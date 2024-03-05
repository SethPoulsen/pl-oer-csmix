import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import numpy.linalg as la

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

def permuteImage(filename):

    img = mpimg.imread(filename)
    X = rgb2gray(img)

    n,m = X.shape

    P = np.eye(n,n)
    perm = np.random.permutation(n)
    P = P[:,perm]

    Q = np.eye(m,m)
    perm = np.random.permutation(m)
    Q = Q[:,perm]

    ymat = P.dot(X.dot(Q))

    A = np.kron(P,Q.T)

    return A, ymat
