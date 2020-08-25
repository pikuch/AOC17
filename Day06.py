# AOC17 day 06


def redistribute(blocks):
    pos = blocks.index(max(blocks))
    count = blocks[pos]
    blocks[pos] = 0
    base = count // len(blocks)
    remainder = count % len(blocks)
    for i in range(pos + 1, pos + 1 + len(blocks)):
        if remainder:
            blocks[i % len(blocks)] += base + 1
            remainder -= 1
        else:
            blocks[i % len(blocks)] += base


def count_redistributions(blocks):
    seen = {tuple(blocks): 0}
    redis = 0
    while True:
        redistribute(blocks)
        redis += 1
        if tuple(blocks) in seen:
            break
        else:
            seen[tuple(blocks)] = redis
    return redis, redis - seen[tuple(blocks)]


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def run():
    data = load_data("Day06.txt")
    blocks = list(map(int, data.split()))
    first_seen, loop_size = count_redistributions(blocks)
    print(f"The infinite loop is detected after {first_seen} redistributions and the loop length is {loop_size}")
