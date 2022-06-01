from listnode import *


def f(head: ListNode) -> int:
    n = 0
    while head is not None:
        n = 2 * n + head.val
        head = head.next
    return n


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        return f(head)


pp(f(ListNode(1, ListNode(0, ListNode(1)))))


pp(f(ListNode(0)))
