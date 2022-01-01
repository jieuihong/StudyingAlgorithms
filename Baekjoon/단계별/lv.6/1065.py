import sys

def han(n):
    lst = list(map(int, list(str(n))))

    diff = []
    for i in range(len(lst) - 1):
        diff.append(lst[i+1] - lst[i])

    for j in range(len(diff) - 1):
        if diff[j] != diff[j+1]:
            return False

    return True

if __name__ == '__main__':
    n = int(sys.stdin.readline())

    cnt = 0
    for i in range(1, n+1):
        if han(i) is True:
            cnt += 1

    print(cnt)
