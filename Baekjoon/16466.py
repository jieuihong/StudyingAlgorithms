import sys

num_sold = int(sys.stdin.readline())
sold_tickets = list(map(int, sys.stdin.readline().split()))
sold_tickets.sort()

min_ticket = 1
for i in range(num_sold):
    if min_ticket == sold_tickets[i]:
        min_ticket += 1
    else:
        print(min_ticket)
        sys.exit(0)

print(sold_tickets[-1] + 1)
