from sys import stdin
from collections import defaultdict
import re

class Light:
    def __init__(self, x, y, v_x, v_y):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y

    def step(self):
        self.x += self.v_x
        self.y += self.v_y

def draw_lights(lights, light_map):
    xs = [light.x for light in lights]
    ys = [light.y for light in lights]
    
    max_x = max(xs)
    min_x = min(xs)
    max_y = max(ys)
    min_y = min(ys)
    
    for y in range(min_y - 2, max_y + 2):
        for x in range(min_x - 2, max_x + 2):
            print('#' if light_map[(x, y)] else '.', end='')
        print()
    print()

def step(lights):
    light_map = defaultdict(bool)
    for light in lights:
        light.step()
        light_map[(light.x, light.y)] = True
    return light_map

def kekas(lights):
    ys = [light.y for light in lights]
    max_y = max(ys)
    min_y = min(ys)
    return max_y - min_y < 10

regex = re.compile(r"position=<(.*?),(.*?)> velocity=<(.*?),(.*?)>")
lights = []
velocities = []

for line in stdin.readlines():
    x, y, v_x, v_y = map(int, regex.match(line).groups())
    lights.append(Light(x, y, v_x, v_y))

while not kekas(lights):
    light_map = step(lights)

draw_lights(lights, light_map)
