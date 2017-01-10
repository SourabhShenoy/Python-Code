# Python program to find the deepest left leaf in a given
# Binary tree
 
# A binary tree node
class Node:
     
    # Constructor to create a new node
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None
 
# A utility function to find deepest leaf node.
# lvl:  level of current node.
# maxlvl: pointer to the deepest left leaf node found so far
# isLeft: A bool indicate that this node is left child
# of its parent
# resPtr: Pointer to the result
def deepestLeftLeafUtil(root, lvl, maxlvl, isLeft):
     
    # Base CAse
    if root is None:
        return
 
    # Update result if this node is left leaf and its 
    # level is more than the max level of the current result
    if(isLeft is True):
        if (root.left == None and root.right == None):
            if lvl > maxlvl[0] : 
                deepestLeftLeafUtil.resPtr = root 
                maxlvl[0] = lvl 
                return
 
    # Recur for left and right subtrees
    deepestLeftLeafUtil(root.left, lvl+1, maxlvl, True)
    deepestLeftLeafUtil(root.right, lvl+1, maxlvl, False)
 
# A wrapper for left and right subtree
def deepestLeftLeaf(root):
    maxlvl = [0]
    deepestLeftLeafUtil.resPtr = None
    deepestLeftLeafUtil(root, 0, maxlvl, False)
    return deepestLeftLeafUtil.resPtr
 
 
# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.right = Node(7)
root.right.right.right = Node(8)
root.right.left.right.left = Node(9)
root.right.right.right.right= Node(10)
 
result = deepestLeftLeaf(root) 
 
if result is None:
    print "There is not left leaf in the given tree"
else:
    print "The deepst left child is", result.val