from itertools import combinations

n = int(input())
input_map = []
for _ in range(n):
    input_map.append(list(map(int, input().split(' '))))
ars_min = int(10e7)

arr = [i for i in range(1, n+1)]
combi = list(combinations(arr, len(arr)//2))
for i in range(0, len(combi)//2):
    start_sum = 0
    for combi_start in combinations(combi[i], 2):
        start_sum += input_map[combi_start[0]-1][combi_start[1]-1]
        start_sum += input_map[combi_start[1]-1][combi_start[0]-1]
    link_sum = 0
    for combi_link in combinations(combi[-(i+1)], 2):

        link_sum += input_map[combi_link[0]-1][combi_link[1]-1]
        link_sum += input_map[combi_link[1]-1][combi_link[0]-1]
    ars_min = min(abs(link_sum - start_sum), ars_min)

print(ars_min)