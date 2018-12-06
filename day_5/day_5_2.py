from sys import stdin

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def react(polymer, c):
    stack = []
    for unit in polymer:
        if stack and unit == stack[-1].swapcase():
            stack.pop()
        elif unit.lower() != c:
            stack.append(unit)
    return stack

polymer = list(stdin.readline()[:-1])
shortest = len(polymer)

for c in ALPHABET:
    shortest = min(len(react(polymer, c)), shortest)

print(shortest)
