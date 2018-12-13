from sys import stdin
from copy import deepcopy

class Track:
    def __init__(self, track_map):
        self.map = []
        for line in track_map:
            self.map.append(list(line.rstrip()))

        self.carts = []
        for y, line in enumerate(self.map):
            for x, tile in enumerate(line):
                if tile == '<' or tile == '>':
                    self.set_tile(x, y, '-')
                    self.carts.append(self.Cart(x, y, tile))
                if tile == '^' or tile == 'v':
                    self.set_tile(x, y, '|')
                    self.carts.append(self.Cart(x, y, tile))

    def tick(self):
        cart_positions = set()
        for cart in self.carts:
            cart_positions.add((cart.x, cart.y))
        for cart in sorted(self.carts):
            cart_position = (cart.x, cart.y)
            cart.move(track)
            if (cart.x, cart.y) in cart_positions:
                return (cart.x, cart.y)
            cart_positions.add((cart.x, cart.y))

    def set_tile(self, x, y, tile):
        self.map[y][x] = tile

    def get_tile(self, x, y):
        return self.map[y][x]

    def print_map(self):
        tmp_map = deepcopy(self.map)
        for cart in self.carts:
            tmp_map[cart.y][cart.x] = cart.direction
        for line in tmp_map:
            print(''.join(line))

    class Cart:
        turn_right     = {'^' : '>', '>' : 'v', 'v' : '<', '<' : '^'}
        turn_left      = {'^' : '<', '<' : 'v', 'v' : '>', '>' : '^'}
        slash_turn     = {'^' : '>', '>' : '^', 'v' : '<', '<' : 'v'} # /
        backslash_turn = {'^' : '<', '>' : 'v', 'v' : '>', '<' : '^'} # \

        def __init__(self, x, y, direction):
            self.x = x
            self.y = y
            self.direction = direction
            self.intersection = 0

        def __lt__(self, other):
            if self.y == other.y:
                return self.x <= other.x
            return self.y < other.y
        
        def move(self, track):
            tile = track.get_tile(self.x, self.y)
            if tile == '+' or tile == '/' or tile == '\\':
                self.turn(tile)
            
            if self.direction == '>':
                self.x += 1
            if self.direction == '<':
                self.x -= 1
            if self.direction == '^':
                self.y -= 1
            if self.direction == 'v':
                self.y += 1

        def turn(self, tile):
            if tile == '/':
                self.direction = self.slash_turn[self.direction]
            if tile == '\\':
                self.direction = self.backslash_turn[self.direction]
            if tile == '+':
                if self.intersection == 0:
                    self.direction = self.turn_left[self.direction]
                if self.intersection == 2:
                    self.direction = self.turn_right[self.direction]
                self.intersection = (self.intersection + 1) % 3

track = Track(stdin.readlines())
while True:
    collision = track.tick()
    if collision:
        print(collision)
        break

