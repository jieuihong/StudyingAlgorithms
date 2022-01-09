while True:
    tri = list(map(int, input().rstrip().split()))
    if not all(tri):
        break
    else:
        longest = max(tri)
        tri.remove(longest)

        if (tri[0] ** 2) + (tri[1] ** 2) == (longest ** 2):
            print('right')
        else:
            print('wrong')
