# AOC17 day 05


def escape_program(prog):
    steps = 0
    index = 0
    while 0 <= index < len(prog):
        new_index = index + prog[index]
        prog[index] += 1
        index = new_index
        steps += 1
    return steps


def escape_program_2(prog):
    steps = 0
    index = 0
    while 0 <= index < len(prog):
        new_index = index + prog[index]
        prog[index] += 1 if prog[index] < 3 else -1
        index = new_index
        steps += 1
    return steps


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def run():
    data = load_data("Day05.txt")
    prog = list(map(int, data.split("\n")))
    prog2 = prog[:]  # a copy before modification is needed
    print(f"It takes {escape_program(prog)} steps to jump out of the program")
    print(f"It takes {escape_program_2(prog2)} steps to jump out of the program with rule 2")
