class Node(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val

#Recursively parse the input and create a tree
def make_tree(values):
    if values is None:
        return None
    else:
        (root, left, right) = values
        r = Node(root)
        r.left = make_tree(left)
        r.right = make_tree(right)
        return r

#To check if the node is in the given range
def inrange(node, a, b):
    if node.data >= a and node.data <=b:
        return True
    return False

def isleaf(node):
    return node.left == None and node.right == None

def max(a, b):
    if a > b:
        return a
    return b

def largest_inrange_subtree(root, a, b):
    if root is None:
        return (0, True)
    if isleaf(root):
#for all the leaf nodes which fall in the required range, return 1 and True
        if inrange(root, a, b):
            return (1, True)
        else:
#for leaf nodes not  in range, return 0 and False. If a node returns false, it's ancestors become ineligible to be a part of the subtree
            return (0, False)
    else:
        if inrange(root, a, b):
            (lval, lgood) = largest_inrange_subtree(root.left, a, b)
            (rval, rgood) = largest_inrange_subtree(root.right, a, b)
#If both left and right child return true, then compute the size of subtree till then and pass it up the tree
            if lgood and rgood:
                return (lval+rval+1, True)
            else:
#If either left or right child return false, then compute the maximum size of subtree returned from either of its children and pass it up the tree
#This node however, wont participate in the process further
                return (max(lval, rval), False)
        else:
#If the current node is not in range, it wont participate in the process further, but will send the size of the maximum subtree computed from it's left and right children up the tree
            (lval, lgood) = largest_inrange_subtree(root.left, a, b)
            (rval, rgood) = largest_inrange_subtree(root.right, a, b)
            return (max(lval, rval), False)

#Input
r = make_tree((25, (19, (12, (4, None, None), None), (22, None, (23, None, None))), (37, (29, None, (30, None, None)), None)))

(val, good) = largest_inrange_subtree(r, 28, 39)
print(val)