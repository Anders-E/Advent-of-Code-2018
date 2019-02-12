from sys import stdin
import re

pots = list("..." + re.match(r"initial state: (.*)", stdin.readline()).group(1) + "...")
stdin.readline()

spread =  {}
spread.setdefault(())

for line in stdin.readlines():
    line = line.split(" => ")
    spread[tuple(line[0])] = line[1].rstrip()

print(''.join(pots))
starting_index = -3
for i in range(20):
    new_pots = pots.copy()
    for index, pot in enumerate(pots[2:-2], 2):
        nearby = tuple(pots[index-2:index+3])
        new_pots[index] = spread[nearby]
    if new_pots[0:3] != pots[0:3]:
        new_pots.insert(0, '.')
        new_pots.insert(0, '.')
        starting_index -= 2
    if new_pots[-3:] != pots[-3:]:
        new_pots.append('.')
        new_pots.append('.')
    pots = new_pots.copy()
    print(''.join(pots))

s = 0
for i, pot in enumerate(pots, starting_index):
    if pot == '#':
        s += i

print(s)
