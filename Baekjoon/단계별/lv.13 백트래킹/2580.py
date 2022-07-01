import sys

board = [list(map(int, input().rstrip().split())) for _ in range(9)]
blanks = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]


def check_row(x, n):
    for i in range(9):
        if n == board[x][i]:
            return False
    return True


def check_col(y, n):
    for i in range(9):
        if n == board[i][y]:
            return False
    return True


def check_square(x, y, n):
    sq_x = x//3 * 3
    sq_y = y//3 * 3

    for i in range(3):
        for j in range(3):
            if n == board[sq_x+1][sq_y+1]:
                return False
    return True


def sudoku(idx):
    if idx == len(blanks):
        for i in range(9):
            print(*board[i])
        exit()

    for i in range(1, 10):
        x = blanks[idx][0]
        y = blanks[idx][1]

        if check_row(x, i) and check_col() and check_square(x, y, i):
            board[x][y] = i
            sudoku(idx+1)
            board[x][y] = 0