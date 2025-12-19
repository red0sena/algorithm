import sys

def solve():
    input_data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(input_data)

    n = next(it); m = next(it); k = next(it)
    cap = k - 1

    parent = list(range(n + 1))
    size = [1] * (n + 1)

    candy = [0] * (n + 1)
    for i in range(1, n + 1):
        candy[i] = next(it)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra = find(a); rb = find(b)
        if ra == rb:
            return
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        candy[ra] += candy[rb]

    for _ in range(m):
        a = next(it); b = next(it)
        union(a, b)

    # buckets[w] = 무게 w 그룹들의 가치(사탕합)
    buckets = [[] for _ in range(cap + 1)]
    for i in range(1, n + 1):
        if parent[i] == i:
            w = size[i]
            if w <= cap:
                buckets[w].append(candy[i])

    # 무게별로 "어차피 담을 수 있는 개수"만 남기기
    items = []
    for w in range(1, cap + 1):
        if buckets[w]:
            buckets[w].sort(reverse=True)
            limit = cap // w
            if limit:
                items.extend((w, v) for v in buckets[w][:limit])

    dp = [0] * (cap + 1)

    # 0/1 knapsack
    for w, v in items:
        for j in range(cap, w - 1, -1):
            nv = dp[j - w] + v
            if nv > dp[j]:
                dp[j] = nv

    print(dp[cap])

if __name__ == "__main__":
    solve()