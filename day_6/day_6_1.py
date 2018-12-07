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

def closest_coord(coords, x, y):
    min_dist = 1e100
    closest = 0
    for coord in coords:
        dist = abs(x - coord[1]) + abs(y - coord[2])
        if dist == min_dist:
            closest = 0
        if dist < min_dist:
            min_dist = dist
            closest = coord[0]
    return closest

def largest_area(M, max_x, max_y):
    areas = {}
    inf = set([0])
    for x in range(max_x):
        for y in range(max_y):
            id = M[x][y]
            if is_border(x, y, max_x, max_y):
                inf.add(id)
                areas[id] = -1
            if id not in areas:
                areas[id] = 0
            if id not in inf:
                areas[id] += 1
    return max(areas.values())

def is_border(x, y, max_x, max_y):
    return x == 0 or x == max_x - 1 or y == 0 or y == max_y - 1

coords, max_x, max_y = read_cords()
M = create_map(coords, max_x, max_y)
for x in range(max_x):
    for y in range(max_y):
        M[x][y] = closest_coord(coords, x, y)

print(largest_area(M, max_x, max_y))

