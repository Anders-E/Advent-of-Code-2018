from collections import defaultdict

GRID_SERIAL_NUMBER = 9110
memo = defaultdict(int)
fuel_cell_memo = defaultdict(int)

def fuel_cell_level(x, y):
    rack_id = x + 10
    level = ((rack_id * y + GRID_SERIAL_NUMBER) * rack_id // 100) % 10 - 5
    return level

def square_level(grid, x, y, size):
    level = memo[(x, y, size - 1)]
    level += sum(grid[x + size -1][y:y+size])
    level += sum([grid[xp][y + size - 1] for xp in range(x, x + size - 1)])
    memo[(x, y, size)] = level
    return level

def find_largest_power_coords(grid):
    max_level = -1e100
    max_x = -1
    max_y = -1
    max_size = -1
    for size in range(1, 301):
        for x in range(301 - size):
            for y in range(301 - size):
                level = square_level(grid, x, y, size)
                if max_level < level:
                    max_level = level
                    max_x = x
                    max_y = y
                    max_size = size
    return max_x, max_y, max_size

grid = [[fuel_cell_level(x, y) for y in range(300)] for x in range(300)]
print(find_largest_power_coords(grid))
