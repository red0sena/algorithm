# 두 정수 A와 B를 입력받습니다.
A, B = map(int, input().split())

# A와 B를 비교하여 결과를 출력합니다.
if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")
