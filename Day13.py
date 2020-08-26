# AOC17 day 13


def move_firewall(firewall):
    for layer in firewall:
        if layer is not None:
            if not 0 <= layer["pos"] + layer["dir"] < layer["range"]:
                layer["dir"] = -layer["dir"]
            layer["pos"] += layer["dir"]


def move_firewall_by(delay, firewall):
    for layer in firewall:
        if layer is not None:
            full_cycles = delay // ((layer["range"] - 1) * 2)
            additional = delay - full_cycles * (layer["range"] - 1) * 2
            while additional:
                if not 0 <= layer["pos"] + layer["dir"] < layer["range"]:
                    layer["dir"] = -layer["dir"]
                layer["pos"] += layer["dir"]
                additional -= 1


def position_at_depth(d, t, firewall):
    full_cycles = (d + t) // ((firewall[d]["range"] - 1) * 2)
    additional = (d + t) - full_cycles * (firewall[d]["range"] - 1) * 2
    pos = firewall[d]["pos"]
    direction = firewall[d]["dir"]
    while additional:
        if not 0 <= pos + direction < firewall[d]["range"]:
            direction = -direction
        pos += direction
        additional -= 1
    return pos


def check_severity(firewall):
    severity = 0
    for depth in range(len(firewall)):
        if firewall[depth] is not None:
            if firewall[depth]["pos"] == 0:
                severity += depth * firewall[depth]["range"]
        move_firewall(firewall)
    return severity


def check_can_pass(delay, firewall):
    move_firewall_by(delay, firewall)

    for depth in range(len(firewall)):
        if firewall[depth] is not None:
            if firewall[depth]["pos"] == 0:
                return False
        move_firewall(firewall)
    return True


def check_can_pass_v2(delay, firewall):
    for depth in range(len(firewall)):
        if firewall[depth] is not None:
            if position_at_depth(depth, delay, firewall) == 0:
                return False
    return True


def find_min_delay(firewall):
    delay = 0
    while True:
        if delay % 1000 == 0:
            print(f"\rchecking delay {delay}", end="")
        reset_firewall(firewall)
        if check_can_pass(delay, firewall):
            break
        delay += 1
    print(" found!")
    return delay


def find_min_delay_v2(firewall):
    delay = 0
    reset_firewall(firewall)
    while True:
        if delay % 1000 == 0:
            print(f"\rchecking delay {delay}+", end="")
        if check_can_pass_v2(delay, firewall):
            break
        delay += 1
    print(" ..found!")
    return delay


def construct_firewall(s):
    fw = {}
    firewall = []
    max_depth = 0
    for line in s.split("\n"):
        words = line.split()
        depth = int(words[0].replace(":", ""))
        fw[depth] = {"range": int(words[1]), "pos": 0, "dir": 1}  # depth, range, position, direction
        if depth > max_depth:
            max_depth = depth
    for i in range(max_depth + 1):
        if i in fw:
            firewall.append(fw[i])
        else:
            firewall.append(None)
    return firewall


def reset_firewall(firewall):
    for depth in firewall:
        if depth is not None:
            depth["pos"] = 0
            depth["dir"] = 1


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def run():
    data = load_data("Day13.txt")
    # test data, should give 24 and 10
    # data = "0: 3\n1: 2\n4: 4\n6: 4"
    firewall = construct_firewall(data)
    severity = check_severity(firewall)
    print(f"Starting at moment 0 gives severity {severity}")
    print(f"Minimum delay to not get caught is {find_min_delay_v2(firewall)}")
