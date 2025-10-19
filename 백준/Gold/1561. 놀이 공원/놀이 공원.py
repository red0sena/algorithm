import sys

def solve():
    # 입력 받기
    # N: 아이들의 수, M: 놀이기구의 수
    n, m = map(int, sys.stdin.readline().split())
    # 각 놀이기구의 운행 시간
    times = list(map(int, sys.stdin.readline().split()))

    # 1. 기본 케이스 처리: 아이들이 놀이기구 수보다 적을 경우
    if n <= m:
        print(n)
        return

    # 2. 이분 탐색으로 N번째 아이가 타는 시간 찾기
    left, right = 0, n * 30  # 시간의 최소, 최대 범위 설정
    min_time = 0

    while left <= right:
        mid = (left + right) // 2
        
        # mid 시간까지 탑승한 아이의 수 계산
        # 처음 m명이 바로 탑승 + mid 시간 동안 추가로 탑승한 인원
        count = m
        for t in times:
            count += mid // t
        
        if count >= n:
            # n명 이상 탑승했다면, 시간을 줄여서 더 최적의 시간을 찾는다.
            min_time = mid
            right = mid - 1
        else:
            # n명 미만 탑승했다면, 시간이 더 필요하다.
            left = mid + 1

    # 3. N번째 아이가 타는 정확한 놀이기구 찾기
    # min_time - 1 까지 탑승한 아이의 수를 계산
    count_before = m
    for t in times:
        count_before += (min_time - 1) // t

    # min_time에 타는 아이들 중에서 N번째 아이가 몇 번째인지 계산
    target_order = n - count_before
    
    current_order = 0
    for i in range(m):
        # min_time에 운행이 끝나는 놀이기구를 찾는다.
        if min_time % times[i] == 0:
            current_order += 1
            if current_order == target_order:
                # 찾았다!
                print(i + 1)
                return

solve()