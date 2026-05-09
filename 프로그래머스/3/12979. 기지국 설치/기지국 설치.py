def solution(n, stations, w):
    answer = 0
    # 기지국이 커버하는 총 너비
    width = 2 * w + 1
    
    # 탐색을 시작할 아파트 번호
    current = 1
    
    for station in stations:
        # 현재 위치에서 기지국 전파가 닿는 왼쪽 끝(station - w) 사이의 빈 공간 계산
        if station - w > current:
            blank_length = (station - w) - current
            # 빈 공간에 필요한 기지국 수 추가
            answer += (blank_length - 1) // width + 1
        
        # 현재 위치를 기지국 전파가 닿는 오른쪽 끝 다음으로 업데이트
        current = station + w + 1
    
    # 마지막 기지국 이후부터 아파트 끝(n)까지 남은 빈 공간 처리
    if current <= n:
        blank_length = n - current + 1
        answer += (blank_length - 1) // width + 1

    return answer