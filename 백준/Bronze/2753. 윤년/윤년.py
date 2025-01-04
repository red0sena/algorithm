# 연도를 입력받습니다.
year = int(input())

# 윤년 판별
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(1)  # 윤년일 경우 1 출력
else:
    print(0)  # 윤년이 아닐 경우 0 출력
