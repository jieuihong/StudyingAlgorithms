def n_base(m, n):
    num = ''
    while m > 0:
        m, r = divmod(m, n)
        num += str(r)
    return num[::-1]


def solution(n, t, m, p):
    lst = []

    for i in range(m * t):
        l = list(n_base(i, n))
        print(l)
        lst.extend(l)

    print(f"final lst: {lst}")

    answer = []
    for i in range(t):
        answer.append(lst[p + m*i])

    return answer


print(n_base(15, 16))
# print(solution(16, 16, 2, 1))