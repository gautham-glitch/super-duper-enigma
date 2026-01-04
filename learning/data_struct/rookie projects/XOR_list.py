class node:
    def __init__(self, data, pxn):
        self.data = data
        self.pxn = pxn
    
    def __repr__(self):
        return f"Data = {self.data}, pointer = {self.pxn}"

class XOR_list:
    def __init__(self, elements: list):
        self.elements = elements
        self.nodes = []
    
    def link(self):
        for i in range(len(self.elements)):
            if i < len(self.elements) - 1 and i > 0 :
                pxn = self.elements[i-1] ^ self.elements[i+1]
            elif i == len(self.elements) - 1:
                pxn = self.elements[i-1] ^ 0
            else:
                pxn = 0 ^ self.elements[i+1]
            
            self.nodes.append(node(self.elements[i], pxn))
        return self.nodes
    
    def delete(self, data):
        self.elements.remove(data)
        self.nodes.clear()
        self.link()
    
    def add(self, data):
        self.elements.append(data)
        self.nodes.clear()
        self.link()
    
def traverse(xor_list):
    nodes = xor_list.nodes
    if not nodes:
        return []

    result = []
    prev_data = 0
    current = nodes[0]

    for _ in range(len(nodes)):
        result.append(current.data)
        next_data = current.pxn ^ prev_data

        # Find the next node by data value
        next_node = next((n for n in nodes if n.data == next_data), None)
        if not next_node:
            break

        prev_data = current.data
        current = next_node

    return result


xlist = XOR_list([1,2,3,4,5,6])
print(xlist.link())
print(xlist.delete(5))
print(traverse(xlist))
print(xlist.add(7))
print(traverse(xlist))    