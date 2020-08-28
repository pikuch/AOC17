# AOC17 day 22
from collections import defaultdict


def parse_input(data):
    cluster = defaultdict(lambda: 0)
    half_width = len(data[0]) // 2
    half_height = len(data) // 2
    for row in range(len(data)):
        for col in range(len(data[0])):
            cluster[(row - half_height, col - half_width)] = 0 if data[row][col] == "." else 1
    return cluster


def parse_input2(data):
    cluster = defaultdict(lambda: 'C')
    half_width = len(data[0]) // 2
    half_height = len(data) // 2
    for row in range(len(data)):
        for col in range(len(data[0])):
            cluster[(row - half_height, col - half_width)] = 'C' if data[row][col] == "." else "I"
    return cluster


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def sporifica(n, cluster):
    row, col = 0, 0
    direction = 0
    move_row = {0: -1, 1: 0, 2: 1, 3: 0}
    move_col = {0: 0, 1: 1, 2: 0, 3: -1}
    infections = 0
    for _ in range(n):
        # turn
        if cluster[(row, col)]:
            direction = (direction + 1) % 4
        else:
            direction = (direction + 3) % 4
            infections += 1
        # modify current node
        cluster[(row, col)] = 1 - cluster[(row, col)]
        # move
        row += move_row[direction]
        col += move_col[direction]
    return infections


def sporifica2(n, cluster):
    row, col = 0, 0
    direction = 0
    move_row = {0: -1, 1: 0, 2: 1, 3: 0}
    move_col = {0: 0, 1: 1, 2: 0, 3: -1}
    changes = {'C': 'W', 'W': 'I', 'I': 'F', 'F': 'C'}
    infections = 0
    for i in range(n):
        if i % 10**5 == 0:
            print(f"\rsimulating {100*i/n:.1f}%", end="")
        # turn
        if cluster[(row, col)] == 'C':
            direction = (direction + 3) % 4
        elif cluster[(row, col)] == 'I':
            direction = (direction + 1) % 4
        elif cluster[(row, col)] == 'F':
            direction = (direction + 2) % 4
        elif cluster[(row, col)] == 'W':
            infections += 1
        else:
            print(f"Illegal state: {cluster[(row, col)]}")
            exit(1)

        # modify current node
        cluster[(row, col)] = changes[cluster[(row, col)]]
        # move
        row += move_row[direction]
        col += move_col[direction]
    print(" done.\r", end="")
    return infections


def run():
    data = load_data("Day22.txt")
    # test data
    # data = "..#\n#..\n..."
    cluster = parse_input(data.split("\n"))
    infections = sporifica(10**4, cluster)
    print(f"There were {infections} infections")

    cluster2 = parse_input2(data.split("\n"))
    infections2 = sporifica2(10**7, cluster2)
    print(f"There were now {infections2} infections")
