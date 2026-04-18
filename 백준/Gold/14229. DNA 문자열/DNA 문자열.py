import sys
from collections import deque

def solve():
    # 입력 받기 (공백 제거)
    s = sys.stdin.readline().strip()
    if not s:
        return

    # DNA 염기 서열
    bases = ['A', 'C', 'G', 'T']
    
    # BFS를 위한 큐 생성
    queue = deque(bases)
    
    while queue:
        current = queue.popleft()
        
        # 현재 문자열이 S에 포함되어 있지 않으면 즉시 출력 후 종료
        if current not in s:
            print(current)
            return
        
        # S의 길이가 2000이므로, 정답 문자열의 길이는 그리 길지 않을 것입니다.
        # 포함되어 있다면 뒤에 A, C, G, T를 붙여서 다음 단계로 진행
        for base in bases:
            queue.append(current + base)

if __name__ == "__main__":
    solve()