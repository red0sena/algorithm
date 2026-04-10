from functools import cache

def solve():
    N = int(input())

    # x 이하의 자연수 중 '666'이 포함된 숫자의 개수를 반환하는 함수
    def count_666(x):
        s = str(x)
        
        @cache
        def dp(i, less, six):
            # 💡 핵심 1: '666'이 완성된 순간, 남은 자릿수는 볼 필요도 없이 O(1)로 끝냄
            if six == 3: 
                return 10**(len(s) - i) if less else int(s[i:] or 0) + 1
            if i == len(s): 
                return 0
                
            limit = 9 if less else int(s[i])
            return sum(dp(i+1, less or d < limit, six + 1 if d == 6 else 0) for d in range(limit + 1))
            
        return dp(0, False, 0)

    # 💡 핵심 2: 정답을 이분 탐색(Binary Search)으로 한 방에 꽂아버림
    lo, hi = 666, 10**11
    while lo < hi:
        mid = (lo + hi) // 2
        if count_666(mid) >= N:
            hi = mid # N번째를 채웠다면 더 작은 숫자가 있는지 범위를 내림
        else:
            lo = mid + 1

    print(lo)

if __name__ == '__main__':
    solve()