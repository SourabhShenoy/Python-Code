class Solution:
# @param root, a tree node
# @return nothing, do it in place
prev = None
def flatten(self, root):
    if not root:
        return
    self.prev = root
    self.flatten(root.left)

    temp = root.right
    root.right, root.left = root.left, None
    self.prev.right = temp

    self.flatten(temp)


         *
       /
      n
   /     \
 left   right
  \ 
   *
    *
     \
      p
      
The idea is very simple. Suppose n is the current visiting node, and p is the previous node of preorder traversal to n.right.

We just need to do the inorder replacement:

n.left -> NULL

n.right - > n.left

p->right -> n.right



class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        '''
        1. flatten left subtree
        2. find left subtree's tail
        3. set root's left to None, root's right to root'left, tail's right to root.right
        4. flatten the original right subtree
        '''
        # escape condition
        if not root:
            return
        right = root.right
        if root.left:
            # flatten left subtree
            self.flatten(root.left)
            # find the tail of left subtree
            tail = root.left
            while tail.right:
                tail = tail.right
            # left <-- None, right <-- left, tail's right <- right
            root.left, root.right, tail.right = None, root.left, right
        # flatten right subtree
        self.flatten(right)
        


