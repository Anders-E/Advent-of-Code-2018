from sys import stdin
from collections import namedtuple
import re

reg_pattern = re.compile(r".*\[(.*)\].*")
Instruction = namedtuple("Instruction", ['op', 'a', 'b', 'c'])

def read_register():
    line = stdin.readline()
    return list(map(int, reg_pattern.match(line).group(1).split(',')))

def read_instruction():
    line = stdin.readline().rstrip()
    return Instruction(*map(int, line.split(' ')))

def addr(reg, i):
    reg[i.c] = reg[i.a] + reg[i.b]
    return reg

def addi(reg, i):
    reg[i.c] = reg[i.a] + i.b
    return reg

def mulr(reg, i):
    reg[i.c] = reg[i.a] * reg[i.b]
    return reg

def muli(reg, i):
    reg[i.c] = reg[i.a] * i.b
    return reg

def banr(reg, i):
    reg[i.c] = reg[i.a] & reg[i.b]
    return reg

def bani(reg, i):
    reg[i.c] = reg[i.a] & i.b
    return reg

def borr(reg, i):
    reg[i.c] = reg[i.a] | reg[i.b]
    return reg

def bori(reg, i):
    reg[i.c] = reg[i.a] | i.b
    return reg

def setr(reg, i):
    reg[i.c] = reg[i.a]
    return reg

def seti(reg, i):
    reg[i.c] = i.a
    return reg

def gtir(reg, i):
    reg[i.c] = int(i.a > reg[i.b])
    return reg

def gtri(reg, i):
    reg[i.c] = int(reg[i.a] > i.b)
    return reg

def gtrr(reg, i):
    reg[i.c] = int(reg[i.a] > reg[i.b])
    return reg

def eqir(reg, i):
    reg[i.c] = int(i.a == reg[i.b])
    return reg

def eqri(reg, i):
    reg[i.c] = int(reg[i.a] == i.b)
    return reg

def eqrr(reg, i):
    reg[i.c] = int(reg[i.a] == reg[i.b])
    return reg

opcodes = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

res = 0
while True:
    try:
        before = read_register()
        instr = read_instruction()
        after = read_register()
    except AttributeError:
        break

    correct_opcodes = 0
    for opcode in opcodes:
        #print("{}({}) = {}".format(opcode.__name__, before, opcode(before, instr)))
        if opcode(before.copy(), instr) == after:
            correct_opcodes += 1

    if correct_opcodes >= 3:
        res += 1

    stdin.readline()

print(res)

