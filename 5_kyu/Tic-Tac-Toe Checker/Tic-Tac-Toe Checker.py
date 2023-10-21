# https://www.codewars.com/kata/525caa5c1bf619d28c000335/train/python


def is_solved(board):

    for i in range(0, 3):
        if len(set(board[i])) == 1:
            if board[i][0] == 1:
                return 1
            if board[i][0] == 2:
                return 2

        if len({board[0][i], board[1][i], board[2][i]}) == 1:
            if board[0][i] == 1:
                return 1
            if board[0][i] == 2:
                return 2

    if (len({board[0][0], board[1][1], board[2][2]}) == 1) | (
            len({board[0][2], board[1][1], board[2][0]}) == 1):
        if board[1][1] == 1:
            return 1
        if board[1][1] == 2:
            return 2

    for i in range(0, 3):
        if 0 in board[i]:
            return -1

    return 0


is_solved([[2, 1, 2],
           [2, 1, 1],
           [1, 1, 2]])
