from sys import stdin
from collections import namedtuple
import re

reg_pattern = re.compile(r".*\[(.*)\].*")
Instruction = namedtuple("Instruction", ['op', 'a', 'b', 'c'])

def addr(i):
    reg[i.c] = reg[i.a] + reg[i.b]
    return reg

def addi(i):
    reg[i.c] = reg[i.a] + i.b
    return reg

def mulr(i):
    reg[i.c] = reg[i.a] * reg[i.b]
    return reg

def muli(i):
    reg[i.c] = reg[i.a] * i.b
    return reg

def banr(i):
    reg[i.c] = reg[i.a] & reg[i.b]
    return reg

def bani(i):
    reg[i.c] = reg[i.a] & i.b
    return reg

def borr(i):
    reg[i.c] = reg[i.a] | reg[i.b]
    return reg

def bori(i):
    reg[i.c] = reg[i.a] | i.b
    return reg

def setr(i):
    reg[i.c] = reg[i.a]
    return reg

def seti(i):
    reg[i.c] = i.a
    return reg

def gtir(i):
    reg[i.c] = int(i.a > reg[i.b])
    return reg

def gtri(i):
    reg[i.c] = int(reg[i.a] > i.b)
    return reg

def gtrr(i):
    reg[i.c] = int(reg[i.a] > reg[i.b])
    return reg

def eqir(i):
    reg[i.c] = int(i.a == reg[i.b])
    return reg

def eqri(i):
    reg[i.c] = int(reg[i.a] == i.b)
    return reg

def eqrr(i):
    reg[i.c] = int(reg[i.a] == reg[i.b])
    return reg

opcodes = {
    0: mulr,
    1: addr,
    2: banr,
    3: eqir,
    4: muli,
    5: setr,
    6: eqri,
    7: gtri,
    8: eqrr,
    9: addi,
    10: gtir,
    11: gtrr,
    12: borr,
    13: bani,
    14: seti,
    15: bori
}

reg = [0, 0, 0, 0]
for line in stdin.readlines():
    i = Instruction(*map(int, line.split(' ')))
    opcodes[i.op](i)
print(reg)

