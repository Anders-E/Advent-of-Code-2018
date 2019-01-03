from sys import stdin
import re

def read_input():
    x_pattern = re.compile(r"x=(.*?)[,\n]")
    y_pattern = re.compile(r"y=(.*?)[,\n]")

    global clay
    global max_x
    global min_x
    global max_y
    global min_y

    for line in stdin.readlines():
        x = tuple(map(int, x_pattern.search(line).group(1).split("..")))
        y = tuple(map(int, y_pattern.search(line).group(1).split("..")))

        if len(x) > 1:
            x = range(x[0], x[1] + 1)
        if len(y) > 1:
            y = range(y[0], y[1] + 1)

        for a in x:
            max_x = max(max_x, a)
            min_x = min(min_x, a)
            for b in y:
                max_y = max(max_y, b)
                min_y = min(min_y, b)
                clay.add((a, b))

def water(x, y, sqm):
    while y < max_y:
        pass


### globals
clay = set()
max_x = 0
min_x = 1e100
max_y = 0
min_y = 1e100

read_input()
water(500, 0, 0)
