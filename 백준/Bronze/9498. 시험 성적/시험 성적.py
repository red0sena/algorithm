# 시험 점수를 입력받습니다.
score = int(input())

# 점수에 따라 성적을 출력합니다.
if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
else:
    print("F")
