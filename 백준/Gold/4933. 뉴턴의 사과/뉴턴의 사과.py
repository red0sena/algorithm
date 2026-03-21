import sys

def solve():
    it = iter(sys.stdin.read().split())
    
    try:
        T = int(next(it))
    except StopIteration:
        return

    def get_canonical_tree():
        st = []
        for x in it:
            if x == 'end':
                return st[0] if st else None
            if x == 'nil':
                # 🔥 에러 해결의 핵심: 문자열 대신 튜플로 넣어서 타입을 통일합니다.
                st.append(('nil',)) 
            else:
                # 이제 스택에서 꺼낸 두 요소는 무조건 튜플이므로 sorted()가 완벽히 작동합니다.
                st.append((x, *sorted([st.pop(), st.pop()])))

    for _ in range(T):
        print("true" if get_canonical_tree() == get_canonical_tree() else "false")

if __name__ == '__main__':
    solve()