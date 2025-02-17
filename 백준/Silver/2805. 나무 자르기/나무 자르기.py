from bisect import bisect_left

n, m = map(int, input().split())

input_list = list(map(int, input().split()))

left, right = 0, 1000000000
res = 0
flag = True

input_list.sort()


prefix = [0]

for i in range(n):
    prefix.append(prefix[i] + input_list[i])


while left <= right:
    mid = (left+right) // 2
    mid_idx = bisect_left(input_list, mid)

    tree_len_sum = (prefix[-1] - prefix[mid_idx]) - mid * (n-mid_idx)


    if tree_len_sum == m:
        print(mid)
        flag = False
        break
    elif tree_len_sum > m:
        left = mid + 1
        res = mid
    else:
        right = mid - 1



if flag:
    print(res)