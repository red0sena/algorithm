from collections import defaultdict
import heapq


def solution(tickets):
    # 인접 리스트 생성: 각 공항에서 출발하는 도착지를 사전순으로 저장
    graph = defaultdict(list)
    for src, dst in sorted(tickets):  # 사전순으로 정렬
        graph[src].append(dst)

    # DFS를 이용한 Hierholzer 알고리즘
    result = []
    def dfs(airport):
        # 현재 공항에서 갈 수 있는 도착지를 사전순으로 탐색
        while graph[airport]:
            next_airport = graph[airport].pop(0)  # 사전순으로 첫 번째 도착지 선택
            dfs(next_airport)
        result.append(airport)  # 더 이상 갈 곳이 없으면 결과에 추가

    dfs("ICN")  # JFK에서 시작
    return result[::-1]  # 결과 역순으로 반환