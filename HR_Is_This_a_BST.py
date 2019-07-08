""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    def helper(root):
        if not root:
            return([])
        else:
            return(helper(root.left)+[root.data]+helper(root.right))
    new = helper(root)
    for i in range(len(new)-1):
        if(new[i+1]<=new[i]):
            return(False)
    return(True)
        
