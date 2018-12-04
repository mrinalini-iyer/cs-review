class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
def inorderTraversal(root):
    print("Inside inorder traversal function")
    inorder = []
    inorder_stack = []
    
    while(root is not None or inorder_stack):
        while(root is not None):
            inorder_stack.append(root)
            root = root.left
    
        top = inorder_stack.pop(-1)
    
        inorder.append(top.val)
    
        root = top.right
        
    return inorder


def inorderTraversalRecursion(root, inorder):
    #print("Inside resursion inorder")
    

    if root is None:
        return
    
    inorderTraversalRecursion(root.left, inorder)
    inorder.append(root.val)
    inorderTraversalRecursion(root.right, inorder)
    
    return


def testFunction():
    # Create a tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    # Traverse the tree inorder and orint the result
    #res = inorderTraversal(root)
    
    inorder = []
    
    inorderTraversalRecursion(root, inorder)
    
    for ele in inorder:
        print("%d," % ele)
        
testFunction()
    
