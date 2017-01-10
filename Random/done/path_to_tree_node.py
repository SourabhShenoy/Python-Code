import unittest

class TreeNode(object):

    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent

	@property
	def path_from_root(self):
		if self.parent:
			return self.parent.path_from_root + [self]
		return [self]

def _build_path_from_root(node, path):
    if node.parent:
        _build_path_from_root(node.parent, path)
    path.append(node)
    
class TreePathAsListTests(unittest.TestCase):

    def setUp(self):
        self.root = TreeNode(value="root")
        self.child_1 = TreeNode(value="child 1", parent=self.root)
        self.child_2 = TreeNode(value="child 2", parent=self.root)
        self.leaf_1a = TreeNode(value="leaf 1a", parent=self.child_1)

    def test_path_from_root(self):
        self.assertEquals([self.root, self.child_1, self.leaf_1a], self.leaf_1a.path_from_root)
        self.assertEquals([self.root, self.child_2], self.child_2.path_from_root)
        self.assertEquals([self.root], self.root.path_from_root)