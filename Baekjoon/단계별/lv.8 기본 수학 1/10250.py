t = int(input())

for i in range(t):
    h, w, n = map(int, input().rstrip().split())

    room_num = n//h + 1
    if n // h == 0:
        room_num = n //h
        floor = h
    else:
        room_num = n//h + 1
        floor = n % h

    print(str(floor * 100 + room_num))

