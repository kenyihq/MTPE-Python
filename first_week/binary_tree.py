class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

class Tree:
    def __init__(self):
        self.root = None


    def add(self, val):
        if self.root is None:
            self.root = Node(val)

        else:
            self.add_val(val, self.root)

    def add_val(self, val, node):
        if val < node.value:
            if node.left is not None:
                self.add_val(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right is not None:
                self.add_val(val, node.right)
            else:
                node.right = Node(val)

    def search(self, val):
        if self.root is not None:
            return self.search_val(val, self.root)
        else:
            return None

    def search_val(self, val, node):
        if val == node.value:
            return node
        elif(val < node.value and node.left is not None):
            return self.search_val(val, node.left)
        elif (val > node.value and node.right is not None):
            return self.search_val(val, node.right)


    def print_tree(self):
        if self.root is not None:
            self.print_all(self.root)

    def print_all(self, node):
        if node is not None:
            self.print_all(node.left)
            print(str(node.value))
            self.print_all(node.right)


def run():
    tree = Tree()
    tree.add(15)
    tree.add(7)
    tree.add(2)
    tree.add(10)
    tree.add(3)
    tree.print_tree()

if __name__ == '__main__':
    run()