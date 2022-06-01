from listnode import *


class TreeNode:
    def __init__(
        self, val: int = 0, left: 'TreeNode|None' = None, right: 'TreeNode|None' = None
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.val)
        return f'({self.val},{repr(self.left)},{repr(self.right)})'


def f(l: list[int]) -> Optional[TreeNode]:
    if not l:
        return None
    return TreeNode(l[len(l) // 2], f(l[: len(l) // 2]), f(l[len(l) // 2 + 1 :]))


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)

        i = head
        l: 'list[int]' = []
        while i is not None:
            l.append(i.val)
            i = i.next

        return TreeNode(l[len(l) // 2], f(l[: len(l) // 2]), f(l[len(l) // 2 + 1 :]))


pp(
    Solution().sortedListToBST(
        ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))
    )
)
