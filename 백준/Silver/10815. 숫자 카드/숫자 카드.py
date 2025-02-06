from bisect import bisect_left, bisect_right

n = int(input())
card_list = list(map(int, input().split()))
card_list.sort()

m = int(input())
num_list = list(map(int, input().split()))
for num in num_list:
    left, right = 0, n-1
    flag = False
    while left <= right:
        mid = (left+right) // 2
        if card_list[mid] == num:
            flag = True
            break
        elif card_list[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    if flag:
        print(1)
    else:
        print(0)
