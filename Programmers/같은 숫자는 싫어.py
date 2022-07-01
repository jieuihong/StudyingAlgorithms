# -- 정확성 O, 효율성 X인 코드 --
# def solution(arr):
#     i = 0
#     while i < len(arr)-1:
#         if arr[i] == arr[i + 1]:
#             arr.pop(i + 1)
#         else:
#             i += 1
#     return arr

# 맞은 코드

def solution(arr):
    ans = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            ans.append(arr[i])
    return ans


