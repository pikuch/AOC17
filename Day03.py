# AOC17 day 03


def calculate_distance(cell_number):
    coords = [0, 0]
    step = -1
    current = 1
    axis = 0
    sign = 0
    while current < cell_number:
        step += 1
        axis = step % 2
        sign = (((step - 1) // 2) % 2) * 2 - 1
        dist = step // 2 + 1
        current += dist
        coords[axis] += sign * dist
    # go back a few cells if needed
    if current > cell_number:
        coords[axis] -= sign * (current - cell_number)
    # return manhattan distance
    return abs(coords[0]) + abs(coords[1])


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def run():
    data = load_data("Day03.txt")
    cell = int(data)
    print(f"Cell {cell} is {calculate_distance(cell)} cells away from center")
