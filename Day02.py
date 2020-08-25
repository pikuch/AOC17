# AOC17 day 02
from itertools import combinations


def prepare(d):
    data_list = []
    lines = d.split("\n")
    for line in lines:
        data_list.append(list(map(int, line.split())))
    return data_list


def get_checksum(d):
    checksum = 0
    for line in d:
        checksum += max(line) - min(line)
    return checksum


def get_divisions(d):
    div_sum = 0
    for line in d:
        for comb in combinations(line, 2):
            if max(comb) % min(comb) == 0:
                div_sum += max(comb) // min(comb)
                break
    return div_sum


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def run():
    data = load_data("Day02.txt")
    nums = prepare(data)
    print(f"The checksum is {get_checksum(nums)}")
    print(f"The sum of divisions is {get_divisions(nums)}")
