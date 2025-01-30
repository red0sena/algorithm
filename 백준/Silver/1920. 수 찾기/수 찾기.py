
n = int(input())
input_list = list(map(int, input().split()))
m = int(input())
input_list.sort()


a = list(map(int, input().split()))
for b in a:
    flag = True
    min_val = 0
    max_val = len(input_list) - 1
    while min_val <= max_val:
        mid = (min_val + max_val) // 2
        if input_list[mid] > b:
            max_val = mid - 1
        elif input_list[mid] < b:
            min_val = mid + 1
        else:
            print(1)
            flag = False
            break

    if flag:
        print(0)
