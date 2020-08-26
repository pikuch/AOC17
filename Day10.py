# AOC17 day 10
from functools import reduce
from KnotHash import KnotHash


def knot_hash(nums, spans):
    pos = 0
    skip_size = 0
    for span in spans:
        reversed_values = []
        for i in range(span):
            reversed_values.append(nums[(pos + i) % len(nums)])
        reversed_values.reverse()
        for i in range(span):
            nums[(pos + i) % len(nums)] = reversed_values[i]
        pos = (pos + span + skip_size) % len(nums)
        skip_size += 1


def sparse_hash(nums, spans):
    pos = 0
    skip_size = 0
    for span in spans * 64:
        reversed_values = []
        for i in range(span):
            reversed_values.append(nums[(pos + i) % len(nums)])
        reversed_values.reverse()
        for i in range(span):
            nums[(pos + i) % len(nums)] = reversed_values[i]
        pos = (pos + span + skip_size) % len(nums)
        skip_size += 1


def dense_hash(nums):
    xord = []
    for i in range(16):
        xord.append(reduce(lambda x, y: x ^ y, nums[i * 16:i * 16 + 16], 0))
    dense = ""
    for n in xord:
        h = hex(n)[2:]
        if len(h) == 1:
            h = "0" + h
        dense += h
    return dense


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def run():
    data = load_data("Day10.txt")
    spans = list(map(int, data.split(",")))
    nums = list(range(256))
    knot_hash(nums, spans)
    print(f"The result of multiplying the first two numbers is {nums[0] * nums[1]}")
    spans2 = list(map(ord, data)) + [17, 31, 73, 47, 23]
    kh = KnotHash(spans2)
    print(f"The dense hash is {kh.hex()}")
