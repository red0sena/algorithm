def solution(n, bans):
    # 1. 문자열을 숫자로 변환하는 함수 (1-based 26진법)
    def to_num(s):
        num = 0
        for char in s:
            num = num * 26 + (ord(char) - ord('a') + 1)
        return num

    # 2. 숫자를 문자열로 변환하는 함수
    def to_string(num):
        result = []
        while num > 0:
            num -= 1  # 0-based로 보정 (나머지 연산을 위해)
            result.append(chr(ord('a') + (num % 26)))
            num //= 26
        return ''.join(result[::-1])

    # 3. bans를 숫자로 변환하고 정렬
    # (문자열 정렬이 아닌 숫자 크기 순 정렬이 필요함)
    ban_nums = [to_num(b) for b in bans]
    ban_nums.sort()

    # 4. n번째 유효한 주문 찾기 (Shifting 기법)
    ans = n
    for ban in ban_nums:
        # 현재 내가 보고 있는 타겟(ans)보다 같거나 작은 곳에 봉인된 주문이 있다면
        # 내 타겟은 그만큼 뒤로 밀려나야 함
        if ban <= ans:
            ans += 1
        else:
            # bans가 정렬되어 있으므로, 현재 ban이 ans보다 크다면
            # 그 뒤의 ban들도 모두 ans보다 크므로 더 볼 필요 없음
            break
            
    # 5. 최종 숫자를 다시 문자열로 변환
    return to_string(ans)