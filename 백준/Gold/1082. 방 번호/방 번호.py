import sys
input = sys.stdin.readline

def main():
    N = int(input().strip())
    P = list(map(int, input().split()))
    M = int(input().strip())

    # 1) dp_length_exact[c] = 비용이 정확히 c일 때 만들 수 있는 최대 자릿수 (가능하지 않으면 -inf)
    INF_NEG = -10**9
    dp_length_exact = [INF_NEG] * (M + 1)
    dp_length_exact[0] = 0

    for cost in range(1, M + 1):
        best = INF_NEG
        for d in range(N):
            cd = P[d]
            if cost >= cd and dp_length_exact[cost - cd] != INF_NEG:
                best = max(best, dp_length_exact[cost - cd] + 1)
        dp_length_exact[cost] = best

    # 2) dp_length_max_le[c] = 비용 ≤ c일 때 얻을 수 있는 최대 자릿수
    dp_length_max_le = [0] * (M + 1)
    dp_length_max_le[0] = max(0, dp_length_exact[0])  # =0
    for c in range(1, M + 1):
        dp_length_max_le[c] = max(dp_length_max_le[c - 1], dp_length_exact[c])

    # 3) 최대 자릿수 후보 (순수하게 비용 ≤ M인 경우)
    max_raw_len = dp_length_max_le[M]

    # 4) 실제로 첫 자리가 0이 될 수 없으므로, 가능한 최대 길이 L을 탐색
    chosen_L = 0
    for L in range(max_raw_len, 1, -1):
        # L >= 2인 경우, 첫 자리 d는 1..N-1 중에서 골라야 한다
        found = False
        for d in range(N - 1, 0, -1):
            if P[d] <= M:
                rem = M - P[d]
                # 나머지 L-1자리를 비용 ≤ rem으로 채울 수 있는지 검사
                if dp_length_max_le[rem] >= L - 1:
                    chosen_L = L
                    found = True
                    break
        if found:
            break

    # 5) 만약 L >= 2인 해가 없으면, L=1로 (한 자리로만 구성)
    if chosen_L <= 1:
        single_digit = -1
        for d in range(N - 1, -1, -1):
            if P[d] <= M:
                single_digit = d
                break
        print(single_digit)
        return

    # 6) Reconstruction: chosen_L 자릿수를 하나씩 채워간다
    result = []
    balance = M
    for pos in range(1, chosen_L + 1):
        for d in range(N - 1, -1, -1):
            # 첫 자리일 때, 다자릿수라면 0은 불가
            if pos == 1 and chosen_L > 1 and d == 0:
                continue
            cd = P[d]
            if cd > balance:
                continue
            rem = balance - cd
            # 남은 자릿수 = chosen_L - pos
            need = chosen_L - pos
            # 남은 need자리를 채울 수 있는지
            if dp_length_max_le[rem] >= need:
                result.append(str(d))
                balance = rem
                break

    print(''.join(result))


if __name__ == "__main__":
    main()
