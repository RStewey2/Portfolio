#Binary Search Tree Example
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class Tree:
    def __init__(self):
        self.root = None

    def build_tree(self,arr):
        arr_clean = []
        for k in arr:
            if k not in arr_clean:
                arr_clean.append(k)
                
        for i in arr_clean:
            if self.root == None:
                self.root = Node(i)
            else:
                self._insert(i, self.root)

    def find(self, value):
        if self.root != None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, node):
        if value == node.data:
            return node
        elif (value < node.data and node.left != None):
            return self._find(value, node.left)
        elif (value > node.data and node.right != None):
            return self._find(value, node.right)

    def insert(self, value):
        if self.find(value).data != value:
            if self.root == None:
                    self.root = Node(value)
            else:
                self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.data:
            if node.left != None:
                self._insert(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right != None:
                self._insert(value, node.right)
            else:
                node.right = Node(value)

    def printTree(self):
        if self.root != None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node != None:
            self._printTree(node.left)
            print(node.data)
            self._printTree(node.right)

    def delete_Node(self, root, key):
      
        if not root: 
            return root
        if root.data > key: 
            root.left = self.delete_Node(root.left, key)
        elif root.data < key: 
            root.right= self.delete_Node(root.right, key)
        else: 
            if not root.right:
                return root.left	
            if not root.left:
                return root.right
            temp_val = root.right
            mini_val = temp_val.val
            while temp_val.left:
                temp_val = temp_val.left
                mini_val = temp_val.val
            root.right = self.deleteNode(root.right,root.data)
        return root

array = [1, 7, 4, 23, 8, 9, 4, 3, 5, 7, 9, 67, 6345, 324]
tree = Tree()
tree.build_tree(array)
print('\ntree:')
tree.printTree()
tree.insert(4)
print('\ntree after insert (4):')
tree.printTree()
tree.delete_Node(tree.root, 5)
print('\ntree after delete (5):')
tree.printTree()
