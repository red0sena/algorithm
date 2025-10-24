# --- Helper Functions ---

def to_base10(s_num, base):
    """문자열 숫자를 10진수 정수로 변환합니다."""
    # 숫자에 base 이상의 문자가 포함되어 있는지 확인
    for digit in s_num:
        if int(digit) >= base:
            return None  # 이 진법에서는 유효하지 않은 숫자
    try:
        return int(s_num, base)
    except ValueError:
        return None

def from_base10(num, base):
    """10진수 정수를 base 진법 문자열로 변환합니다."""
    if num == 0:
        return "0"
    
    digits = []
    while num > 0:
        digits.append(str(num % base))
        num //= base
    return "".join(reversed(digits))

# --- Main Solution ---

def solution(expressions):
    known_equations = []
    unknown_equations = []
    all_numbers_str = set()

    # 1. 수식 파싱 및 모든 숫자 수집
    for expr in expressions:
        A, op, B, eq, C = expr.split()
        
        all_numbers_str.add(A)
        all_numbers_str.add(B)
        
        if C == 'X':
            unknown_equations.append((A, op, B))
        else:
            known_equations.append((A, op, B, C))
            all_numbers_str.add(C)

    # 2. 최종 후보 진법 찾기
    final_bases = set()
    for base in range(2, 10):
        is_valid_base = True
        
        # 2-1. 단서 1: 모든 숫자가 진법에 유효한지 확인
        for s_num in all_numbers_str:
            for digit in s_num:
                if int(digit) >= base:
                    is_valid_base = False
                    break
            if not is_valid_base:
                break
        
        if not is_valid_base:
            continue
            
        # 2-2. 단서 2: 알려진 수식이 모두 성립하는지 확인
        for A_str, op, B_str, C_str in known_equations:
            # 여기서는 to_base10이 아닌 int(s, base)를 바로 사용해도 됨
            # (이미 2-1에서 숫자 유효성을 검사했으므로)
            a_val = int(A_str, base)
            b_val = int(B_str, base)
            c_val = int(C_str, base)
            
            result_10 = a_val + b_val if op == '+' else a_val - b_val
            
            if result_10 != c_val:
                is_valid_base = False
                break
        
        if is_valid_base:
            final_bases.add(base)

    # 3. 'X' 수식 풀이
    answer = []
    for A_str, op, B_str in unknown_equations:
        possible_results = set()
        
        for base in final_bases:
            # 2-1에서 이미 유효성을 검사했으므로 int() 바로 사용
            a_val = int(A_str, base)
            b_val = int(B_str, base)
            
            result_10 = a_val + b_val if op == '+' else a_val - b_val
            
            result_str = from_base10(result_10, base)
            possible_results.add(result_str)
            
        # 결과 포맷팅
        full_expr_prefix = f"{A_str} {op} {B_str} = "
        if len(possible_results) == 1:
            answer.append(full_expr_prefix + possible_results.pop())
        else:
            # 0개인 경우 (모순, 문제 조건상 없음) 또는 2개 이상인 경우
            answer.append(full_expr_prefix + "?")
            
    return answer