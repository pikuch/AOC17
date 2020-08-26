# AOC17 day 09


def parse(s):
    score = 0
    garbage_counter = 0
    group_level = 0
    garbage = False
    index = 0
    while index < len(s):
        if garbage:
            if s[index] == "!":
                index += 2
            elif s[index] == ">":
                garbage = False
                index += 1
            else:
                index += 1
                garbage_counter += 1
        else:  # not in garbage
            if s[index] == "!":
                index += 2
            elif s[index] == "<":
                garbage = True
                index += 1
            elif s[index] == "{":
                group_level += 1
                score += group_level
                index += 1
            elif s[index] == "}":
                group_level -= 1
                index += 1
            else:
                index += 1
    return score, garbage_counter


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def run():
    data = load_data("Day09.txt")
    score, garbage_counter = parse(data)
    print(f"The score of the stream is {score} and there are {garbage_counter} garbage characters")
