# AOC17 day 18
from Duet import Duet


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def run():
    data = load_data("Day18.txt")
    # test data
    # data = "snd 1\nsnd 2\nsnd p\nrcv a\nrcv b\nrcv c\nrcv d"
    duet = Duet()
    duet.load(data.split("\n"))
    duet.run()
    # The first recovered frequency was 4601
    print(f"Program 1 sent a value {duet.send_count[1]} times")
