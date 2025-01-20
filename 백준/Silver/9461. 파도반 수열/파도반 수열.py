T = int(input())



for _ in range(T):
    n = int(input())
    P = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    if n < 10:
        print(P[n-1])
    else:
        for i in range(10, n+1):
            P.append(P[i-2] + P[i-3])

        print(P[-2])

