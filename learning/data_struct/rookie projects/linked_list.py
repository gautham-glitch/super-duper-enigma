class node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value

class L_list:
    def __init__(self, elements):
        self.elements = elements
        self.nodes = []

    def link(self):
        self.nodes = [node(val) for val in self.elements]

        for i in range(len(self.nodes)):
            self.nodes[i].prev = self.nodes[i - 1] if i > 0 else self.nodes[-1]
            self.nodes[i].next = self.nodes[i + 1] if i < len(self.nodes) - 1 else self.nodes[0]

    def delete(self, item):
        self.elements.remove(item)
        self.link()
    
    def add(self, item):
        self.elements.append(item)
        self.link()


    def __str__(self):
        result = []
        for n in self.nodes:
            prev_val = n.prev.value if n.prev else None
            next_val = n.next.value if n.next else None
            result.append(f"({prev_val} <- {n.value} -> {next_val})")
        return " <-> ".join(result)

# Usage
obj = L_list([1, 2, 3, 4, 5])
obj.add(6)
print(obj)
       