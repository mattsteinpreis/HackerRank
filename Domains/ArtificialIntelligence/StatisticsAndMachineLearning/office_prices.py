import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def make_poly_features(mat, max_order):
    poly = PolynomialFeatures(max_order)
    polymat = poly.fit_transform(mat)
    return polymat


if __name__ == '__main__':
    n_feat, n_obs = [int(i) for i in input().strip().split()]

    datamat = np.array([None]*(n_feat+1), ndmin=2)
    for input_i in range(n_obs):
        line = [float(i) for i in input().strip().split()]
        datamat = np.append(datamat, np.array(line,ndmin=2), 0)
    datamat = datamat[1:,:]
    n_test = int(input())
    testmat = np.array([None]*n_feat, ndmin=2)
    for input_i in range(n_test):
        line = [float(i) for i in input().strip().split()]
        testmat = np.append(testmat, np.array(line, ndmin=2), 0)
    testmat = testmat[1:,:]

    X = datamat[:, :n_feat]
    X = make_poly_features(X, 4)
    y = datamat[:, n_feat , None]

    lr = LinearRegression()
    lr.fit(X, y)

    Xtest = make_poly_features(testmat, 4)
    pred = lr.predict(Xtest)
    for p in pred:
        print(p[0])
