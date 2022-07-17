from listnode import *


def f(head: ListNode, k: int, size: int):
    it = head
    for _ in range(size - 1 - k):
        it = it.next
        assert it
    new_head = it.next
    it.next = None
    assert new_head
    it = new_head
    while it.next is not None:
        it = it.next
    it.next = head
    return new_head


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        it = head
        size = 0
        while it is not None:
            size += 1
            it = it.next
        return f(head, k % size, size) if k % size != 0 else head


print(
    Solution().rotateRight(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
)


print(Solution().rotateRight(ListNode(0, ListNode(1, ListNode(2))), 4))
