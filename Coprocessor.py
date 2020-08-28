
class Coprocessor:
    def __init__(self):
        self.pc = 0
        self.reg = {}
        self.prog = ()
        self.instructions = {"set": self.set,
                             "sub": self.sub,
                             "mul": self.mul,
                             "jnz": self.jnz}
        self.mul_invocations = 0

    ##############################################################
    # instructions
    ##############################################################

    def set(self, args):
        self.reg[args[0]] = self.reg[args[1]]
        self.pc += 1

    def sub(self, args):
        self.reg[args[0]] -= self.reg[args[1]]
        self.pc += 1

    def mul(self, args):
        self.reg[args[0]] *= self.reg[args[1]]
        self.pc += 1
        self.mul_invocations += 1

    def jnz(self, args):
        if self.reg[args[0]]:
            self.pc += self.reg[args[1]]
        else:
            self.pc += 1

    ##############################################################

    def load(self, lines):
        registers = "abcdefgh"
        const_index = 0
        prog_constructor = []
        for line in lines:
            words = line.split()
            for i in range(1, len(words)):
                if words[i] not in registers:
                    self.reg[const_index] = int(words[i])
                    words[i] = const_index
                    const_index += 1
                else:
                    self.reg[words[i]] = 0
            prog_constructor.append(tuple(words))
        self.prog = tuple(prog_constructor)

    def execute(self, inst):
        self.instructions[inst[0]](inst[1:])

    def run(self):
        while True:
            if self.pc < 0 or self.pc >= len(self.prog):
                break
            self.execute(self.prog[self.pc])
