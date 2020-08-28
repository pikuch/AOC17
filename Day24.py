# AOC17 day 24

def make_components(data):
    return tuple(map(lambda x: tuple(map(int, x.split("/"))), data))


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def find_max_strength_and_length(components, endings):
    max_length = 0
    max_length_strength = 0
    max_strength = 0
    to_check = [(set(), 0, 0, 0)]  # used components, last connector, strength so far
    while len(to_check):
        used, connector, strength, length = to_check.pop(0)
        if strength > max_strength:
            max_strength = strength
        if length > max_length:
            max_length = length
            max_length_strength = strength
        if length == max_length and strength > max_length_strength:
            max_length_strength = strength
        if connector in endings:
            continue
        for i in range(len(components)):
            if i not in used:
                if components[i][0] == connector:
                    new_used = used.copy()
                    new_used.add(i)
                    to_check.append((new_used, components[i][1], strength + sum(components[i]), length + 1))
                elif components[i][1] == connector:
                    new_used = used.copy()
                    new_used.add(i)
                    to_check.append((new_used, components[i][0], strength + sum(components[i]), length + 1))
                else:
                    pass

    return max_strength, max_length, max_length_strength


# prepares a set of connectors that have no pairs
def find_endings(components):
    counts = dict()
    for i in range(len(components)):
        for j in range(2):
            if components[i][j] not in counts:
                counts[components[i][j]] = 1
            else:
                counts[components[i][j]] += 1
    endings = set()
    for ending, n in counts.items():
        if n == 1:
            endings.add(ending)
    return endings


def run():
    data = load_data("Day24.txt")
    # test data
    # data = "0/2\n2/2\n2/3\n3/4\n3/5\n0/1\n10/1\n9/10"
    components = make_components(data.split("\n"))
    endings = find_endings(components)
    strength, length, long_strength = find_max_strength_and_length(components, endings)
    print(f"The highest possible strength is {strength}")
    print(f"The longest possible bridge is {length} long and has a strength of {long_strength}")
