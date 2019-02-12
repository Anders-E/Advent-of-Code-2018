from sys import stdin
from collections import defaultdict
import re

class Marble:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

regex = re.compile(r"(\d*) players; last marble is worth (\d*)")
players, last_marble = map(int, regex.match(stdin.readline()).groups())

scores = defaultdict(int)
player = 1
current = Marble(0)
current.prev = current
current.next = current

for i in range(1, last_marble + 1):
    if not i % 23:
        current = current.prev.prev.prev.prev.prev.prev.prev
        scores[player] += i + current.value
        current.prev.next = current.next
        current.next.prev = current.prev
        current = current.next
    else:
        current = current.next.next
        new_node = Marble(i, current.prev, current)
        current.prev.next = new_node
        current.prev = new_node
        current = new_node

    player = ((player + 1) % (players + 1)) or 1

print(max(scores.values()))
