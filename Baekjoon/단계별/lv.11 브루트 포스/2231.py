num = int(input())

digit_sum = 0
for i in range(num):
    digit_sum = i
    for n in str(digit_sum):
        digit_sum += int(n)

    if digit_sum == num:
        digit_sum = 1
        print(i)
        break

if digit_sum != 1:
    print(0)
