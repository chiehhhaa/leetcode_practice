def optimize_path(directions):
    path = []  # 用來存儲最佳化的路徑
    opposite = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}  # 定義相對的方向

    for direction in directions:
        # 如果路徑不是空的且當前方向與前一個方向相反，則移除前一個方向
        if path and direction == opposite[path[-1]]:
            path.pop()
        else:
            path.append(direction)

    return path
