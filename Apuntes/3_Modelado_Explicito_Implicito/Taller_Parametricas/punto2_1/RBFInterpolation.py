import numpy as np


def euclidean_distance(points: np.ndarray, points2: np.ndarray):
    result = []
    for i in range(len(points)):
        res_aux = []
        for j in range(len(points2)):
            res_aux.append(np.sqrt(np.sum((points[i] - points2[j]) ** 2)))
        result.append(res_aux)
    return np.array(result)


def gauss_rbf(radius, eps):
    return np.exp(-(eps * radius) ** 2)


class RBFInterp(object):
    def __init__(self, linear: bool):
        self.linear = linear
        self.xk = None
        self.w_ = None

    def fit(self, xk, yk):
        self.xk = xk
        transformation = euclidean_distance(xk, xk)
        print(transformation.shape)
        transformation = transformation if self.linear else gauss_rbf(transformation, 2)
        self.w_ = np.linalg.solve(transformation, yk.reshape(-1, 1))

    def __call__(self, xn):
        transformation = euclidean_distance(xn, self.xk)
        transformation = transformation if self.linear else gauss_rbf(transformation, 2)
        return transformation.dot(self.w_)
