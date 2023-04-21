class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert_data_to_root(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_data_to_child(data, self.root)
    
    def insert_data_to_child(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self.insert_data_to_child(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self.insert_data_to_child(data, current_node.right)
        
        else:
            print("The value already exists in the tree.")
    
    def print_root_node(self):
        if self.root is not None:
            self.print_child_node(self.root)

    def print_child_node(self, current_node):
        if current_node is not None:
            self.print_child_node(current_node.left)
            print(str(current_node.data), end=" ")
            self.print_child_node(current_node.right)

if __name__ =="__main__":
    tree = BinaryTree()
    vaule = list(map(int, input("Enter elements separated by space: ").split()))
    for i in vaule:
        tree.insert_data_to_root(i)
    tree.print_root_node()