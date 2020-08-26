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


def remove_region(squares):
    to_check = [squares.pop()]
    while len(to_check):
        row, col = to_check.pop(0)
        for pair in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if pair in squares:
                to_check.append(pair)
                squares.remove(pair)


def count_regions(grid):
    squares = set()
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col]:
                squares.add((row, col))
    regions = 0
    while len(squares):
        remove_region(squares)
        regions += 1
    return regions


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
    print(f"There are {count_regions(grid)} regions present")
