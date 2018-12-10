from sys import stdin
import re

def read_input():
    regex = re.compile(r"Step (.) must be finished before step (.) can begin\.")
    deps = {}
    for line in stdin.readlines():
        dep, step = regex.match(line).groups()
        if step not in deps:
            deps[step] = set()
        if dep not in deps:
            deps[dep] = set()
        deps[step].add(dep)
    return deps

def find_path(deps):
    visited = set()
    path = []
    while len(visited) != len(deps):
        for step in sorted(deps.keys()):
            deps[step] -= visited
            if not deps[step] and step not in visited:
                visited.add(step)
                path.append(step)
                break
    return path

deps = read_input()
path = find_path(deps)
print("".join(path))

