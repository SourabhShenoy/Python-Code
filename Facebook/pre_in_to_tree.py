#Recursive

def buildTree(self, preorder, inorder):
    if inorder:
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        root.left = self.buildTree(preorder, inorder[0:ind])
        root.right = self.buildTree(preorder, inorder[ind+1:])
        return root
        
'''
Preorder: [root, left nodes, right nodes],
Inorder: [left nodes, root, right nodes].
With preorder.pop(0) executed for each
node.left = self.buildTree(preorder[1:l_len+1], inorder[0:l_len]) and its recursive steps, we can guarantee that left nodes are all popped out in the preorder list and it is ready for
root.right = self.buildTree(preorder, inorder[ind+1:]).'''


#iterative

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        stack=[]
        root=TreeNode(0)
        if len(preorder)==0:
            return None
        root=TreeNode(preorder[0])
        stack.append(root)
        index=0
        for i in range(1,len(preorder)+1):
            cur=stack[-1]
            if(stack[-1].val!=inorder[index]):
                cur.left=TreeNode(preorder[i])
                stack.append(cur.left)
            else:
                while(len(stack)!=0 and stack[-1].val==inorder[index]):
                    cur=stack[-1]
                    stack.pop()
                    index+=1
                if(index<len(inorder)):
                    cur.right=TreeNode(preorder[i])
                    stack.append(cur.right)
            i+=1
        return root