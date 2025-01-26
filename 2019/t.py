#!/usr/bin/env python3

import sys
import time
from collections import defaultdict


class Computer:
    def __init__(self, program):
        self.program = defaultdict(int)
        for i, v in enumerate(list(map(int, program.split(",")))):
            self.program[i] = v
        self.done = False
        self.eip = 0
        self.rel_base = 0

    def get_param(self, mode, reg):
        value = self.program[self.eip + reg]
        if mode == "0":
            return self.program[value]
        elif mode == "1":
            return value
        elif mode == "2":
            return self.program[self.rel_base + value]
        else:
            print("Error: Invalid Parameter Mode")
            sys.exit()

    def get_address(self, mode, reg):
        value = self.program[self.eip + reg]
        if mode == "0":
            return value
        elif mode == "2":
            return self.rel_base + value
        else:
            print("Error: Invalid Address Mode")
            sys.exit()

    def compute(self, signal):
        while True:
            inst = self.program[self.eip]
            op = inst % 100
            mode3, mode2, mode1 = f"{inst // 100:03d}"
            if op == 1:
                self.program[self.get_address(mode3, 3)] = self.get_param(
                    mode1, 1
                ) + self.get_param(mode2, 2)
                self.eip += 4
            elif op == 2:
                self.program[self.get_address(mode3, 3)] = self.get_param(
                    mode1, 1
                ) * self.get_param(mode2, 2)
                self.eip += 4
            elif op == 3:
                self.program[self.get_address(mode1, 1)] = signal
                self.eip += 2
            elif op == 4:
                self.eip += 2
                return self.get_param(mode1, 1 - 2)
            elif op == 5:
                if self.get_param(mode1, 1) != 0:
                    self.eip = self.get_param(mode2, 2)
                else:
                    self.eip += 3
            elif op == 6:
                if self.get_param(mode1, 1) == 0:
                    self.eip = self.get_param(mode2, 2)
                else:
                    self.eip += 3
            elif op == 7:
                self.program[self.get_address(mode3, 3)] = int(
                    self.get_param(mode1, 1) < self.get_param(mode2, 2)
                )
                self.eip += 4
            elif op == 8:
                self.program[self.get_address(mode3, 3)] = int(
                    self.get_param(mode1, 1) == self.get_param(mode2, 2)
                )
                self.eip += 4
            elif op == 9:
                self.rel_base += self.get_param(mode1, 1)
                self.eip += 2
            elif op == 99:
                self.done = True
                return 0
            else:
                print("Error")
                sys.exit()


def print_screen(screen, score):
    print("\33[2J")
    icons = {0: " ", 1: chr(9608), 2: ".", 3: "_", 4: "o"}
    for y in range(31):
        output = "  "
        for x in range(47):
            output += icons[screen[(x, y)]]
        print(output)
    print(f'  {"-"*16}{score:05d}{"-"*16}')


with open(sys.argv[1], "r") as f:
    program_str = f.read().strip()


comp = Computer(program_str)
count = 0
while not comp.done:
    _, _, block = comp.compute(None), comp.compute(None), comp.compute(None)
    if block == 2:
        count += 1


watch = int(len(sys.argv) > 2 and sys.argv[2] == "watch")
program_str = "2" + program_str[1:]
comp = Computer(program_str)
screen = defaultdict(int)
joystick = 0
score = 0

while not comp.done:
    need_to_print = False
    x = comp.compute(joystick)
    y = comp.compute(joystick)
    b = comp.compute(joystick)

    if (x, y) == (-1, 0):
        score = b
        need_to_print = True
    else:
        screen[(x, y)] = b

    if b == 4:
        need_to_print = True

    ball = [p for p in screen if screen[p] == 4]
    paddle = [p for p in screen if screen[p] == 3]

    if ball and paddle:
        if ball[0][0] < paddle[0][0]:
            joystick = -1
        elif ball[0][0] > paddle[0][0]:
            joystick = 1
        else:
            joystick = 0

    if watch and need_to_print:
        print_screen(screen, score)
        time.sleep(0.05)

print(f"Part 1: {count}")
print(f"Part 2: {score}")
