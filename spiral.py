# Завдання 4
def spiral(matrix):
    result = []
    if len(matrix) == 0:
        return result
    m = len(matrix)
    n = len(matrix[0])
    passed = [[0 for i in range(n)] for j in range(m)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    x = 0
    y = 0
    di = 0
    for i in range(m * n):
        result.append(matrix[x][y])
        passed[x][y] = True
        cr = x + dr[di]
        cc = y + dc[di]
        if 0 <= cr < m and 0 <= cc < n and not (passed[cr][cc]):
            x = cr
            y = cc
        else:
            di = (di + 1) % 4
            x += dr[di]
            y += dc[di]
    return result


print(spiral([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(spiral([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
