# AOC17 day 08
from collections import defaultdict


def decode(prog):
    regs = defaultdict(lambda: 0)  # for new registers
    for words in map(lambda x: x.split(), prog):




def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def run():
    data = load_data("Day08.txt")
    program = data.split("\n")
    registers = decode(program)
    print(f"The largest value in any register is {max(registers.values())}")
