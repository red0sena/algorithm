def solution(A,B):
    A.sort()
    B.sort(reverse=True)

    res = 0
    for a, b in zip(A, B):
        res += (a*b)


    return res