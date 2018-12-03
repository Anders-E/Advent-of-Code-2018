from sys import stdin

freq = 0

for num in map(int, stdin.readlines()):
    freq += num

print(freq)

