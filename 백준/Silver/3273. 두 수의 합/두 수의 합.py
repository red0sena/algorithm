n = int(input())
input_list = list(map(int, input().split()))
input_list.sort()
x = int(input())

left, right = 0, len(input_list)-1
count = 0

while True:
    sum_val = input_list[left] + input_list[right]
    if left == right:
        break
    elif sum_val == x:
        count += 1
        left += 1
    elif sum_val < x:
        left += 1
    else:
        right -= 1

print(count)