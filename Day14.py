# AOC17 day 14
from functools import reduce
from KnotHash import KnotHash


def get_grid(data):
    grid = []
    for row in range(128):
        grid.append(KnotHash(data + "-" + str(row)).bin())
    return grid


def show_grid(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col]:
                print("#", end="")
            else:
                print(".", end="")
        print("")


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def run():
    data = load_data("Day14.txt")
    # test data
    # data = "flqrgnkx"
    grid = get_grid(data)
    used = sum(map(lambda x: sum(x), grid))
    print(f"There are {used} squares used")
