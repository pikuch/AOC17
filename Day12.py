# AOC17 day 12


def get_connected(node0, net):
    con_list = []
    to_check = [node0]
    while len(to_check):
        current = to_check.pop(0)
        if current not in con_list:
            con_list.append(current)
            to_check.extend(net[current])
    return con_list


# clears the net, oops ¯\_(ヅ)_/¯
def count_groups(net):
    group_counter = 0
    while len(net):
        connected = get_connected(next(iter(net)), net)
        group_counter += 1
        for node in connected:
            del net[node]
    return group_counter


def make_net(data):
    net = {}
    for line in data.split("\n"):
        words = line.split()
        net[int(words[0])] = list(map(lambda x: int(x.replace(",", "")), words[2:]))
    return net


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def run():
    data = load_data("Day12.txt")
    net = make_net(data)
    connected_to_0 = get_connected(0, net)
    print(f"There are {len(connected_to_0)} programs connected to program 0")
    print(f"There are {count_groups(net)} groups of programs")
