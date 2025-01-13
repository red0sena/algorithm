t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    dam = 1
    for i in range(n):
        dam *= m-i
        dam/=1+i
    print(int(dam))
