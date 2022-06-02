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
