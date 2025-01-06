def solution(points, routes):
    def shortest_path_coordinates(x, y, x1, y1):
        path_coordinates = []

        # Current position
        current_x, current_y = x, y

        while current_x != x1 or current_y != y1:
            if current_x != x1:
                if current_x < x1:
                    current_x += 1
                else:
                    current_x -= 1
            elif current_y != y1:
                if current_y < y1:
                    current_y += 1
                else:
                    current_y -= 1
            path_coordinates.append((current_x, current_y))
        return path_coordinates

    # Example usage

    all_paths = []
    for route in routes:
        this_paths = [(points[route[0]-1])]
        for i in range(1, len(route)):
            start_point = points[route[i-1]-1]
            end_point = points[route[i]-1]
            path = shortest_path_coordinates(*start_point, *end_point)
            this_paths.extend(path)
        all_paths.append(this_paths)


    j = 0
    res = 0
    while True:
        compare_xy = []
        count = 0
        already_comare = []
        for i in range(len(all_paths)):
            try:
                compare_xy.append(all_paths[i][j])
            except:
                count += 1
                continue
        if count >= len(all_paths):
            break
        compare_xy.sort()
        for i in range(1, len(compare_xy)):
            if compare_xy[i-1] == compare_xy[i] and not(compare_xy[i] in already_comare):
                res += 1
                already_comare.append(compare_xy[i])
        j += 1
    return res

