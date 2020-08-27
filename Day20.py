# AOC17 day 20


def parse_data(data):
    particles = []
    for line in data.split("\n"):
        particles.append(list(map(lambda x: list(map(int, x.strip("pva=<>,").split(","))), line.split())))
    return particles


def how_far_will_the_ith_particle_be(i, particles, n):
    # pn = p0 + n v0 + (n^2+n)/2 a0
    pos = [particles[i][0][x] + n * particles[i][1][x] + (n * n + n) // 2 * particles[i][2][x] for x in range(3)]
    return sum(map(abs, pos))


def long_run_closest(particles, after_n):
    closest = 0
    closest_dist = how_far_will_the_ith_particle_be(0, particles, after_n)
    for i in range(len(particles)):
        current_dist = how_far_will_the_ith_particle_be(i, particles, after_n)
        if current_dist < closest_dist:
            closest_dist = current_dist
            closest = i
    return closest


def where_will_the_nth_particle_be(i, particles, n):
    # pn = p0 + n v0 + (n^2+n)/2 a0
    return tuple([particles[i][0][x] + n * particles[i][1][x] + (n * n + n) // 2 * particles[i][2][x] for x in range(3)])


def get_positions(t, particles):
    return list(map(lambda x: where_will_the_nth_particle_be(x, particles, t), range(len(particles))))


def look_for_collisions(particles):
    t = 0
    while t < 500:
        t += 1
        positions = get_positions(t, particles)
        to_remove = set()
        for p1 in range(len(positions)):
            for p2 in range(p1 + 1, len(positions)):
                if positions[p1] == positions[p2]:
                    to_remove.add(p1)
                    to_remove.add(p2)
        print(f"\rAt t={t} there were {len(particles)} particles,", end="")
        for p in sorted(list(to_remove), reverse=True):
            del particles[p]
        print(f" {len(to_remove)} particles collided, leaving {len(particles)} particles", end="")
    print(" ..enough searching")
    return len(particles)


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def run():
    data = load_data("Day20.txt")
    particles = parse_data(data)
    print(f"The particle closest to (0,0,0) in the long run is {long_run_closest(particles, 10000)}")
    leftover = look_for_collisions(particles)
    print(f"There are {leftover} uncolided particles left")
