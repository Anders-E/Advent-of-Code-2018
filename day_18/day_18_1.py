from sys import stdin

#   . open ground
#   | trees
#   # lumberyard

def read_input():
    m = {}
    for y, line in enumerate(stdin.readlines()):
        for x, char in enumerate(line.rstrip()):
            m[(x, y)] = char
    return m

def tick(m):
    new_m = {}
    for x in range(50):
        for y in range(50):
            counts = adjacents(m, x, y)
            if m[(x, y)] == '.' and counts['|'] >= 3:
                new_m[(x, y)] = '|'
            elif m[(x, y)] == '.':
                new_m[(x, y)] = '.'
            if m[(x, y)] == '|' and counts['#'] >= 3:
                new_m[(x, y)] = '#'
            elif m[(x, y)] == '|':
                new_m[(x, y)] = '|'
            if m[(x, y)] == '#' and counts['|'] > 0 and counts['#'] > 0:
                new_m[(x, y)] = '#'
            elif m[(x, y)] == '#':
                new_m[(x, y)] = '.'
    return new_m

def adjacents(m, x, y):
    counts = {'.': 0, '|': 0, '#': 0}
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (i, j) in m:
                counts[m[(i, j)]] += 1
    counts[m[(x, y)]] -= 1
    return counts

def print_m(m):
    for y in range(50):
        for x in range(50):
            print(m[(x, y)], end="")
        print()
    print()

m = read_input()
print_m(m)
for i in range(1, 11):
    m = tick(m)
    print("After {} minutes:".format(i))
    print_m(m)

counts = {'.': 0, '|': 0, '#': 0}
for value in m.values():
    counts[value] += 1
print("{} * {} = {}".format(counts['|'], counts['#'], counts['|'] * counts['#']))
