import sys
from bisect import bisect_left



n, m =  map(int, sys.stdin.readline().rstrip().split())
input_list = list(map(int, sys.stdin.readline().rstrip().split()))
res = 0
left, right = max(input_list), 10000 * n
while left <= right:
    mid = (left+right) // 2 # 블루레이 시간
    count = 1
    count = 1  # 최소 한 개의 블루레이 필요
    current_sum = 0

    # 강의를 순서대로 할당
    for lecture in input_list:
        if current_sum + lecture > mid:
            count += 1  # 새로운 블루레이에 강의를 넣음
            current_sum = lecture
        else:
            current_sum += lecture

    if count <= m:
        right =  mid - 1
        res = mid
    else:
        left = mid + 1

# 현재 제시한 블루레이 시간이 모든 강의를 3개로 나누었을 때 담을 수 있는가?
# 현재 mid 값으로 누접합을 m번만에 다 채울 수 있는가? <- 이거 어케 구현함?
# 채울 수 있다면 더 적은 mid값으로 해본다.
# 채울 수 없다면 더 많은 mid값으로 해본다.
print(res)

