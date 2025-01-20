n = int(input())
max_value = -int(10e100)



input_list = list(map(int, input().split(" ")))

max_index = len(input_list)-1

current_sum = 0

for i in range(n):
    current_sum += input_list[i]
    if current_sum > max_value:
        max_value = current_sum
    if current_sum < 0:
        current_sum = 0


print(max_value)