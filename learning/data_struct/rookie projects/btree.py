class treenode:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = treenode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = treenode(value)
            else:
                self.right.insert(value)
    def inorder_traversal(self):
        if self.right:
            self.right.inorder_traversal()
            print(self.value)
        if self.left:
            self.left.inorder_traversal()
            print(self.value)
    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
            print(self.value)
        if self.right:
            self.right.postorder_traversal()
            print(self.value)
    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
            print(self.value)
        if self.right:
            self.right.preorder_traversal()
            print(self.value)
        
root_node = treenode(int(input("input a number as a root node: ")))
num_of_other_nodes = int(input("how many other nodes do you need: "))
i = 0
while i<=num_of_other_nodes:
    node = int(input("put a number as a node other than the root node: "))
    root_node.insert(node)
    i+=1
root_node.inorder_traversal()