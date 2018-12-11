from sys import stdin
from collections import defaultdict
import re

regex = re.compile(r"(\d*) players; last marble is worth (\d*)")
players, last_marble = map(int, regex.match(stdin.readline()).groups())

scores = defaultdict(int)
current = 0
player = 1
circle = [0]
for i in range(1, last_marble + 1):
    if not i % 23:
        current = (current - 7) % len(circle)
        scores[player] += i + circle.pop(current)
    else:
        current = ((current + 2) % (len(circle) or current + 3)) or len(circle)
        circle.insert(current, i)
    player = ((player + 1) % (players + 1)) or 1

print(max(scores.values()))
