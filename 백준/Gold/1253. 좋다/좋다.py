import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# 1) 배열 정렬
arr.sort()

good_count = 0

# 2) 각 원소 arr[k]를 타겟으로 두고 투 포인터 진행
for k in range(N):
    target = arr[k]
    left, right = 0, N - 1
    found = False

    while left < right:
        # k 자신(동일 인덱스)은 건너뛴다
        if left == k:
            left += 1
            continue
        if right == k:
            right -= 1
            continue

        current_sum = arr[left] + arr[right]

        if current_sum == target:
            # arr[k] = arr[left] + arr[right] 발견!
            found = True
            break
        elif current_sum < target:
            left += 1
        else:  # current_sum > target
            right -= 1

    if found:
        good_count += 1

print(good_count)