from typing import *
from pprint import pp


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode|None" = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        s = str(self.val)
        if self.next is not None:
            s += f"->{repr(self.next)}"
        return s
