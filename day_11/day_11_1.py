GRID_SERIAL_NUMBER = 9110

def fuel_cell_level(x, y):
    rack_id = x + 10
    return ((rack_id * y + GRID_SERIAL_NUMBER) * rack_id // 100) % 10 - 5

def square_level(grid, x, y):
    return sum(
        [sum(value) for value in [col[y:y+3] for col in grid[x:x+3]]]
    )

def find_largest_power_coords(grid):
    max_level = -45
    max_x = -1
    max_y = -1
    for x in range(298):
        for y in range(298):
            if max_level < square_level(grid, x, y):
                max_level = square_level(grid, x, y)
                max_x = x
                max_y = y
    return max_x, max_y

grid = [[fuel_cell_level(x, y) for y in range(300)] for x in range(300)]
print(find_largest_power_coords(grid))

