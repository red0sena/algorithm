import sys

def solve():
    while True:
        try:
            line = list(map(int, sys.stdin.readline().split()))
            
            # 입력의 마지막 0 처리
            if line[0] == 0:
                break
            
            n = line[0]
            heights = line[1:]
            
            # 마지막에 0을 추가하여 스택에 남은 모든 막대를 처리하도록 유도
            heights.append(0)
            
            stack = [] # 인덱스를 저장하는 스택
            max_area = 0
            
            for i, h in enumerate(heights):
                # 스택이 비어있지 않고, 현재 높이가 스택 top의 높이보다 작다면
                # => 직사각형을 확정지을 때가 옴 (오른쪽 끝을 만남)
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    
                    # 너비 계산 (width)
                    if not stack:
                        width = i
                    else:
                        width = i - stack[-1] - 1
                        
                    max_area = max(max_area, height * width)
                
                stack.append(i)
            
            print(max_area)
            
        except ValueError:
            break

if __name__ == "__main__":
    solve()