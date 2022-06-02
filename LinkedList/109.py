from listnode import *


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
