class TreeNode:
    def __init__(self, value, children = []):
        self.value = value
        self.children = children
    
    def __str__ (self, level=0):
        ll = level
        ret = " " * level + str(self.value) + '\n'
        for child in self.children:
            ch = child.value
            ret += child.__str__(level+1)
        return ret
    
    def addChild(self,TreeNode):
        self.children.append(TreeNode)

cold = TreeNode("Cold",[]) 
hot = TreeNode("Hot",[])
tree = TreeNode("Drinks",[cold,hot])


print(tree)
