import sys

X, Y = map(int, sys.stdin.readline().split())

# 현재 승률 (소수점 버림)
Z = (Y * 100) // X

# 현재 승률이 99 이상이면 아무리 이겨도 변하지 않음
if Z >= 99:
    print(-1)
    exit(0)

# 이분 탐색을 위한 범위 설정
low, high = 1, 10000000000
answer = -1

while low <= high:
    mid = (low + high) // 2
    newZ = ((Y + mid) * 100) // (X + mid)

    if newZ > Z:
        answer = mid
        high = mid - 1
    else:
        low = mid + 1

print(answer)