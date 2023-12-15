N = int(input())
input_list = []
for _ in range(N):
    num = int(input())
    input_list.append(num)

dp_0 = [1, 0]
dp_1 = [0, 1]


for input in input_list:
    if len(dp_0) <= input:
        for i in range(len(dp_0), input+1):
            dp_0.append(dp_0[i-2] + dp_0[i-1])
            dp_1.append(dp_1[i-2] + dp_1[i-1])
        print(dp_0[-1], dp_1[-1])
    else:
        print(dp_0[input], dp_1[input])