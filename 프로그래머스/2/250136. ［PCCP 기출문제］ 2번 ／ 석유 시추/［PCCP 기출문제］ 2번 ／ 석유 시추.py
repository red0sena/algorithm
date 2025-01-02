from collections import deque
global_oil_count = 0

def solution(land):
    oil_map = [[-1] * len(land[0]) for _ in range(len(land))]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


    def count_oil(start_x, start_y):
        global global_oil_count
        queue = deque([(start_x, start_y)])
        # visited = [[-1] * len(land[0]) for _ in range(len(land))]
        oil_map[start_x][start_y] = 1
        visited_list = [(start_x, start_y)]
        count = 0
        while queue:
            count += 1
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(land) and 0 <= ny < len(land[0]) and (land[nx][ny] == 1):
                    if oil_map[nx][ny] != 1:
                        oil_map[nx][ny] = 1
                        queue.append((nx, ny))
                        visited_list.append((nx, ny))
        global_oil_count += 1
        for x, y in visited_list:
            oil_map[x][y] = (global_oil_count, count)

        return count, global_oil_count

    res = -1
    # 석유가 있나 열별로 찾기
    for column in range(len(land[0])):
        # 이 열에서 석유 개수
        oil_this_column = 0
        # 이 열에서 이미 count한 석유
        already_count_list = []
        for row in range(len(land)):
            # 만약 석유가 있는 땅이면
            if land[row][column] == 1:
                # 아직 이 땅의 석유 범위를 세지 않았다면
                if oil_map[row][column] == -1:
                    # 석유범위를 세고
                    count_oil_return = count_oil(row, column)
                    # 열에서 석유 숫자 넣고
                    oil_this_column += count_oil_return[0]
                    # 이미 셋으니까 count on
                    already_count_list.append(count_oil_return[1])
                else:
                    # 이미 이땅에서 석유가 count가 되었다면 이전에 count했던 정보 가져오기
                    oil_count = oil_map[row][column]
                    # 이 열에서 이 범위의 석유를 이미 count했다면
                    if oil_count[0] in already_count_list:
                        # pass
                        pass
                    # 이 열에서 석유 범위를 count 안했다면
                    else:
                        # 석유 count 그리고 count 목록에 추가
                        oil_this_column += oil_count[1]
                        already_count_list.append(oil_count[0])
        # 열 중에서 최대값 찾기
        res = max(oil_this_column, res)

    return res


print(
    solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]])
)