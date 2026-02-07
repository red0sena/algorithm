import sys

def solve():
    s = sys.stdin.readline().strip()
    
    # 1. 전처리: 짝수 길이 팰린드롬을 처리하기 위해 문자 사이마다 '#' 삽입
    # 예: 'aba' -> '#a#b#a#', 'abba' -> '#a#b#b#a#'
    t = ['#'] * (2 * len(s) + 1)
    for i in range(len(s)):
        t[2 * i + 1] = s[i]
    
    n = len(t)
    p = [0] * n  # 각 위치에서의 팰린드롬 반지름 길이를 저장할 배열
    
    c = 0 # current center: 현재 가장 우측으로 뻗은 팰린드롬의 중심
    r = 0 # right boundary: 그 팰린드롬의 가장 오른쪽 경계 (c + p[c])
    
    # 2. 매내처 알고리즘 수행
    for i in range(n):
        # i가 r 안쪽에 있다면, 대칭점(mirror)을 이용해 p[i] 초기값 설정
        if i < r:
            mirror = 2 * c - i  # c를 기준으로 i의 대칭점
            p[i] = min(r - i, p[mirror])
        
        # 중심 i에서 팰린드롬 확장 시도
        # 경계를 벗어나지 않고, 좌우 문자가 같다면 반지름 증가
        while (i - p[i] - 1 >= 0 and 
               i + p[i] + 1 < n and 
               t[i - p[i] - 1] == t[i + p[i] + 1]):
            p[i] += 1
        
        # 3. 중심 및 우측 경계 갱신
        # 새로 구한 팰린드롬이 기존 r보다 더 오른쪽으로 뻗어나간다면 갱신
        if i + p[i] > r:
            c = i
            r = i + p[i]
            
    # 4. 정답 출력
    # 변형된 문자열 t에서의 반지름 길이 p[i]는 원본 문자열 s에서의 팰린드롬 길이와 같습니다.
    print(max(p))

if __name__ == "__main__":
    solve()