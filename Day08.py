# AOC17 day 08
from collections import defaultdict
import operator


def check_condition(items, regs, ops):
    return ops[items[1]](regs[items[0]], int(items[2]))


def update_register(items, regs, ops):
    regs[items[0]] = ops[items[1]](regs[items[0]], int(items[2]))


def decode(prog):
    ops = {"<": operator.lt,
           "<=": operator.le,
           "==": operator.eq,
           "!=": operator.ne,
           ">=": operator.ge,
           ">": operator.gt,
           "inc": operator.iadd,
           "dec": operator.isub
           }
    max_reg = 0
    regs = defaultdict(lambda: 0)  # for new registers
    for words in map(lambda x: x.split(), prog):
        if check_condition(words[4:], regs, ops):
            update_register(words[0:3], regs, ops)
        if regs[words[0]] > max_reg:
            max_reg = regs[words[0]]
    return regs, max_reg


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def run():
    data = load_data("Day08.txt")
    program = data.split("\n")
    registers, max_reg = decode(program)
    print(f"The largest value in any register is {max(registers.values())}, and the largest at any time is {max_reg}")
