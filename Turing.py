from collections import defaultdict


class Turing:
    def __init__(self):
        self.state = ""
        self.states = dict()
        self.tape = defaultdict(lambda: 0)
        self.cursor = 0
        self.step = 0
        self.stop = 0

    def load(self, data):
        i = 0
        while i < len(data):
            if len(data[i]) == 0:
                i += 1
                continue
            else:
                words = data[i].split()

            if words[0] == "Begin":
                self.state = words[3].strip(".")
                i += 1
            elif words[0] == "Perform":
                self.stop = int(words[5])
                i += 1
            elif words[0] == "In":
                state_name = words[2].strip(":")
                write0 = int(data[i+2].split()[4].strip("."))
                move0 = 1 if data[i+3].split()[6] == "right." else -1
                new_state0 = data[i+4].split()[4].strip(".")
                write1 = int(data[i+6].split()[4].strip("."))
                move1 = 1 if data[i+7].split()[6] == "right." else -1
                new_state1 = data[i+8].split()[4].strip(".")
                self.states[state_name] = {0: (write0, move0, new_state0), 1: (write1, move1, new_state1)}
                i += 9

    def run(self):
        while self.step < self.stop:
            if self.step % 10**5 == 0:
                print(f"\rturing progress is {100 * self.step / self.stop:.1f}%", end="")
            inst = self.states[self.state][self.tape[self.cursor]]
            self.tape[self.cursor] = inst[0]
            self.cursor += inst[1]
            self.state = inst[2]
            self.step += 1
        print(" done.")
        return sum(self.tape.values())
