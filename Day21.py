# AOC17 day 21
import numpy as np


def text_to_numpy(code):
    digits = list(map(lambda x: x.replace(".", "0").replace("#", "1"), code.split("/")))
    for line in range(len(digits)):
        digits[line] = list(map(int, list(digits[line])))
    return np.array(digits, dtype=np.uint8)


def get_all_transformations(tile):
    transformations = [tile,
                       np.rot90(tile),
                       np.rot90(np.rot90(tile)),
                       np.rot90(np.rot90(np.rot90(tile))),
                       np.flipud(tile),
                       np.rot90(np.flipud(tile)),
                       np.rot90(np.rot90(np.flipud(tile))),
                       np.rot90(np.rot90(np.rot90(np.flipud(tile)))),
                       ]
    unique_t = {t.tostring(): t for t in transformations}
    return unique_t.values()


def parse_rules(lines):
    rules2 = []
    rules3 = []
    for line in lines:
        words = line.split()
        for transformed in get_all_transformations(text_to_numpy(words[0])):
            if len(words[0]) == 5:
                rules2.append([transformed, text_to_numpy(words[2])])
            elif len(words[0]) == 11:
                rules3.append([transformed, text_to_numpy(words[2])])
            else:
                print(f"Unsupported rule length: {words[0]}")
                exit(1)
    return rules2, rules3


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def get_pattern(pat, rules):
    for i in range(len(rules)):
        if np.all(rules[i][0] == pat):
            return rules[i][1]
    return None


def convert2(pattern, rules):
    new_pattern = np.zeros((pattern.shape[0] * 3 // 2, pattern.shape[1] * 3 // 2), dtype=np.uint8)
    for row in range(pattern.shape[0] // 2):
        for col in range(pattern.shape[1] // 2):
            subpattern = pattern[row * 2: row * 2 + 2, col * 2: col * 2 + 2]
            new_pattern[row * 3: row * 3 + 3, col * 3: col * 3 + 3] = get_pattern(subpattern, rules)
    return new_pattern


def convert3(pattern, rules):
    new_pattern = np.zeros((pattern.shape[0] * 4 // 3, pattern.shape[1] * 4 // 3), dtype=np.uint8)
    for row in range(pattern.shape[0] // 3):
        for col in range(pattern.shape[1] // 3):
            subpattern = pattern[row * 3: row * 3 + 3, col * 3: col * 3 + 3]
            new_pattern[row * 4: row * 4 + 4, col * 4: col * 4 + 4] = get_pattern(subpattern, rules)
    return new_pattern


def add_iterations(pattern, n, rules2, rules3):
    for i in range(n):
        print(f"\rbuilding iteration {i}/{n}, the array is {pattern.shape[1]}x{pattern.shape[0]}", end="")
        if pattern.shape[0] % 2:  # divisible by 3
            pattern = convert3(pattern, rules3)
        else:  # divisable by 2
            pattern = convert2(pattern, rules2)
    print(" ..done.")
    return pattern


def run():
    data = load_data("Day21.txt")
    rules2, rules3 = parse_rules(data.split("\n"))
    pattern = text_to_numpy(".#./..#/###")
    pattern5 = add_iterations(pattern, 5, rules2, rules3)
    print(f"After 5 iterations pattern has {np.sum(pattern5)} pixels on")
    pattern18 = add_iterations(pattern, 18, rules2, rules3)
    print(f"After 18 iterations pattern has {np.sum(pattern18)} pixels on")
