import sys
n = int(sys.stdin.readline().rstrip())

input_list = list(map(int, sys.stdin.readline().rstrip().split()))

input_list.sort()

min_val = int(10e10)
ans_list = None
for k in range(1, n):
    target = input_list[k-1]
    tmp_input_list = input_list[:k-1] + input_list[k:]
    # print(tmp_input_list, target)
    left, right = 0, n - 2
    while left < right:
        current_sum = tmp_input_list[left] + tmp_input_list[right] + target
        # print(current_sum, tmp_input_list[left], target, tmp_input_list[right])
        if min_val > abs(current_sum):
            min_val = abs(current_sum)
            # print('hit')
            ans_list = [tmp_input_list[left], target, tmp_input_list[right]]
        if current_sum == 0:
            print(*sorted([tmp_input_list[left], tmp_input_list[right], target]))
            exit(0)
        elif current_sum > 0:
            right -= 1
        else:
            left += 1

ans_list.sort()
print(*ans_list)
