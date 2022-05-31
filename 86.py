from listnode import *


def f(head: ListNode, x: int):
    left = ListNode()
    left_i = left
    right = ListNode()
    right_i = right

    i = head
    while i is not None:
        if i.val < x:
            left_i.next = i
            left_i = left_i.next
        else:
            right_i.next = i
            right_i = right_i.next
        i = i.next
    left_i.next = right.next
    right_i.next = None
    return left.next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return head
        return f(head, x)


pp(f(ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2)))))), 3))


pp(f(ListNode(2, ListNode(1)), 2))


pp(
    f(
        ListNode(
            1, ListNode(4, ListNode(3, ListNode(0, ListNode(2, ListNode(5, ListNode(2))))))
        ),
        3,
    )
)
# [1,0,2,2,4,3,5]
