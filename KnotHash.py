from functools import reduce


# Knot hash calculations in one class
class KnotHash:
    def __init__(self, data):
        self.hash = list(range(256))
        self.calculate_sparse_hash(data)
        self.hex_hash = None

    def hex(self):
        if self.hex_hash is None:
            self.hex_hash = self.calculate_dense_hash()
        return self.hex_hash

    def calculate_sparse_hash(self, spans):
        pos = 0
        skip_size = 0
        for span in spans * 64:
            reversed_values = []
            for i in range(span):
                reversed_values.append(self.hash[(pos + i) % len(self.hash)])
            reversed_values.reverse()
            for i in range(span):
                self.hash[(pos + i) % len(self.hash)] = reversed_values[i]
            pos = (pos + span + skip_size) % len(self.hash)
            skip_size += 1

    def calculate_dense_hash(self):
        xord = [reduce(lambda x, y: x ^ y, self.hash[i * 16:i * 16 + 16], 0) for i in range(16)]
        return bytes(xord).hex()
