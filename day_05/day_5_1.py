from sys import stdin

def react(polymer):
    stack = []
    for unit in polymer:
        if stack and unit == stack[-1].swapcase():
            stack.pop()
        else:
            stack.append(unit)
    return stack

polymer = list(stdin.readline()[:-1])
print(len(react(polymer)))
