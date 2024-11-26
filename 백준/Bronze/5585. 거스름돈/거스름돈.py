import sys

bill = int(sys.stdin.readline().rstrip())
bill = 1000 - bill
count = 0
for coin in [500, 100, 50, 10, 5, 1]:
    count += bill // coin
    bill = bill - (bill // coin*coin)
    if bill == 0:
        break

print(count)

