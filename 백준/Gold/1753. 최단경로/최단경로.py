import sys
import heapq

def main():
    input_data = sys.stdin.read().splitlines()  # 전체 입력을 한 번에 읽습니다.
    V, E = map(int, input_data[0].split())
    start = int(input_data[1])
    
    # 그래프 초기화 (인접 리스트)
    graph = [[] for _ in range(V + 1)]
    for line in input_data[2:]:
        u, v, w = map(int, line.split())
        graph[u].append((v, w))
    
    INF = float('inf')
    distances = [INF] * (V + 1)
    distances[start] = 0
    heap = [(0, start)]
    
    # 다익스트라 알고리즘
    while heap:
        current_distance, current_node = heapq.heappop(heap)
        if current_distance > distances[current_node]:
            continue
        
        for next_node, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(heap, (distance, next_node))
    
    # 결과를 리스트에 저장 후 한 번에 출력
    output = []
    for i in range(1, V + 1):
        output.append("INF" if distances[i] == INF else str(distances[i]))
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
