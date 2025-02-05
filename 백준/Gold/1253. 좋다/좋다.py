import sys

n = int(sys.stdin.readline().rstrip())

input_list = list(map(int, sys.stdin.readline().rstrip().split()))

input_list.sort()

count = 0

for k in range(n):
    target = input_list[k]
    left, right = 0, n-1

    while left < right:
        if left == k:
            left += 1
            continue
        if right == k:
            right -= 1
            continue

        lr = input_list[left] + input_list[right]
        if lr == target:
            count += 1
            break
        elif lr < target:
            left += 1
        else:
            right -= 1


print(count)
