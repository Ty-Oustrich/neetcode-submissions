# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #go to the bottom and then pass the height up

        def dfs(root):
            if not root: return [True, 0] #base case

            left, right = dfs(root.left), dfs(root.right) #traversal, catching bool and height
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1) #bool
            return [balanced, 1 + max(left[1], right[1])] #return list of bool and height
        return dfs(root)[0]