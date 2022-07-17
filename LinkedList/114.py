from listnode import *


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return
        l: 'list[TreeNode]' = []
        stack = [root]
        while stack:
            it = stack.pop()
            if it.right is not None:
                stack.append(it.right)
            if it.left is not None:
                stack.append(it.left)
            it.left = None
            l.append(it)
        assert l[0] == root
        for i in range(len(l) - 1):
            l[i].right = l[i + 1]
        assert l[-1].right == None


f = Solution().flatten

l = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
f(l)
pp(l)
