import sys

# 입력 속도를 높이기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    M = int(input())
    MOD = 1000000007
    
    total_expected_value = 0
    
    for _ in range(M):
        N, S = map(int, input().split())
        
        # 기댓값 = S / N
        # 모듈러 역원을 이용한 나눗셈 변환: S * (N^(MOD-2)) % MOD
        # pow(base, exp, mod)는 base^exp % mod를 빠르게 계산함
        inverse_N = pow(N, MOD - 2, MOD)
        expected_value = (S * inverse_N) % MOD
        
        total_expected_value = (total_expected_value + expected_value) % MOD
        
    print(total_expected_value)

if __name__ == "__main__":
    solve()