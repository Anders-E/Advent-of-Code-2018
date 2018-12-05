from sys import stdin
import re

def mark_fabric(x_margin, y_margin, w, h):
    for x in range(x_margin, x_margin + w):
        for y in range(y_margin, y_margin + h):
            fabric[x][y] += 1

def overlaps():
    count = 0
    for x in fabric:
        for y in x:
            if y > 1:
                count += 1
    return count

regex = re.compile(r"#(\d*) @ (\d*),(\d*): (\d*)x(\d*)")
fabric = [[0] * 1000] * 1000

for line in stdin.readlines():
    id, x_margin, y_margin, w, h = map(int, re.match(regex, line).groups())
    mark_fabric(x_margin, y_margin, w, h)

print(overlaps())

