from sys import stdin

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def react(polymer):
    for i in range(0, len(polymer) - 1):
        a = polymer[i]
        b = polymer[i + 1]
        if (a.islower() and b == a.upper() or a.isupper() and b == a.lower()):
            polymer.pop(i)
            polymer.pop(i)
            return True
    return False

polymer = list(stdin.readline()[:-1])
shortest = len(polymer)

for c in ALPHABET:
    filtered_polymer = [unit for unit in polymer if unit.lower() != c]
    while (react(filtered_polymer)):
        pass
    if len(filtered_polymer) < shortest:
        shortest = len(filtered_polymer)

print(shortest)
