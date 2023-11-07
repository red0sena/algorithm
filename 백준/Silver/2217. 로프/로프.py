import sys 

N = int(sys.stdin.readline())

rope_list = []

for _ in range(N):
    rope_list.append(int(sys.stdin.readline()))

rope_list.sort()

i = 0
max_val = -1
while(N):
    rope_weight = rope_list[i] * N 
    if max_val < rope_weight:
        max_val = rope_weight
    i += 1
    N -= 1

print(max_val)
