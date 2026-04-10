import sys
# 파이썬의 기본 재귀 깊이 제한을 늘려줍니다. (안전장치)
sys.setrecursionlimit(10**6)

def solve():
    input = sys.stdin.readline
    n = int(input())
    m = int(input())

    # graph[x] = (y, k) : x를 만드는데 y가 k개 필요하다
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y, k = map(int, input().split())
        graph[x].append((y, k))

    # memo[x]: x를 만들기 위해 필요한 기본 부품들의 개수 (딕셔너리로 저장)
    # None이면 아직 계산 안 됨을 의미
    memo = [None] * (n + 1)

    def dfs(node):
        # 1. 이미 수첩(memo)에 적혀있다면, 조립법을 다시 찾지 않고 바로 꺼내 쓴다! (유레카 포인트 1)
        if memo[node] is not None:
            return memo[node]

        # 2. 설명서(graph)를 봤는데 하위 부품이 없다면? -> 이것이 기본 부품! (유레카 포인트 2)
        if not graph[node]:
            memo[node] = {node: 1} # "나 자신 1개가 필요해" 라고 메모
            return memo[node]

        # 3. 조립해야 하는 중간 부품이라면 하위 부품들을 모아본다.
        parts_needed = {}
        for next_node, count in graph[node]:
            # 하위 부품을 만들기 위해 필요한 기본 부품들을 재귀로 가져옴
            sub_parts = dfs(next_node)
            
            # 가져온 기본 부품들에 '필요한 개수(count)'를 곱해서 내 수첩에 합산
            for part_num, part_count in sub_parts.items():
                parts_needed[part_num] = parts_needed.get(part_num, 0) + (part_count * count)

        # 다 모았으면 수첩에 기록하고 반환
        memo[node] = parts_needed
        return memo[node]

    # 완제품 N에 대해서만 물어보면 알아서 연쇄적으로 계산됨
    result = dfs(n)

    # 결과를 부품 번호 오름차순으로 출력
    for part_num in sorted(result.keys()):
        print(f"{part_num} {result[part_num]}")

if __name__ == '__main__':
    solve()