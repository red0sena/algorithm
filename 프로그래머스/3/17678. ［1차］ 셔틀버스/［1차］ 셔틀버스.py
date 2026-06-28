def solution(n, t, m, timetable):
    # 시간을 분 단위 정수로 변환
    def to_min(time_str):
        h, mi = map(int, time_str.split(':'))
        return h * 60 + mi

    def to_time(minutes):
        return f"{minutes // 60:02d}:{minutes % 60:02d}"

    # 크루 도착 시각 정렬
    crews = sorted(to_min(t_) for t_ in timetable)

    last_shuttle = 540 + t * (n - 1)  # 마지막 셔틀 시각 (분)
    crew_idx = 0  # 크루 포인터

    for i in range(n):
        shuttle_time = 540 + t * i  # 현재 셔틀 도착 시각
        count = 0  # 현재 셔틀에 탄 인원

        while crew_idx < len(crews) and crews[crew_idx] <= shuttle_time and count < m:
            count += 1
            crew_idx += 1

        # 마지막 셔틀일 때 콘의 최적 시각 계산
        if i == n - 1:
            if count < m:
                # 자리 있음 → 셔틀 시각에 도착해도 됨
                return to_time(shuttle_time)
            else:
                # 자리 없음 → 마지막 탑승자보다 1분 일찍
                return to_time(crews[crew_idx - 1] - 1)