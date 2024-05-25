from src.DataStructures.Tree.TreeNode import TreeNode


class BST:
    def __init__(self, value):
        self.root = TreeNode(value)

    def insert_node(self, value):
        new_node = TreeNode(value)
        curr = prev = self.root
        while curr is not None:
            prev = curr
            if new_node.value > curr.value:
                curr = curr.right
            elif new_node.value <= curr.value:
                curr = curr.left
        if new_node.value <= prev.value:
            prev.left = new_node
        else:
            prev.right = new_node
        print("Node inserted")

    def preorder_display(self, node):
        if node is None:
            return []

        res = [node.value]

        res += self.preorder_display(self.root.left)

        res += self.preorder_display(self.root.right)

        return res

    def display_tree(self):
        return self.preorder_display(self.root)
