# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        suma3 = 0
        currentNo = ""
    
        def traverse(node,currentNo):
            nonlocal suma3
            
            currentNo += str(node.val)

            if not node.left and not node.right:
                suma3 += int(currentNo,2)
                return suma3

            if node.left:
                traverse(node.left,currentNo)
            if node.right:
                traverse(node.right,currentNo)
                
            
        traverse(root,currentNo)

        return suma3
