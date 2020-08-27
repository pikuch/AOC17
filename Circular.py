
class Cnode:
    def __init__(self, value):
        self.value = value
        self.next = self
        self.prev = self


class Circular:
    def __init__(self, value):
        self.head = Cnode(value)
        self.length = 1

    def insert_after_current(self, value):
        new_node = Cnode(value)
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next.prev = new_node
        self.head.next = new_node
        self.head = new_node
        self.length += 1

    def insert_from_list(self, value_list):
        for value in value_list:
            self.insert_after_current(value)

    def go_to_node_with_value(self, value):
        if self.head.value == value:
            return
        current = self.head.next
        while current != self.head:
            if current.value == value:
                self.head = current
                return
            current = current.next

    def step_forward(self, steps):
        if steps > self.length:
            steps = steps % self.length
        while steps:
            self.head = self.head.next
            steps -= 1
