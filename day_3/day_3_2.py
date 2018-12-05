from sys import stdin
import re

def mark_fabric(id, x_margin, y_margin, w, h):
    for x in range(x_margin, x_margin + w):
        for y in range(y_margin, y_margin + h):
            fabric[x][y].add(id)

def find_non_overlapping():
    overlapping = set()
    for x in range(1000):
        for y in range(1000):
            if len(fabric[x][y]) > 1:
                overlapping |= fabric[x][y]
    for id in range(1, 1350):
        if id not in overlapping:
            return id

regex = re.compile(r"#(\d*) @ (\d*),(\d*): (\d*)x(\d*)")
fabric = [[set() for y in range(1000)] for x in range(1000)]

for line in stdin.readlines():
    id, x_margin, y_margin, w, h = map(int, regex.match(line).groups())
    mark_fabric(id, x_margin, y_margin, w, h)

print(find_non_overlapping())
