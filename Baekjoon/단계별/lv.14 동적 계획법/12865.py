n, k = map(int, input().split())

things = [(0,0)]
for _ in range(n):
    w, v = map(int, input().split())
    things.append((w, v))

backpack = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = things[i][0]
        value = things[i][1]

        if j < weight:
            # 현재 돌고 있는 j값이 weight보다 작으면 이전 물품의 j 시점의 최대값 가져오기
            backpack[i][j] = backpack[i-1][j]
        else:
            # option1, option2 중 최대값을 backpack[i][j]에 넣기

            # 이전 물품까지의 최대값
            option1 = backpack[i-1][j]
            # 현재 value와 (최대 무게 - 현재 물품 무게)의 최대 value를 더한 값
            option2 = backpack[i-1][j-weight] + value
            backpack[i][j] = max(option1, option2)

print(backpack[n][k])