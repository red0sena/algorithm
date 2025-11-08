import sys

# 빠른 입출력을 위한 설정
input = sys.stdin.readline

N, M = map(int, input().split())
stations = list(map(int, input().split()))

# 역 번호가 최대 1,000,000이므로 1,000,001 크기의 리스트 생성
# next_station[i] = i번 역의 다음 역 번호
# prev_station[i] = i번 역의 이전 역 번호
MAX_ID = 1000001
next_station = [0] * MAX_ID
prev_station = [0] * MAX_ID

# 1. 초기 원형 이중 연결 리스트 구축 (O(N))
for i in range(N):
    curr = stations[i]
    
    # 다음 역: (i + 1) % N
    nxt = stations[(i + 1) % N]
    
    # 이전 역: (i - 1 + N) % N (음수 인덱스 방지)
    prv = stations[(i - 1 + N) % N]
    
    next_station[curr] = nxt
    prev_station[curr] = prv

# 출력을 모아둘 리스트
results = []

# 2. M개의 명령 처리 (O(M))
for _ in range(M):
    line = input().split()
    cmd = line[0]
    i = int(line[1])
    
    if cmd == "BN":
        j = int(line[2])
        
        # i의 원래 다음 역을 찾음
        target_next = next_station[i]
        results.append(str(target_next))
        
        # i -> j -> target_next 연결
        next_station[i] = j
        prev_station[j] = i
        next_station[j] = target_next
        prev_station[target_next] = j
        
    elif cmd == "BP":
        j = int(line[2])
        
        # i의 원래 이전 역을 찾음
        target_prev = prev_station[i]
        results.append(str(target_prev))
        
        # target_prev -> j -> i 연결
        next_station[target_prev] = j
        prev_station[j] = target_prev
        next_station[j] = i
        prev_station[i] = j
        
    elif cmd == "CN":
        # i의 다음 역(삭제 대상)을 찾음
        to_remove = next_station[i]
        results.append(str(to_remove))
        
        # 삭제될 역의 다음 역을 찾음
        new_next = next_station[to_remove]
        
        # i -> new_next 연결 (to_remove 건너뛰기)
        next_station[i] = new_next
        prev_station[new_next] = i
        
        # (선택 사항) 삭제된 노드의 연결 정보 초기화
        # next_station[to_remove] = 0
        # prev_station[to_remove] = 0
        
    elif cmd == "CP":
        # i의 이전 역(삭제 대상)을 찾음
        to_remove = prev_station[i]
        results.append(str(to_remove))
        
        # 삭제될 역의 이전 역을 찾음
        new_prev = prev_station[to_remove]
        
        # new_prev -> i 연결 (to_remove 건너뛰기)
        next_station[new_prev] = i
        prev_station[i] = new_prev
        
        # (선택 사항) 삭제된 노드의 연결 정보 초기화
        # next_station[to_remove] = 0
        # prev_station[to_remove] = 0

# 3. 결과 한 번에 출력
print('\n'.join(results))