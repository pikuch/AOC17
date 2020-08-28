# AOC17 day 25
from Turing import Turing


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def run():
    data = load_data("Day25.txt")
    tur = Turing()
    tur.load(data.split("\n"))
    checksum = tur.run()
    print(f"The checksum is {checksum}")
