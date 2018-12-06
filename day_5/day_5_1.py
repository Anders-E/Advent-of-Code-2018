from sys import stdin

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

while (react(polymer)):
    pass

print(len(polymer))
