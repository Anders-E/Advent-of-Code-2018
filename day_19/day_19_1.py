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

reg = [0] * 6
opcodes = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
opcodes = {op.__name__: op for op in opcodes}
ip = int(stdin.readline().split(' ')[1])
instructions = stdin.readlines()

while reg[ip] < len(instructions):
    line = instructions[reg[ip]]
    line = line.split(' ')
    op = line[0]
    a, b, c = map(int, line[1:])
    i = Instruction(op, a, b, c)
    opcodes[op](i)
    reg[ip] += 1

print(reg)

