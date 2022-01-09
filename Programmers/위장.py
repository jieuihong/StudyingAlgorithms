from itertools import combinations

def solution(clothes):
    clothes_dict = {}
    
    for c in clothes:
        if c[1] not in clothes_dict:
            clothes_dict[c[1]] = [c[0]]
        else:
            clothes_dict[c[1]].append(c[0])
    print(clothes_dict)

    comb = []
    for i in range(1, len(clothes_dict)+1):
        comb.extend(combinations(clothes_dict, i))

    print(comb)
    
    return ''


solution([["yellowhat", "headgear"],
              ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
