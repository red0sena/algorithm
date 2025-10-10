import sys

def solve():
    # 입력 받기
    N, K = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    # piece_map: 각 칸에 쌓인 말의 번호를 저장 (3D 리스트)
    piece_map = [[[] for _ in range(N)] for _ in range(N)]
    
    # pieces: 각 말의 정보를 저장 {말 번호: [행, 열, 방향]}
    pieces = {}

    for i in range(1, K + 1):
        r, c, d = map(int, sys.stdin.readline().split())
        # 0-based 인덱스로 변환
        pieces[i] = [r - 1, c - 1, d - 1]
        piece_map[r - 1][c - 1].append(i)

    # 방향 벡터 (우, 좌, 상, 하) / 문제의 1,2,3,4 와 인덱스 0,1,2,3 매칭
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]

    # 방향을 반대로 바꾸는 맵
    reverse_dir = [1, 0, 3, 2]

    turn = 1
    while turn <= 1000:
        # 1번 말부터 K번 말까지 순서대로 이동
        for p_num in range(1, K + 1):
            r, c, d = pieces[p_num]

            # 현재 말이 쌓여있는 스택에서 자신의 위치(인덱스) 찾기
            stack = piece_map[r][c]
            try:
                p_idx = stack.index(p_num)
            except ValueError:
                # 이 경우는 발생하면 안 됨 (로직 오류)
                continue
            
            # 함께 움직일 말들 분리
            moving_group = stack[p_idx:]
            piece_map[r][c] = stack[:p_idx] # 기존 위치에서는 제거

            # 다음 위치 계산
            nr, nc = r + dr[d], c + dc[d]

            # 1. 파란색이거나 맵을 벗어나는 경우
            if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] == 2:
                # 방향을 반대로 변경
                d = reverse_dir[d]
                pieces[p_num][2] = d
                
                # 변경된 방향으로 다음 위치 다시 계산
                nr, nc = r + dr[d], c + dc[d]

                # 방향 바꾼 후에도 파란색이거나 맵 밖이면 이동하지 않음
                if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] == 2:
                    piece_map[r][c].extend(moving_group) # 원래 위치로 복귀
                    continue

            # 2. 빨간색인 경우 (이동 후 순서 뒤집기)
            if board[nr][nc] == 1:
                moving_group.reverse()
            
            # 3. 흰색 또는 (파란색에서 방향 바꾼 후) 빨간색 칸으로 이동
            piece_map[nr][nc].extend(moving_group)

            # 이동한 말들의 위치 정보 업데이트
            for moved_p_num in moving_group:
                pieces[moved_p_num][0], pieces[moved_p_num][1] = nr, nc
            
            # 종료 조건 확인
            if len(piece_map[nr][nc]) >= 4:
                print(turn)
                return

        turn += 1

    # 1000턴이 지나도 끝나지 않은 경우
    print(-1)

solve()