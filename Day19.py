# AOC17 day 19


def navigate(paths):
    row = 0
    col = 0
    for col in range(len(paths[0])):
        if paths[0][col] == "|":
            break
    direction = "S"
    delta_row = {"N": -1, "S": 1, "E": 0, "W": 0}
    delta_col = {"N": 0, "S": 0, "E": 1, "W": -1}
    dir_choice = {"N": ("E", "W"), "S": ("E", "W"), "E": ("N", "S"), "W": ("N", "S")}
    visited = []
    steps = 0

    # follow the path
    while True:
        if paths[row][col] == "|" or paths[row][col] == "-":
            row += delta_row[direction]
            col += delta_col[direction]
        elif paths[row][col].isalpha():
            visited.append(paths[row][col])
            row += delta_row[direction]
            col += delta_col[direction]
        elif paths[row][col] == "+":
            if paths[row + delta_row[dir_choice[direction][0]]][col+delta_col[dir_choice[direction][0]]] == " ":
                direction = dir_choice[direction][1]
            else:
                direction = dir_choice[direction][0]
            row += delta_row[direction]
            col += delta_col[direction]
        elif paths[row][col] == " ":
            break
        else:
            print(f"Unrecognized character: {paths[row][col]}")
            exit(1)
        steps += 1

    return visited, steps


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def run():
    data = load_data("Day19.txt")
    paths = list(map(lambda x: x + " " * 100, data.split("\n")))
    visited, steps = navigate(paths)
    print(f"The packet visited {''.join(visited)} and made {steps} steps")
