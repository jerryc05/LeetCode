from listnode import * 

class ListNode2(ListNode):
    def __init__(self, n):
        super().__init__(n.val, n.next)

    def __lt__(self, o):
        return isinstance(o, ListNode) and self.val < o.val


from heapq import *


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        it = None
        heap = []

        for l in lists[:]:
            if l is None:
                lists.remove(l)
                continue
            heap.append(ListNode2(l))
            l = l.next
        heapify(heap)

        while heap:
            popp = heappop(heap)
            if head is None:
                head = popp
                it = head
            else:
                assert it
                it.next = popp
                it = it.next
            popp = popp.next
            if popp is not None:
                heappush(heap, ListNode2(popp))

        return head


print(
    Solution().mergeKLists(
        [
            ListNode(1, ListNode(4, ListNode(5))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(2, ListNode(6)),
        ]
    )
)


print(Solution().mergeKLists([]))


print(Solution().mergeKLists([None]))
