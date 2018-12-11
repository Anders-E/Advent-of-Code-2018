from sys import stdin, exit

def is_correct(a, b):
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
            diff_index = i
    if diff == 1:
        return a[:diff_index] + a[diff_index + 1:]

ids = list(map(str.rstrip, stdin.readlines()))
for i, a in enumerate(ids):
    for b in ids[i:]:
        if is_correct(a, b):
            print(is_correct(a, b))
            exit()

