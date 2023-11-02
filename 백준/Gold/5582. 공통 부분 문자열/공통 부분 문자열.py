import sys

input1 = sys.stdin.readline().rstrip()
input2 = sys.stdin.readline().rstrip()

dp_array = [[0] * (len(input2)+1) for _ in range(0, 2)]

max_value = 0

for i in range(0, len(input1)):
    dp_array[0] = dp_array[1]
    dp_array[1] = [0] * (len(input2)+1)
    for j in range(0, len(input2)):
        if input1[i] == input2[j]:
            dp_array[1][j] = dp_array[0][j-1] + 1
            if max_value < dp_array[1][j]:
                max_value = dp_array[1][j]


print(max_value)