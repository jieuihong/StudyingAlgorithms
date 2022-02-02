h, w = map(int, input().rstrip().split())
board = []
recolored = []

for _ in range(h):
    board.append(input())

for i in range(h - 7):
    print(i)
    for j in range(w - 7):
        print(j)
        first_white = 0
        first_black = 0
        for k in range(i, i + 8):
            print(k)
            for l in range(j, j + 8):
                print(l)
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        first_white += 1
                    else:
                        first_black += 1
                else:
                    if board[k][l] != 'B':
                        first_white += 1
                    else:
                        first_black += 1

        recolored.append(first_white)
        recolored.append(first_black)

print(min(recolored))
