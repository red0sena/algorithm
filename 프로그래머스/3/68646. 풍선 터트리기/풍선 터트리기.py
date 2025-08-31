def solution(a):
    n = len(a)
    
    inf = float('inf')
    # 현재 index 기준 왼쪽에 풍선 중에서 최소값 구하기
    left_min = [inf] * n
    for i in range(1, n):
        left_min[i] = min(left_min[i-1], a[i-1])
		
		# 현재 index 기준 오른쪽의 풍선 중에서 최소값 구하기
    right_min = [inf] * n
    for i in range(n-2, -1, -1):
        right_min[i] = min(right_min[i+1], a[i+1])
    
    # 마지막까지 남을 수 있는 풍선 수 세기
    count = 0
    for i in range(n):
		    # 왼쪽 최소값보다 작거나 오른쪽 최소값보다 작으면 살 수 있다.
        if a[i] <= left_min[i] or a[i] <= right_min[i]:
            count += 1
    return count