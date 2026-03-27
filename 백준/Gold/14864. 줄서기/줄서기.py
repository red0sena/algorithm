import sys

def solve_14864():
    input = sys.stdin.read().split()
    if not input: return
    
    n, m = int(input[0]), int(input[1])
    # 각 위치의 초기 번호를 인덱스 값으로 설정
    ans = [i for i in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        x = int(input[idx])
        y = int(input[idx+1])
        ans[x] += 1
        ans[y] -= 1
        idx += 2
        
    # 유효성 검사: 1~N까지 숫자가 모두 한 번씩 쓰였는지 확인
    check = [False] * (n + 1)
    for i in range(1, n + 1):
        val = ans[i]
        if val < 1 or val > n or check[val]:
            print("-1")
            return
        check[val] = True
        
    print(*(ans[1:]))

solve_14864()