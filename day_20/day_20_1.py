from sys import stdin
from enum import Enum

class Token(Enum):
    W = 'W'
    N = 'N'
    E = 'E'
    S = 'S'
    L_PAREN = '('
    R_PAREN = ')'
    PIPE = '|'
    CARET = '^'
    DOLLAR = '$'

class Room():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def traverse(regex, room):
    global rooms
    token = Token(regex.pop())
    if token == Token.R_PAREN or token == Token.DOLLAR
        return

regex = list(reversed(stdin.readline()))
room = Room(0, 0)
rooms = {(0, 0): room}
traverse(regex, room)
