def solution(video_len, pos, op_start, op_end, commands):
    video_m, video_s = map(int, video_len.split(":"))
    video_len = video_m * 60 + video_s

    op_start_m, op_start_s = map(int, op_start.split(":"))
    op_start = op_start_m * 60 + op_start_s

    op_end_m, op_end_s = map(int, op_end.split(":"))
    op_end = op_end_m * 60 + op_end_s


    pos_m, pos_s = map(int, pos.split(":"))
    pos = pos_m * 60 + pos_s

    for command in commands:
        if pos >= op_start  and pos < op_end:
            pos = op_end
        if command == "next":
            if pos + 10 > video_len:
                pos = video_len
            else:
                pos += 10
        if command == "prev":
            if pos - 10 < 0:
                pos = 0
            else:
                pos -= 10

    if pos > op_start  and pos < op_end:
        pos = op_end
    
    ans_m = pos // 60
    ans_s = pos % 60
    
    if ans_m < 10:
        ans_m = f"0{ans_m}"
    if ans_s < 10:
        ans_s = f"0{ans_s}"

    return f"{ans_m}:{ans_s}"
