import sys
from collections import deque

# 가수의 수(N)와 보조 PD의 수(M)를 입력받음
n, m = map(int, sys.stdin.readline().split())

# 각 가수의 진입 차수(in-degree)를 저장할 리스트
in_degree = [0] * (n + 1)

# 각 가수에 대한 인접 리스트 (그래프)
# graph[i]는 가수 i 다음에 나와야 할 가수들의 리스트
graph = [[] for _ in range(n + 1)]

# M개의 보조 PD 정보를 입력받아 그래프를 구성
for _ in range(m):
    pd_list = list(map(int, sys.stdin.readline().split()))
    # pd_list[0]은 해당 PD가 담당한 가수의 수이므로, 순서 정보는 인덱스 1부터 시작
    for i in range(1, len(pd_list) - 1):
        # pd_list[i] -> pd_list[i+1] 순서를 그래프에 추가
        graph[pd_list[i]].append(pd_list[i+1])
        # pd_list[i+1]의 진입 차수 증가
        in_degree[pd_list[i+1]] += 1

# 위상 정렬 결과를 저장할 리스트
result = []
# 진입 차수가 0인 노드(가수)들을 담을 큐
q = deque()

# 초기에 진입 차수가 0인 모든 노드를 큐에 삽입
for i in range(1, n + 1):
    if in_degree[i] == 0:
        q.append(i)

# 큐가 빌 때까지 반복
while q:
    # 큐에서 노드를 하나 꺼내 결과 리스트에 추가
    current_singer = q.popleft()
    result.append(current_singer)

    # 현재 노드와 연결된(다음에 나와야 할) 모든 노드에 대해
    for next_singer in graph[current_singer]:
        # 해당 노드들의 진입 차수를 1 감소
        in_degree[next_singer] -= 1
        # 만약 진입 차수가 0이 되면 큐에 삽입
        if in_degree[next_singer] == 0:
            q.append(next_singer)

# 결과 확인
# result 리스트의 길이가 전체 가수의 수(N)와 같다면 위상 정렬 성공
if len(result) == n:
    for singer in result:
        print(singer)
# 같지 않다면 그래프에 사이클이 존재하여 순서를 정할 수 없음
else:
    print(0)