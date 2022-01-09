# # 효율성 3, 4  틀림
# def solution(phone_book):
#     for i in range(len(phone_book)):
#         temp = phone_book[:]
#         temp.pop(i)
#         print(temp)
#         for t in temp:
#             print(t)
#             if len(t) > len(phone_book[i]) and phone_book[i] == t[:len(phone_book[i])]:
#                 return False
#     return True


from itertools import combinations


def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True


print(solution(["119", "97674223", "1195524421"]))