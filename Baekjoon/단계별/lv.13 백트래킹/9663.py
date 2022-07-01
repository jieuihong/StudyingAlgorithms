import sys

n = int(sys.stdin.readline())
board = [0] * n
cnt = 0


def is_possible(x):
    for i in range(x):
        if board[x] == board[i] or abs(board[x] - board[i]) == abs(x - i):
            return False
    return True


def queen(x):
    global cnt
    if x == n:
        cnt += 1

    else:
        for y in range(n):
            board[x] = y
            if is_possible(x):
                queen(x + 1)


queen(0)
print(cnt)
