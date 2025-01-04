while True:
    # 한 줄씩 입력을 받습니다.
    A, B = map(int, input().split())
    
    # 입력이 "0 0"이면 종료합니다.
    if A == 0 and B == 0:
        break
    
    # A + B의 결과를 출력합니다.
    print(A + B)
