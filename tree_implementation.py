


# Binary Tree
#               5
#             /   \
#           3      7
#          / \         
#         2   4


# Insertion
# Traversal 🚶‍♂️🚶
#   - In-order traversal
#       🎯 Traverse Left (3,2)
#       🎯 Visit Root(5)
#       🎯 Traverse Right (4,7)
#           🏁 2,3,4,5,7

#   - Pre-order traversal
#       🎯 Visit Root(5)
#       🎯 Traverse Left(3,2)
#       🎯 Traverse Right (4,7)
#           🏁 5,3,2,4,7

#   - Post-order traversal
#       🎯 Traverse Left (3,2)
#       🎯 Traverse Right (4,7)
#       🎯 Visit Root(5)
#           🏁 2,4,3,7,5

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val  = key

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        self.root = self._insert(self.root, key) 
    
    def _insert(self, root, key):
        if root is None:
            return TreeNode(key)
        else:
            if key < root.val:
                root.left = self._insert(root.left,key)
            else:
                root.right = self._insert(root.right,key)
        return root
    
    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result
    
    def _inorder_traversal(self, root, result):
        if root:
            self._inorder_traversal(root.left, result)
            result.append(root.val)
            self._inorder_traversal(root.right, result)
    
    def preorder_traversal(self):
        result = []
        self._preorder_traversal(self.root, result)
        return result
    
    def _preorder_traversal(self, root, result):
        if root:
            result.append(root.val)
            self._preorder_traversal(root.left, result)
            self._preorder_traversal(root.right, result)
    
    def postorder_traversal(self):
        result = []
        self._postorder_traversal(self.root, result)
        return result
    
    def _postorder_traversal(self, root, result):
        if root:
            self._postorder_traversal(root.left, result)
            self._postorder_traversal(root.right, result)
            result.append(root.val)
            
    
    
# Usage
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)

# Make some traversal 🚶‍♂️🚶
inorder_tr =tree.inorder_traversal()
preorder_tr = tree.preorder_traversal()
postorder_tr = tree.postorder_traversal()

# Display the results
print("In-order Traversal", inorder_tr)
print("Pre-order Traversal",preorder_tr)
print("Post-order Traversal",postorder_tr)



# APPLICATIONS OF TREES
    # File Systems
    # Organization Chartsz
    # Database Indexing
    # Network Routing Algorithms - routing decision 
    # HTML DOM(Document Object Model) <div> <p> </p> <div>
    # Compiler Design AST Abstract Syntax Tree
    # Game Development
    # AI
    # XML, JSON parsing
    # Cryptography
    # Search Engines
