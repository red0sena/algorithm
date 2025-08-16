def solution(info, edges):
    from collections import defaultdict
    
    n = len(info)
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)  # 무방향 입력이지만, 후보 관리가 핵심이라 양방향 둬도 OK

    answer = 0
    # visited를 비트마스크로 관리 (프루닝용)
    from functools import lru_cache

    # 현재 후보 집합은 리스트/튜플로 유지(정렬된 튜플로 캐시 키에 사용)
    def dfs(sheep, wolf, visited_mask, candidates):
        nonlocal answer
        answer = max(answer, sheep)

        # 메모이제이션: 같은 visited_mask에서 sheep가 이전보다 작/같으면 중단
        # dp에 최대 sheep 저장
        if visited_best[visited_mask] >= sheep:
            return
        visited_best[visited_mask] = sheep

        for i, nxt in enumerate(candidates):
            if (visited_mask >> nxt) & 1:
                continue  # 이미 방문
            ns, nw = sheep, wolf
            if info[nxt] == 0:
                ns += 1
            else:
                nw += 1

            if nw >= ns:
                continue  # 조건 위반

            # 다음 후보 집합 만들기: 현재 후보에서 nxt 제거 + nxt의 인접 노드 추가
            new_candidates = list(candidates[:i] + candidates[i+1:])
            # 인접 노드 중 아직 방문하지 않은 것들을 후보에 추가
            for nei in tree[nxt]:
                if ((visited_mask >> nei) & 1) == 0:
                    # 부모 방문 여부와 무관하게, 현재 경로에서 한 번이라도 상위가 방문되면 결국 연결이 열림
                    # 다만 실제 트리라면 '부모가 방문되었을 때 자식 추가'가 직관적
                    # 이 구현은 무방향 + 후보 집합으로도 동일 효과
                    if nei not in new_candidates:
                        new_candidates.append(nei)

            dfs(ns, nw, visited_mask | (1 << nxt), tuple(new_candidates))

    # 시작: 0 방문
    sheep = 1 if info[0] == 0 else 0
    wolf = 1 if info[0] == 1 else 0
    if wolf >= sheep:
        return 0  # 시작이 늑대면 바로 끝(문제 조건상 보통 0은 양)

    # 초기 후보: 0의 인접 노드들
    start_candidates = []
    for nei in tree[0]:
        if nei != 0:
            start_candidates.append(nei)

    visited_best = [ -1 ] * (1 << n)  # 해당 방문 마스크에서 얻은 최대 sheep
    dfs(sheep, wolf, 1 << 0, tuple(start_candidates))
    return answer
