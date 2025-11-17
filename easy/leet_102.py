from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        output = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            
            local_list = []
            for i in range(level_size):
                node = queue.popleft()
                local_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:                    
                    queue.append(node.right)
            output.append(local_list)
        return output

