import sys

# 좌표 문자열(예: A1, B2)을 인덱스 (0, 0), (1, 1)로 변환
def pos_to_idx(pos):
    return ord(pos[0]) - ord('A'), int(pos[1]) - 1

def get_box(r, c):
    return (r // 3) * 3 + (c // 3)

def check(r, c, num, row_check, col_check, box_check):
    return not (row_check[r][num] or col_check[c][num] or box_check[get_box(r, c)][num])

def backtrack(idx, board, row_check, col_check, box_check, used_domino):
    if idx == 81:
        return True
    
    r, c = divmod(idx, 9)
    if board[r][c] != 0:
        return backtrack(idx + 1, board, row_check, col_check, box_check, used_domino)
    
    # 가로(0, 1) 또는 세로(1, 0)로 도미노 놓기 시도
    for dr, dc in [(0, 1), (1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 9 and 0 <= nc < 9 and board[nr][nc] == 0:
            # 사용할 숫자 쌍 (i, j) 선택
            for i in range(1, 10):
                for j in range(1, 10):
                    if i == j or used_domino[i][j]:
                        continue
                    
                    if check(r, c, i, row_check, col_check, box_check) and \
                       check(nr, nc, j, row_check, col_check, box_check):
                        
                        # 상태 기록
                        board[r][c], board[nr][nc] = i, j
                        row_check[r][i] = col_check[c][i] = box_check[get_box(r, c)][i] = True
                        row_check[nr][j] = col_check[nc][j] = box_check[get_box(nr, nc)][j] = True
                        used_domino[i][j] = used_domino[j][i] = True
                        
                        if backtrack(idx + 1, board, row_check, col_check, box_check, used_domino):
                            return True
                        
                        # 복구 (Backtracking)
                        used_domino[i][j] = used_domino[j][i] = False
                        row_check[r][i] = col_check[c][i] = box_check[get_box(r, c)][i] = False
                        row_check[nr][j] = col_check[nc][j] = box_check[get_box(nr, nc)][j] = False
                        board[r][c], board[nr][nc] = 0, 0
                        
    return False

def solve():
    tc = 1
    while True:
        line = sys.stdin.readline().split()
        if line[0] == '0':
            break
        
        N = int(line[0])
        board = [[0] * 9 for _ in range(9)]
        row_check = [[False] * 10 for _ in range(9)]
        col_check = [[False] * 10 for _ in range(9)]
        box_check = [[False] * 10 for _ in range(9)]
        used_domino = [[False] * 10 for _ in range(10)]
        
        # 1. 도미노 정보 입력
        for _ in range(N):
            u_val, u_pos, v_val, v_pos = sys.stdin.readline().split()
            u_val, v_val = int(u_val), int(v_val)
            ur, uc = pos_to_idx(u_pos)
            vr, vc = pos_to_idx(v_pos)
            
            board[ur][uc], board[vr][vc] = u_val, v_val
            used_domino[u_val][v_val] = used_domino[v_val][u_val] = True
            
            for r, c, val in [(ur, uc, u_val), (vr, vc, v_val)]:
                row_check[r][val] = col_check[c][val] = box_check[get_box(r, c)][val] = True
                
        # 2. 숫자 1~9의 위치 정보 입력
        num_positions = sys.stdin.readline().split()
        for i in range(9):
            r, c = pos_to_idx(num_positions[i])
            val = i + 1
            board[r][c] = val
            row_check[r][val] = col_check[c][val] = box_check[get_box(r, c)][val] = True
            
        # 3. 백트래킹 시작
        backtrack(0, board, row_check, col_check, box_check, used_domino)
        
        # 출력 양식
        print(f"Puzzle {tc}")
        for row in board:
            print("".join(map(str, row)))
        tc += 1

if __name__ == "__main__":
    solve()