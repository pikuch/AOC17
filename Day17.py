# AOC17 day 17

def build_buffer(steps):
    n = 0
    buffer = [n]
    pos = 0
    while n < 2017:
        pos = (pos + steps) % len(buffer)
        n += 1
        buffer.insert(pos + 1, n)
        pos += 1
    return buffer[(pos + 1) % len(buffer)]


# don't build a buffer, just track its size and what's after 0
def no_buffer_50M(steps):
    n = 0
    item_after_0 = 0
    buf_len = 1
    pos = 0
    while n < 5*10**7:
        pos = (pos + steps) % buf_len
        n += 1
        if pos == 0:
            item_after_0 = n
        buf_len += 1
        pos += 1
        if n % 10**5 == 0:
            print(f"\rbuilding a buffer {100*n/(5*10**7):.1f}%", end="")
    print(" done.")
    return item_after_0


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def run():
    data = load_data("Day17.txt")
    steps = int(data)
    # test data
    # steps = 3
    print(f"The value after the last inserted is {build_buffer(steps)}")
    print(f"The value after 0 with 50M inserted is {no_buffer_50M(steps)}")
