# https://www.codewars.com/kata/52a382ee44408cea2500074c/train/python

import numpy as np


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    else:
        det = np.linalg.det(matrix)
        return round(det)


determinant([[4, 6], [3, 8]])
