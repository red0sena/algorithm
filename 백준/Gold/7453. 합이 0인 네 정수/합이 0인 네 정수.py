import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    n = int(input())
    A, B, C, D = [], [], [], []
    for _ in range(n):
        a, b, c, d = map(int, input().split())
        A.append(a); B.append(b); C.append(c); D.append(d)

    # 1) A+B 모든 합의 빈도 카운트
    cnt_ab = defaultdict(int)
    for a in A:
        for b in B:
            cnt_ab[a + b] += 1

    # 2) C+D의 합에 대해 -(C+D)가 cnt_ab에 몇 개 있는지 합산
    ans = 0
    for c in C:
        for d in D:
            ans += cnt_ab.get(-(c + d), 0)

    print(ans)

if __name__ == "__main__":
    main()
