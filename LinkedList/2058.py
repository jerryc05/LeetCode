from listnode import *


def f(head: ListNode) -> 'tuple[int,int]':
    l: 'list[int]' = []
    shortest = -1
    i = 2
    it = head
    while it.next.next is not None:
        if it.val != it.next.val and it.next.val != it.next.next.val:
            left = it.next.val < it.val
            right = it.next.val < it.next.next.val
            if left == right:
                l.append(i)
                if len(l) >= 2:
                    curr_short = l[-1] - l[-2]
                    if shortest == -1 or shortest > curr_short:
                        shortest = l[-1] - l[-2]
        i += 1
        it = it.next
    if shortest == -1:
        return -1, -1
    return shortest, l[-1] - l[0]


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> Sequence[int]:
        assert head
        return f(head)


pp(f(ListNode(3, ListNode(1))))


pp(
    f(
        ListNode(
            5, ListNode(3, ListNode(1, ListNode(2, ListNode(5, ListNode(1, ListNode(2))))))
        )
    )
)


pp(
    f(
        ListNode(
            1,
            ListNode(
                3,
                ListNode(
                    2,
                    ListNode(
                        2, ListNode(3, ListNode(2, ListNode(2, ListNode(2, ListNode(7)))))
                    ),
                ),
            ),
        )
    )
)
