from sys import stdin
from queue import Queue
from copy import deepcopy

class Map:
    def __init__(self, m):
        self.map = []
        self.units = {}
        for line in m:
            self.map.append(list(line.rstrip()))
        self.w = len(self.map[0])
        self.h = len(self.map)
        self.elves = 0
        self.goblins = 0
        self.rounds = 0
        for y, row in enumerate(self.map):
            for x, tile in enumerate(row):
                if tile == 'E':
                    self.units[(x, y)] = self.Unit(x, y, tile)
                    self.elves += 1
                if tile == 'G':
                    self.units[(x, y)] = self.Unit(x, y, tile)
                    self.goblins += 1

    def tick(self):
        for unit in sorted(self.units.values()):
            if self.elves == 0 or self.goblins == 0:
                return
            if unit.is_dead():
                continue
            self.set_tile(unit.coords(), '.')
            del self.units[unit.coords()]
            unit.move(self)
            self.set_tile(unit.coords(), unit.tile)
            self.units[unit.coords()] = unit
            unit.attack(self, self.units)
        print("Round: {}".format(self.rounds + 1))
        print(self)
        self.rounds += 1

    def set_tile(self, coords, tile):
        self.map[coords[1]][coords[0]] = tile

    def get_tile(self, coords):
        return self.map[coords[1]][coords[0]]

    def __str__(self):
        s = []
        tmp_map = deepcopy(self.map)
        for line in tmp_map:
            s += line + ['\n']
        return ''.join(s[:-1])

    class Unit:
        attack_power = 3

        def __init__(self, x, y, tile):
            self.x = x
            self.y = y
            self.tile = tile
            self.enemy = 'E' if tile == 'G' else 'G'
            self.hp = 200

        def coords(self):
            return (self.x, self.y)

        def find_path(self, m):
            visited = set()
            queue = Queue()
            queue.put([self.coords()])
            while not queue.empty():
                path = queue.get()
                current = path[-1]
                if current not in visited:
                    visited.add(current)
                    for adjacent in get_adjacents(current):
                        tile = m.get_tile(adjacent)
                        if tile == self.enemy:
                            return path
                        if tile == '.':
                            new_path = path.copy()
                            new_path.append(adjacent)
                            queue.put(new_path)

        def move(self, m):
            path = self.find_path(m)
            if path and len(path) > 1:
                self.x = path[1][0]
                self.y = path[1][1]

        def attack(self, m, units):
            min_hp = 201
            target = None
            for adjacent in reversed(get_adjacents((self.x, self.y))):
                if m.get_tile(adjacent) == self.enemy:
                    other = units.get(adjacent)
                    if not other.is_dead():
                        if other.hp <= min_hp:
                            min_hp = other.hp
                            target = other
            if target:
                target.hp -= self.attack_power
                if target.is_dead():
                    del units[target.coords()]
                    m.set_tile(target.coords(), '.')
                    if target.tile == 'G':
                        m.goblins -= 1
                    if target.tile == 'E':
                        m.elves -= 1

        def is_dead(self):
            return self.hp <= 0

        def __lt__(self, other):
            if self.y == other.y:
                return self.x < other.x
            return self.y < other.y

def get_adjacents(coords):
    x = coords[0]
    y = coords[1]
    return [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]

m = Map(stdin.readlines())
while m.goblins > 0 and m.elves > 0:
    m.tick()
s = 0
for unit in sorted(m.units.values()):
    s += unit.hp
print("{} * {} = {}".format(m.rounds, s, m.rounds * s))

