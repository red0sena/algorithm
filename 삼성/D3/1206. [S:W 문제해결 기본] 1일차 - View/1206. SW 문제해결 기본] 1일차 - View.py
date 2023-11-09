T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    input_list = list(map(int, input().split()))
    count = 0 
 
    now_building = input_list[0]
    if input_list[1] < now_building and input_list[2] < now_building:
        max_near_building = max([input_list[1], input_list[2]])
        count += now_building- max_near_building
 
    now_building = input_list[1]
    if input_list[0] < now_building and input_list[2] < now_building and input_list[3] < now_building:
        max_near_building = max([input_list[0], input_list[2], input_list[3]])
        count += now_building- max_near_building
 
    now_building = input_list[-2]
    if input_list[-4] < now_building and input_list[-3] < now_building and input_list[-1] < now_building:
        max_near_building = max([input_list[-4], input_list[-3], input_list[-1]])
        count += now_building- max_near_building
 
    now_building = input_list[-1]
    if input_list[-3] < now_building and input_list[-2] < now_building:
        max_near_building = max([input_list[-3], input_list[-2]])
        count += now_building- max_near_building
 
 
 
    for i in range(2, len(input_list)-2):
        now_building = input_list[i]
        if input_list[i-2] < now_building and input_list[i-1] < now_building and input_list[i+1] < now_building and input_list[i+2] < now_building:
            max_near_building = max([input_list[i-2], input_list[i-1], input_list[i+1], input_list[i+2]])
            count += now_building -max_near_building
 
    print(f"#{test_case} {count}")