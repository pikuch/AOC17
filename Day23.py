# AOC17 day 23
from Coprocessor import Coprocessor
from math import sqrt, ceil


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def is_composite(n):
    for divider in range(2, int(sqrt(n)) + 2):
        if n % divider == 0:
            return True
    return False


def run():
    data = load_data("Day23.txt")
    cop = Coprocessor()
    cop.load(data.split("\n"))
    cop.run()
    print(f"The mul instruction was invoked {cop.mul_invocations} times")

    # cop = Coprocessor()
    # cop.load(data.split("\n"))
    # cop.reg['a'] = 1
    # cop.run()
    # print(f"The final value in register h is {cop.reg['h']}")

    # the program returns the number of composite numbers within the set [105700 + i * 17], i = [0, 1000]
    non_primes = 0
    for i in range(1001):
        if is_composite(105700 + i * 17):
            non_primes += 1
    print(f"The output of the program will be {non_primes}")
