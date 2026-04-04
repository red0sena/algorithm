n = int(input())
m = 1000000007
A, B = [1, 1, 3], [1, 1, 2]

for i in range(3, n + 1):
    A.append((A[-1] + 2*A[-2] + 3*A[-3]) % m)
    B.append((B[-1] + B[-2] + B[-3]) % m)

print((A[n] - B[n] + m) % m if n > 1 else 0)