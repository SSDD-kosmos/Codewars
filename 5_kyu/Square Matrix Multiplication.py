# https://codewars.com/kata/5263a84ffcadb968b6000513/train/python
import numpy as np  # I want to check my solution with numpy


def matrix_mult(a, b):
    output = []
    for row in range(len(a)):
        row_values = []
        for b_column in range(len(b)):
            current_row = a[row]
            current_col = [i[b_column] for i in b]
            value = sum([x*y for x, y in zip(current_row, current_col)])
            row_values.append(value)
        output.append(row_values)
    print(output)
    return output


matrix_mult([
                [1, 2],
                [3, 2]],
            [
                [3, 2],
                [1, 1]]
            )
# 5 4 11 8
