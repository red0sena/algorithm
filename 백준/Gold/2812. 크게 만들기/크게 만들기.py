import sys

# 입력을 빠르게 받기 위한 설정
input = sys.stdin.readline

def solution():
    """
    N자리 숫자에서 K개의 수를 지워 가장 큰 수를 만드는 함수입니다.
    """
    n, k = map(int, input().split())
    number_str = input().strip()
    
    # 결과를 저장할 스택
    stack = []
    
    # 지워야 할 개수를 저장
    k_remains = k

    for digit in number_str:
        # 1. 스택이 비어있지 않고,
        # 2. 아직 지울 횟수가 남아있고,
        # 3. 스택의 최상단 값보다 현재 숫자가 더 크면
        #    -> 스택의 최상단 값을 제거 (pop)하고, 지울 횟수를 1 줄입니다.
        while stack and k_remains > 0 and stack[-1] < digit:
            stack.pop()
            k_remains -= 1
        
        # 현재 숫자를 스택에 추가합니다.
        stack.append(digit)

    # 최종적으로 만들어야 할 숫자의 길이
    final_length = n - k
    
    # 스택에 있는 숫자들을 필요한 길이만큼 잘라서 문자열로 합칩니다.
    # 만약 k_remains가 남아있다면(예: 98765, k=2), 스택의 뒷부분을 잘라냅니다.
    result = "".join(stack[:final_length])
    
    print(result)

solution()