
class Duet:
    def __init__(self):
        self.id = 0
        self.pc = [0, 0]
        self.send_count = [0, 0]
        self.finished = [False, False]
        self.reg = [[0] * (1 + ord('z') - ord('a')), [0] * (1 + ord('z') - ord('a'))]
        self.queue = [[], []]
        self.prog = []
        self.instructions = {"snd": self.snd,
                             "set": self.set,
                             "add": self.add,
                             "mul": self.mul,
                             "mod": self.mod,
                             "rcv": self.rcv,
                             "jgz": self.jgz}
        # setup of ID registers
        self.reg[0][ord('p') - ord('a')] = 0
        self.reg[1][ord('p') - ord('a')] = 1

    def load(self, program):
        for item in program:
            words = item.split()
            for i in range(1, len(words)):
                if words[i].islower():
                    words[i] = ord(words[i]) - ord('a')
                else:
                    self.reg[0].append(int(words[i]))
                    self.reg[1].append(int(words[i]))
                    words[i] = len(self.reg[0]) - 1
            self.prog.append(words)

    #####################################################
    # Instructions
    #####################################################

    def snd(self, params):
        self.queue[1 - self.id].append(self.reg[self.id][params[0]])
        self.send_count[self.id] += 1
        self.pc[self.id] += 1

    def set(self, params):
        self.reg[self.id][params[0]] = self.reg[self.id][params[1]]
        self.pc[self.id] += 1

    def add(self, params):
        self.reg[self.id][params[0]] += self.reg[self.id][params[1]]
        self.pc[self.id] += 1

    def mul(self, params):
        self.reg[self.id][params[0]] *= self.reg[self.id][params[1]]
        self.pc[self.id] += 1

    def mod(self, params):
        self.reg[self.id][params[0]] %= self.reg[self.id][params[1]]
        self.pc[self.id] += 1

    def rcv(self, params):
        if len(self.queue[self.id]):
            self.reg[self.id][params[0]] = self.queue[self.id].pop(0)
            self.pc[self.id] += 1

    def jgz(self, params):
        if self.reg[self.id][params[0]] > 0:
            self.pc[self.id] += self.reg[self.id][params[1]]
        else:
            self.pc[self.id] += 1

    #####################################################

    def execute(self, inst):
        self.instructions[inst[0]](inst[1:])

    def run(self):
        while True:
            # program loop
            for self.id in range(2):
                if not self.finished[self.id]:
                    if self.pc[self.id] < 0 or self.pc[self.id] >= len(self.prog):
                        self.finished[self.id] = True
                    else:
                        self.execute(self.prog[self.pc[self.id]])

            # program ending checks
            if self.finished[0] and self.finished[1]:
                # out of instructions
                break
            if self.prog[self.pc[0]][0] == 'rcv' and self.prog[self.pc[1]][0] == 'rcv':
                if len(self.queue[0]) == 0 and len(self.queue[1]) == 0:
                    # deadlock
                    break
