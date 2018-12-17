from sys import stdin
from copy import deepcopy

class Track:
    def __init__(self, track_map):
        self.map = []
        for line in track_map:
            self.map.append(list(line.rstrip()))

        self.carts = []
        self.cart_positions = set()
        for y, line in enumerate(self.map):
            for x, tile in enumerate(line):
                if tile == '<' or tile == '>':
                    self.set_tile(x, y, '-')
                    self.carts.append(self.Cart(x, y, tile))
                    self.cart_positions.add((x, y))
                if tile == '^' or tile == 'v':
                    self.set_tile(x, y, '|')
                    self.carts.append(self.Cart(x, y, tile))
                    self.cart_positions.add((x, y))

    def tick(self):
        self.cart_positions = set()
        for cart in self.carts:
            self.cart_positions.add((cart.x, cart.y))
        for cart in sorted(self.carts):
            prev_pos = (cart.x, cart.y)
            cart.move(track)
            if (cart.x, cart.y) in self.cart_positions:
                self.remove_carts(cart.x, cart.y)
            else:
                self.cart_positions.add((cart.x, cart.y))
            if prev_pos in self.cart_positions:
                self.cart_positions.remove(prev_pos)

    def remove_carts(self, x, y):
        tmp = len(self.carts)
        self.carts = [cart for cart in self.carts if (cart.x, cart.y) != (x, y)]
        self.cart_positions.remove((x, y))

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
while len(track.carts) > 1:
    track.tick()
last_cart = track.carts[0]
print((last_cart.x, last_cart.y))

