# AOC17 day 15


def get_starting_numbers(data):
    lines = data.split("\n")
    return tuple(map(lambda x: int(x.split()[-1]), lines))


def count_matching(starting_pair, pair_count):
    factor_a, factor_b = 16807, 48271
    divider = 2147483647
    a, b = starting_pair
    score = 0
    for i in range(pair_count):
        a = (a * factor_a) % divider
        b = (b * factor_b) % divider
        if a % 65536 == b % 65536:
            score += 1
        if i % 10**4 == 0:
            print(f"\rchecking {100*i/pair_count:.1f}%", end="")
    print(" done.")
    return score


def count_matching_picky(starting_pair, pair_count):
    factor_a, factor_b = 16807, 48271
    divider = 2147483647
    a, b = starting_pair
    score = 0
    for i in range(pair_count):
        while True:
            a = (a * factor_a) % divider
            if a % 4 == 0:
                break
        while True:
            b = (b * factor_b) % divider
            if b % 8 == 0:
                break
        if a % 65536 == b % 65536:
            score += 1
        if i % 10**3 == 0:
            print(f"\rchecking {100*i/pair_count:.1f}%", end="")
    print(" done.")
    return score


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def run():
    data = load_data("Day15.txt")
    starting_pair = get_starting_numbers(data)
    # test data
    # starting_pair = (65, 8921)
    pair_count = 4*10**7
    print(f"Judge counted {count_matching(starting_pair, pair_count)} matching endings")
    pair_count = 5*10**6
    print(f"Judge now counted {count_matching_picky(starting_pair, pair_count)} matching endings")
