class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


class BinaryTree(object):
	def __init__(self, root):
		self.root = Node(root)

		
	def height(self, root):
		if not root:
			return 0
		return 1 + max(self.height(root.left), self.height(root.right))


# Calculate height of binary tree:
#     1
#    / \
#   2  3
#  / \
# 4  5
#
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.height(tree.root))

