n = int(input())

num1, num2 = 0, 1
if n == 0 or n == 1:
    print(n)
else:
    for i in range(2, n+1):
        num1, num2 = num2, (num1+num2)

    print(num2)
