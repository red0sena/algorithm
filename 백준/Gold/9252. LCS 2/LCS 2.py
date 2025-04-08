def solution():
    import sys
    input = sys.stdin.readline

    # 두 문자열 입력 (strip()을 이용해 양쪽 공백 제거)
    A = input().strip()
    B = input().strip()
    n, m = len(A), len(B)
    
    # dp 테이블 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # 동적 계획법을 이용해 LCS 길이 계산
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # LCS의 길이 출력
    lcs_length = dp[n][m]
    print(lcs_length)
    
    # LCS 길이가 0이면, 둘째 줄 출력하지 않음
    if lcs_length == 0:
        return
    
    # LCS 재구성 (역추적)
    i, j = n, m
    lcs_chars = []
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            lcs_chars.append(A[i - 1])
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

    # 역순으로 수집한 LCS를 올바른 순서로 뒤집기
    lcs_chars.reverse()
    print(''.join(lcs_chars))


if __name__ == '__main__':
    solution()
