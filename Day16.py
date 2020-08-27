# AOC17 day 16


def dance(progs, moves):
    for m in moves:
        if m[0] == "s":
            c = int(m[1])
            progs = progs[-c:] + progs[:-c]
        elif m[0] == "x":
            p1, p2 = int(m[1]), int(m[2])
            progs[p1], progs[p2] = progs[p2], progs[p1]
        elif m[0] == "p":
            p1, p2 = progs.index(m[1]), progs.index(m[2])
            progs[p1], progs[p2] = progs[p2], progs[p1]
        else:
            print(f"Illegal dance move: {m}")
            exit(1)
    return progs


def dance_b(progs, moves):  # finds a cycle and takes a shortcut
    progs0 = progs[:]
    i = 0
    while True:
        progs = dance(progs, moves)
        i += 1
        if progs == progs0:
            break
    i = 10**9 % i
    while i:
        progs = dance(progs, moves)
        i -= 1
    return progs


def parse_moves(data):
    return list(map(lambda x: [x[0]] + x[1:].split("/"), data.split(",")))


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def run():
    data = load_data("Day16.txt")
    moves = parse_moves(data)
    progs = list(map(lambda x: chr(x + ord('a')), range(16)))
    # test data
    # progs = ['a', 'b', 'c', 'd', 'e']
    # moves = parse_moves("s1,x3/4,pe/b")
    progs = dance(progs, moves)
    print(f"{''.join(progs)}")
    progs = list(map(lambda x: chr(x + ord('a')), range(16)))
    progs = dance_b(progs, moves)
    print(f"{''.join(progs)}")
