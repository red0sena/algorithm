def solve():
    import sys
    input = sys.stdin.readline

    game_no = 1
    # 방향별 이동 좌표: U, D, L, R
    moves = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    
    while True:
        line = input().split()
        if not line:
            break
        R, C = map(int, line)
        if R == 0 and C == 0:
            break

        board = [list(input().rstrip('\n')) for _ in range(R)]
        keys = input().strip()

        # underlying : 각 칸의 바닥 정보 (벽 '#', 일반 바닥 '.', 목표 '+')
        underlying = [['.' for _ in range(C)] for _ in range(R)]
        # 캐릭터 위치
        char_r = char_c = -1

        for i in range(R):
            for j in range(C):
                ch = board[i][j]
                if ch == '#':
                    underlying[i][j] = '#'
                elif ch in ('.', 'b', 'w'):
                    underlying[i][j] = '.'
                elif ch in ('+', 'B', 'W'):
                    underlying[i][j] = '+'
                # 저장 후, 찾기: 캐릭터는 'w' 혹은 'W'
                if ch in ('w', 'W'):
                    char_r, char_c = i, j

        def update_cell(i, j, obj):
            """ i,j에 obj('w'/'W' 또는 'b'/'B')를 놓을 때 underlying에 따라 결정 """
            if obj in ('w', 'W'):
                board[i][j] = 'W' if underlying[i][j] == '+' else 'w'
            elif obj in ('b', 'B'):
                board[i][j] = 'B' if underlying[i][j] == '+' else 'b'
            else:
                board[i][j] = underlying[i][j]

        def is_empty(i, j):
            # 빈 칸: 대상 셀에 캐릭터나 박스가 없고, 벽이 아닌 경우
            return board[i][j] in ('.', '+')
        
        # 함수: 현재 게임 상태가 complete인지 (모든 박스가 목표 위에 있는지)
        def game_complete():
            for i in range(R):
                for j in range(C):
                    if board[i][j] == 'b':  # 바닥 위에 있는 박스
                        return False
            return True

        game_done = False

        for key in keys:
            if game_complete():
                game_done = True
                break

            dr, dc = moves[key]
            nr, nc = char_r + dr, char_c + dc

            # 이동할 칸에 벽이면 움직이지 않음.
            if board[nr][nc] == '#':
                continue
            # 이동할 칸에 박스가 있을 경우
            if board[nr][nc] in ('b', 'B'):
                # 박스를 밀 위치
                nr2, nc2 = nr + dr, nc + dc
                if not is_empty(nr2, nc2):
                    continue  # 밀 수 없는 경우
                # 박스 이동: 박스가 도착하는 칸은 underlying에 따라 'b' 또는 'B'
                update_cell(nr2, nc2, 'b')
                # 캐릭터가 박스가 있던 칸으로 이동
                update_cell(nr, nc, 'w')
                # 원래 캐릭터가 있던 칸은 underlying로 복원
                board[char_r][char_c] = underlying[char_r][char_c]
                # 캐릭터 위치 갱신
                char_r, char_c = nr, nc
            # 빈 칸일 경우
            elif board[nr][nc] in ('.', '+'):
                # 현재 위치 복원
                board[char_r][char_c] = underlying[char_r][char_c]
                # 캐릭터 이동
                update_cell(nr, nc, 'w')
                char_r, char_c = nr, nc
            # 그 외에는 아무것도 하지 않음

        status = "complete" if game_complete() else "incomplete"

        sys.stdout.write(f"Game {game_no}: {status}\n")
        for i in range(R):
            sys.stdout.write("".join(board[i]) + "\n")
        game_no += 1

if __name__ == '__main__':
    solve()
