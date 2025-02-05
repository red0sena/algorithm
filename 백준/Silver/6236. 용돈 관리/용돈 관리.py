n, m = map(int, input().split())

input_list = []

for _ in range(n):
    input_list.append(int(input()))

max_price = max(input_list)
left, right = max_price, (max_price*n)//m
res = 0
while left <= right:
    mid = (left+right) // 2
    k = mid
    count = 1
    for i in range(n):
        need_money = input_list[i]
        if need_money > k:
            k = mid
            count += 1
        k -= need_money
    if count > m:
        left = mid + 1

    else:
        right = mid - 1
        res = mid


print(res)