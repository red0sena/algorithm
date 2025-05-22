import sys
input = sys.stdin.readline

def main():
    N = int(input())
    M = int(input())
    S = input().rstrip()

    cnt = 0   # 현재 연속된 "IOI" 패턴 수
    ans = 0   # 찾은 P_N 패턴 수
    i = 0
    # i+2 < M 조건으로 S[i:i+3] 접근이 항상 유효하도록 함
    while i + 2 < M:
        # "I","O","I" 연속 등장 확인
        if S[i] == 'I' and S[i+1] == 'O' and S[i+2] == 'I':
            cnt += 1
            # 현재 연속된 "IOI"가 N개 이상이면 P_N 패턴 하나 발견
            if cnt >= N:
                ans += 1
            i += 2  # 중첩 허용하며 다음 검사 위치로 점프
        else:
            cnt = 0
            i += 1

    print(ans)

if __name__ == "__main__":
    main()
