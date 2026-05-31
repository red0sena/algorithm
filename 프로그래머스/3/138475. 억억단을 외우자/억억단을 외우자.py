import numpy as np, math
from bisect import bisect_left

def solution(e, starts):
    # cnt[n] = 억억단에서 n의 등장 횟수 = n의 약수 개수
    cnt = np.zeros(e + 1, dtype=np.int32)
    for i in range(1, math.isqrt(e) + 1):   # √e번만 순회
        cnt[i*i::i] += 2      # 약수쌍 (i, n//i) 두 개를 카운트
        cnt[i*i]    -= 1      # 완전제곱수(i*i)는 약수가 하나뿐이므로 보정

    # [s, e] 구간 최빈값(동률이면 최소수) 후보 = 오른쪽 전부보다 크거나 같은 위치
    arr = cnt[1:e + 1]                              # arr[k] = cnt[k+1]
    inc = np.maximum.accumulate(arr[::-1])[::-1]    # 자기 포함 suffix max
    exc = np.empty(e, dtype=np.int32)              # 자기 제외 suffix max
    exc[:-1] = inc[1:]; exc[-1] = 0
    records = (np.nonzero(arr >= exc)[0] + 1).tolist()  # 오름차순 후보 목록

    # 각 s에 대해 s 이상인 가장 작은 record가 정답
    return [records[bisect_left(records, s)] for s in starts]