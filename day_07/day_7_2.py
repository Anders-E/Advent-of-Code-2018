from sys import stdin
from string import ascii_uppercase
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

def get_min_time(worker_times):
    min_time = max(worker_times)
    for wt in worker_times:
        if wt != 0:
            min_time = min(min_time, wt)
    return min_time

def path_time(deps):
    step_times = {c: i for i, c in enumerate(ascii_uppercase, 61)}
    visited = set()
    worker_times = [0] * 5
    worker_tasks = [''] * 5
    total_time = 0

    while len(visited) != len(deps):
        min_time = get_min_time(worker_times)

        total_time += min_time
        worker_times = list(map(lambda x: x - min_time if x >= min_time else 0, worker_times))
        
        for i in range(len(worker_times)):
            if not worker_times[i]:
                visited.add(worker_tasks[i])
                worker_tasks[i] = ''

        for step in sorted(deps.keys()):
            deps[step] -= visited
            if not deps[step] and step not in visited and step not in worker_tasks and not all(worker_times):
                for i in range(len(worker_times)):
                    if not worker_times[i]:
                        worker_times[i] = step_times[step]
                        worker_tasks[i] = step
                        break

    return total_time + max(worker_times)

deps = read_input()
time = path_time(deps)
print(time)

