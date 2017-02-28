#We need to add the smaller one of the child depths - except if that's zero, then add the larger one.

def minDepth(self, root):
    if not root: return 0
    d = map(self.minDepth, (root.left, root.right))
    return 1 + (min(d) or max(d))
    
#with DFS
def minDepth(self, root):
    return 0 if not root else self.dfs(root)
def dfs(self, root):
    return 1 + min([self.dfs(x) for x in (root.left,root.right) if x] or [0])
    
    
#With BFS
l, i = [root], 1
        while l and root and all(n.left or n.right for n in l):
            l, i = [kid for n in l for kid in [n.left, n.right] if kid], i+1
        return i if root else 0