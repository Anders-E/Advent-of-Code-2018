from sys import stdin
from queue import Queue

class Coordinate:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

def closest_coord(M, x, y, max_x, max_y):
    pass

def read_cords():
    coords = []
    max_x = 0
    max_y = 0
    for id, line in enumerate(stdin.readlines(), 1):
        x, y = map(int, line.split(','))
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        coords.append(Coordinate(id, x, y))
    return coords, max_x + 1, max_y + 1

def create_map(coords, max_x, max_y):
    M1 = [['.'] * (max_x) for x in range(max_y)]
    for coord in coords:
        M1[coord.y][coord.x] = coord.id
    return M1

coords, max_x, max_y = read_cords()
M1 = create_map(coords, max_x, max_y)
M2 = M1.copy()
for x in range(max_x):
    for y in range(max_y):
        M2[y][x] = closest_coord(M1, x, y, max_x, max_y)

print(M2)


