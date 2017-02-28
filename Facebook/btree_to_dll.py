def toDLL(self, parent=None):
      """
        Implement rewrite rules:
          1) The rightmost node of a node's left subtree (rml) becomes the node's 
             prev (left).
          2) The leftmost node of a node's right subtree (lmr) becomes the node's
             next (right).
      """
      lm, rm = self, self    # when None left or right, lm, rm is self
      lmr, rml = None, None  # when None left or right, lmr, rml is None
 
      if self.left: lm, rml = self.left.toDLL(self)
      if self.right: lmr, rm = self.right.toDLL(self)
 
      self.left, self.right = rml, lmr  # the rule above
      if rml: rml.right = self          # back pointers
      if lmr: lmr.left = self
      if not parent:  # root: join up first and last elements
        lm.left = rm
        rm.right = lm
      return lm, rm