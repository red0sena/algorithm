n, m = map(int, input().split())

price_list = []

for _ in range(n):
    price_list.append(int(input()))

max_price = max(price_list)

low, high = max_price, ((max_price * n) // m)

answer = high

while low <= high:
    mid = (low+high) // 2
    count = 0
    nokori_price = mid
    for i in range(len(price_list)):
        price = price_list[i]
        if nokori_price - price < 0:
            nokori_price = mid
            nokori_price -= price
            count += 1
        else:
            nokori_price -= price
    
    if count < m:
        high = mid - 1
        answer = mid

    else:
        low = mid + 1

print(answer)