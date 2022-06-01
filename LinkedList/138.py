from listnode import *


class Node:
    def __init__(self, x: int, next: 'Node|None' = None, random: 'Node|None' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        orig2new: 'dict[Node,Node]' = {}
        i = head
        while i is not None:
            orig2new[i] = Node(i.val)
            i = i.next
        for k, v in orig2new.items():
            if k.next is not None:
                v.next = orig2new[k.next]
            if k.random is not None:
                v.random = orig2new[k.random]
        return orig2new[head]
