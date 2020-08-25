# AOC17 day 01

def calculate_sum(s, ahead):
    digit_sum = 0
    for i in range(len(s)):
        if s[i] == s[(i + ahead) % len(s)]:
            digit_sum += int(s[i])
    return digit_sum


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def run():
    data = load_data("Day01.txt")
    print(f"The sum of digits repeating one ahead is {calculate_sum(data, 1)}")
    print(f"The sum of digits repeating half way around ahead is {calculate_sum(data, len(data)//2)}")
