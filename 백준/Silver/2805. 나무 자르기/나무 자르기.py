n, m = map(int, input().split())

input_list = list(map(int, input().split()))


max_val = max(input_list) - 1
min_val = 0
res = max_val

while min_val <= max_val:
    mid = (min_val+max_val) // 2
    tree_m = 0
    for tree in input_list:
        if tree >= mid:
            tree_m += (tree - mid)

    if tree_m >= m:
        min_val = mid + 1
        res = mid
    else:
        max_val = mid - 1


print(res)


