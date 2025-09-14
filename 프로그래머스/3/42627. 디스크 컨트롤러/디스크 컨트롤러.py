import heapq

def solution(jobs):
    """
    디스크 컨트롤러 문제에 대한 해결 함수입니다.

    Args:
        jobs: 각 작업의 [요청 시점, 소요 시간]을 담은 2차원 리스트

    Returns:
        작업의 요청부터 종료까지 걸린 시간의 평균 (소수점 이하 버림)
    """
    
    # jobs 리스트를 요청 시간 기준으로 오름차순 정렬합니다.
    # jobs가 비어있는 경우를 대비해 인덱스 초기값을 -1로 설정합니다.
    jobs.sort()
    
    start_time = -1  # 마지막으로 작업이 시작된 시간
    current_time = 0   # 현재 시각
    total_response_time = 0  # 모든 작업의 '요청부터 종료까지' 걸린 시간의 총합
    completed_jobs = 0 # 처리 완료된 작업의 수
    
    # 처리해야 할 작업의 총 개수
    total_jobs = len(jobs)
    # 다음으로 큐에 넣을 작업의 인덱스
    job_index = 0
    # 처리 대기 중인 작업을 저장할 최소 힙 (소요 시간을 기준으로 정렬)
    waiting_heap = []

    while completed_jobs < total_jobs:
        # 현재 시점 이전에 요청된 모든 작업을 힙에 추가합니다.
        # 힙에는 [소요 시간, 요청 시간] 형태로 저장하여 소요 시간 기준으로 최소 힙이 구성되도록 합니다.
        while job_index < total_jobs and jobs[job_index][0] <= current_time:
            heapq.heappush(waiting_heap, [jobs[job_index][1], jobs[job_index][0]])
            job_index += 1
            
        # 처리할 작업이 힙에 있는 경우
        if waiting_heap:
            # 소요 시간이 가장 짧은 작업을 꺼냅니다.
            duration, request_time = heapq.heappop(waiting_heap)
            
            # 현재 시간을 작업이 끝나는 시간으로 업데이트합니다.
            current_time += duration
            
            # '작업 종료 시간 - 작업 요청 시간'을 총 소요 시간에 더합니다.
            total_response_time += (current_time - request_time)
            
            # 처리된 작업 수를 증가시킵니다.
            completed_jobs += 1
        # 처리할 작업이 힙에 없는 경우 (현재 시점에 할 일이 없음)
        else:
            # 다음 작업의 요청 시간으로 현재 시간을 점프시킵니다.
            if job_index < total_jobs:
                current_time = jobs[job_index][0]

    # 총 소요 시간을 작업의 수로 나누어 평균을 구하고, 소수점 이하는 버립니다.
    return total_response_time // total_jobs