# AOC17 day 11


def calculate(path):
    # using a skewed coordinate system
    max_dist = 0
    row, col = 0, 0
    trans = {"n": (-1, 0),
             "s": (1, 0),
             "nw": (0, -1),
             "se": (0, 1),
             "ne": (-1, 1),
             "sw": (1, -1)}
    for move in path:
        row += trans[move][0]
        col += trans[move][1]
        if dist(row, col) > max_dist:
            max_dist = dist(row, col)

    return dist(row, col), max_dist


def dist(row, col):
    # distance from 0, 0
    d = 0
    if row > 0 > col:
        d += min(row, -col)
        row -= d
        col += d
    if row < 0 < col:
        d += min(-row, col)
        row += d
        col -= d
    d += max(abs(row), abs(col))
    return d


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def run():
    data = load_data("Day11.txt")
    path = data.split(",")
    end_dist, max_dist = calculate(path)
    print(f"The child program is {end_dist} tiles away and was at most {max_dist} tiles away")
