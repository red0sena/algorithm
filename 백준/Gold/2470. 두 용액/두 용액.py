import sys


n = int(input())

input_list = list(map(int, input().split()))
min_val = float('inf')
input_list.sort()
ans = ()
left, right = 0, len(input_list)-1

while left<right:
    val = input_list[left] + input_list[right]
    if abs(val) < min_val:
        min_val = abs(val)
        ans = (left, right)
    if val == 0:
        print(input_list[left], input_list[right])
        break
    elif val > 0:
        right -= 1
    else:
        left += 1

a, b = ans
print(input_list[a], input_list[b])