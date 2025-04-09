def solve():
    import sys
    from collections import deque
    input = sys.stdin.readline

    # B : 판단 데이터의 개수 (각각 낮음, 높음)
    B = int(input().strip())
    
    # 낮음을 판단하는 데이터 (차고의 낮음에 해당하면 -1의 기여도를 줌)
    low_patterns = [input().strip() for _ in range(B)]
    
    # 높음을 판단하는 데이터 (차고의 높음에 해당하면 +1의 기여도를 줌)
    high_patterns = [input().strip() for _ in range(B)]
    
    # 실시간 데이터의 개수 및 문자열 리스트
    N = int(input().strip())
    realtime_data = [input().strip() for _ in range(N)]
    
    # Aho-Corasick 알고리즘용 트라이 자료구조 구성
    # 각 노드는 다음 정보를 가짐: 
    #   'next': 다음 노드 정보를 담는 dict (문자->노드번호),
    #   'fail': 실패 함수(실패 시 이동할 노드 번호),
    #   'out': 이 노드에서 끝나는 패턴들의 총 점수 (높음은 +1, 낮음은 -1)
    trie = [{'next': {}, 'fail': 0, 'out': 0}]
    
    def add_pattern(pattern, value):
        node = 0
        for ch in pattern:
            if ch not in trie[node]['next']:
                trie[node]['next'][ch] = len(trie)
                trie.append({'next': {}, 'fail': 0, 'out': 0})
            node = trie[node]['next'][ch]
        trie[node]['out'] += value

    # 낮음 판단 데이터는 기여도가 -1
    for pattern in low_patterns:
        add_pattern(pattern, -1)
    
    # 높음 판단 데이터는 기여도가 +1
    for pattern in high_patterns:
        add_pattern(pattern, +1)
    
    # 실패 포인터(fail)을 계산하기 위해 BFS 수행
    q = deque()
    # 루트 노드의 자식들은 실패 노드를 0으로 초기화
    for ch, nxt in trie[0]['next'].items():
        trie[nxt]['fail'] = 0
        q.append(nxt)
    
    while q:
        curr = q.popleft()
        for ch, nxt in trie[curr]['next'].items():
            f = trie[curr]['fail']
            # 실패 포인터를 따라 ch가 있는 노드 찾기
            while f and ch not in trie[f]['next']:
                f = trie[f]['fail']
            if ch in trie[f]['next']:
                trie[nxt]['fail'] = trie[f]['next'][ch]
            else:
                trie[nxt]['fail'] = 0
            # 현재 노드의 out 값에 실패 노드의 out 값을 누적하여, 
            # 현재 노드에 해당하는 모든 패턴의 기여도를 합산
            trie[nxt]['out'] += trie[trie[nxt]['fail']]['out']
            q.append(nxt)
    
    # 각 실시간 데이터에 대해 검색 및 결과 출력
    output_lines = []
    for text in realtime_data:
        node = 0
        score = 0  # 현재 차고(C)를 누적할 점수
        for ch in text:
            # 현재 문자에 대해 트라이에서 다음 노드가 없으면 실패 링크를 따라 이동
            while node and ch not in trie[node]['next']:
                node = trie[node]['fail']
            if ch in trie[node]['next']:
                node = trie[node]['next'][ch]
            # 현재 노드에서 대응하는 패턴의 결과를 score에 더함
            score += trie[node]['out']
        # score에 따라 결과 결정: C > 0이면 "LOW", C < 0이면 "HIGH", 0이면 "GOOD"
        if score > 0:
            output_lines.append("LOW " + str(score))
        elif score < 0:
            output_lines.append("HIGH " + str(-score))
        else:
            output_lines.append("GOOD")
    
    sys.stdout.write("\n".join(output_lines))
    
if __name__ == '__main__':
    solve()
