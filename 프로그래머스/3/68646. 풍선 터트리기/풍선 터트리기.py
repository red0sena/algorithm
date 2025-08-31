def solution(a):
    n = len(a)
    if n == 0:
        return 0
    inf = 10**10
    left_min = [inf] * n
    for i in range(1, n):
        left_min[i] = min(left_min[i-1], a[i-1])
    right_min = [inf] * n
    for i in range(n-2, -1, -1):
        right_min[i] = min(right_min[i+1], a[i+1])
    count = 0
    for i in range(n):
        if not (left_min[i] < a[i] and right_min[i] < a[i]):
            count += 1
    return count