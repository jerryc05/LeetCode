from listnode import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        it = head
        for _ in range(k - 1):
            if it.next is not None:
                it = it.next
            else:
                return head
        it2 = head.next
        head.next = self.reverseKGroup(it.next, k)
        for _ in range(k - 1):
            assert it2
            it3 = it2.next
            it2.next = head
            head = it2
            it2 = it3

        return head


print(
    Solution().reverseKGroup(
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2
    )
)


print(
    Solution().reverseKGroup(
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 3
    )
)
