from sys import stdin

def read_cords():
    coords = []
    max_x = 0
    max_y = 0
    for id, line in enumerate(stdin.readlines(), 1):
        x, y = map(int, line.split(','))
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        coords.append((id, x, y))
    return coords, max_x + 1, max_y + 1

def create_map(coords, max_x, max_y):
    M = [['.'] * (max_y) for x in range(max_x)]
    for coord in coords:
        M[coord[1]][coord[2]] = coord[0]
    return M

def is_safe(coords, x, y):
    return sum([abs(x - coord[1]) + abs(y - coord[2]) for coord in coords]) < 10000

def largest_area(M):
    return sum(map(sum, M))

coords, max_x, max_y = read_cords()
M = create_map(coords, max_x, max_y)
for x in range(max_x):
    for y in range(max_y):
        M[x][y] = is_safe(coords, x, y)

print(largest_area(M))

