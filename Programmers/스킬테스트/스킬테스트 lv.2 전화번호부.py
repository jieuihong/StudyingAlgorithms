# 효율성 X
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if len(phone_book[i]) == len(phone_book[i]):
                pass
            if phone_book[j][:len(phone_book[i])] == phone_book[i]:
                return False
    return True


# 통과
def solution(phone_book):
    book = {}
    for p in phone_book:
        book[p] = 1
    
    for phone in phone_book:
        temp = ""
        for num in phone:
            temp += num
            
            if temp in book and temp != phone:
                return False
    return True