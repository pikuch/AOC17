from functools import reduce


# Knot hash calculations in one class
class KnotHash:
    def __init__(self, s):
        self.dense_hash = None
        self.hex_hash = None
        self.bin_hash = None
        self.hash = list(range(256))
        self.input_data = list(map(ord, s)) + [17, 31, 73, 47, 23]
        self.calculate_hash()

    def hex(self):
        if self.hex_hash is None:
            self.calculate_hex_hash()
        return self.hex_hash

    def bin(self):
        if self.bin_hash is None:
            self.calculate_bin_hash()
        return self.bin_hash

    def calculate_hash(self):
        pos = 0
        skip_size = 0
        for span in self.input_data * 64:
            if pos + span < len(self.hash):
                reversed_values = self.hash[pos: pos + span]
                reversed_values.reverse()
                self.hash = self.hash[:pos] + reversed_values + self.hash[pos + span:]
            else:
                reversed_values = self.hash[pos:] + self.hash[:pos + span - len(self.hash)]
                reversed_values.reverse()
                self.hash = reversed_values[:pos + span - len(self.hash)]\
                    + self.hash[pos + span - len(self.hash):pos]\
                    + reversed_values[pos + span - len(self.hash):]
                for i in range(span):
                    self.hash[(pos + i) % len(self.hash)] = reversed_values[i]

            pos = (pos + span + skip_size) % len(self.hash)
            skip_size += 1
        self.dense_hash = [reduce(lambda x, y: x ^ y, self.hash[i * 16:i * 16 + 16], 0) for i in range(16)]

    def calculate_hex_hash(self):
        self.hex_hash = bytes(self.dense_hash).hex()

    def calculate_bin_hash(self):
        bit_chars = reduce(lambda x, y: x + y, map(lambda x: list(f"{x:08b}"), self.dense_hash), [])
        self.bin_hash = list(map(int, bit_chars))
