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


def sum_neighbours(coords, cells):
    summer = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if (coords[0] + dx, coords[1] + dy) in cells:
                summer += cells[(coords[0] + dx, coords[1] + dy)]
    return summer


def stress_test(cell_value):
    coords = [0, 0]
    cells = {(0, 0): 1}
    step = -1
    current = 1
    axis = 0
    sign = 0
    while current <= cell_value:
        step += 1
        axis = step % 2
        sign = (((step - 1) // 2) % 2) * 2 - 1
        dist = step // 2 + 1
        for i in range(dist):
            coords[axis] += sign
            current = sum_neighbours(coords, cells)
            cells[tuple(coords)] = current
            if current > cell_value:
                break
    # return current value
    return current


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def run():
    data = load_data("Day03.txt")
    cell = int(data)
    print(f"Cell {cell} is {calculate_distance(cell)} cells away from center")
    print(f"The first cell with a value larger than {cell} is {stress_test(cell)}")
