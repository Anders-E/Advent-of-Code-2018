from sys import stdin

def two_three(s):
    counts = {}
    for c in s:
        counts[c] = 1 if c not in counts else counts[c] + 1
    return (2 in counts.values(), 3 in counts.values())

two_count = 0
three_count = 0

for two, three in map(two_three, stdin.readlines()):
    two_count, three_count = (two_count + two, three_count + three)

print(two_count * three_count)

