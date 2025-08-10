def solution(coin, cards):
    n = len(cards)
    target = n + 1

    hand = set(cards[: n // 3])   # 초기 손패
    open_set = set()              # 지금까지 공개(보관)된 카드
    i = n // 3
    rounds = 1

    def find_free_pair():
        # 손패 2장으로 n+1 만드는 한 쌍을 찾으면 (x, y) 반환
        for x in hand:
            y = target - x
            if y in hand and y != x:
                return x, y
        return None

    while i + 1 < n:
        # 이번 라운드 공개 2장
        a, b = cards[i], cards[i + 1]
        open_set.add(a); open_set.add(b)
        i += 2

        # 0코인: 손패 2장
        pair = find_free_pair()
        if pair:
            x, y = pair
            hand.remove(x); hand.remove(y)
            rounds += 1
            continue

        # 1코인: 손패 1 + 보관 1
        used = False
        if coin >= 1:
            for x in list(hand):
                y = target - x
                if y in open_set:
                    hand.remove(x)
                    open_set.remove(y)
                    coin -= 1
                    rounds += 1
                    used = True
                    break
        if used:
            continue

        # 2코인: 보관 2장
        if coin >= 2:
            # 손패의 보완카드(보관에서 가능하면 건드리지 않을 집합)
            avoid = {target - x for x in hand}

            chosen = None
            # (1) 둘 다 avoid가 아닌 쌍 우선
            for u in open_set:
                v = target - u
                if v in open_set and v != u and (u not in avoid and v not in avoid):
                    chosen = (u, v); break
            # (2) 없으면 둘 중 하나만 avoid인 쌍
            if not chosen:
                for u in open_set:
                    v = target - u
                    if v in open_set and v != u and not (u in avoid and v in avoid):
                        chosen = (u, v); break
            # (3) 그래도 없으면 아무 쌍이나
            if not chosen:
                for u in open_set:
                    v = target - u
                    if v in open_set and v != u:
                        chosen = (u, v); break

            if chosen:
                u, v = chosen
                open_set.remove(u); open_set.remove(v)
                coin -= 2
                rounds += 1
                continue

        # 불가능하면 종료
        break

    return rounds
