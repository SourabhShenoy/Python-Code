def maxDepth(self, root):
    return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0
    


    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        leftChildHeight=self.maxDepth(root.left)
        rightChildHeight=self.maxDepth(root.right)
        return max(leftChildHeight, rightChildHeight)+1
        
        

#stack for level order

 def maxDepth(self, root):     
     if not root:
         return 0
 
     tstack,h = [root],0
     
     #count number of levels
     while tstack:
         nextlevel = []
         while tstack:
             top = tstack.pop()
             if top.left:
                 nextlevel.append(top.left)
             if top.right:
                 nextlevel.append(top.right)
         tstack = nextlevel
         h+=1
     return h
     
#queue for level order

 def maxDepth(self, root):     
     if not root:
         return 0
     
     tqueue, h = collections.deque(),0
     tqueue.append(root)
     while tqueue:
         nextlevel = collections.deque()
         while tqueue:
             front = tqueue.popleft()
             if front.left:
                 nextlevel.append(front.left)
             if front.right:
                 nextlevel.append(front.right)
         tqueue = nextlevel
         h += 1
     return h