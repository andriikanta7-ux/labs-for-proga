class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binary_tree_diameter(tree: BinaryTree) -> int:
    max_diameter = 0
    
    def height(node):
        nonlocal max_diameter
        
        if node is None:
            return -1 
        
        left_height = height(node.left)
        right_height = height(node.right)

        current_diameter = left_height + right_height + 2
        max_diameter = max(max_diameter, current_diameter)

        return max(left_height, right_height) + 1

    height(tree)
    return max_diameter
    