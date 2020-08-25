# AOC17 day 04
from itertools import combinations, permutations


def is_valid(s):
    words = s.split()
    for comb in combinations(words, 2):
        if comb[0] == comb[1]:
            return False
    return True


def is_valid_strict(s):
    words = s.split()
    for comb in combinations(words, 2):
        if len(comb[0]) == len(comb[1]) and tuple(comb[0]) in permutations(comb[1]):
            return False
    return True


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def run():
    data = load_data("Day04.txt")
    phrases = data.split("\n")
    print(f"There are {sum(map(is_valid, phrases))} valid passphrases")
    print(f"There are {sum(map(is_valid_strict, phrases))} valid passphrases when using strict rules")
