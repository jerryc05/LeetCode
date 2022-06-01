from listnode import *
from collections import defaultdict


class AllOne:
    def __init__(self):
        self.key2count: 'dict[str,int]' = defaultdict(int)
        self.count2key: 'dict[int,set[str]]' = defaultdict(set)

    def inc(self, key: str) -> None:
        try:
            self.count2key[self.key2count[key]].remove(key)
        except:
            ...
        self.key2count[key] += 1
        self.count2key[self.key2count[key]].add(key)

    def dec(self, key: str) -> None:
        self.count2key[self.key2count[key]].remove(key)
        if self.key2count[key] == 1:
            self.key2count.pop(key)
        else:
            self.key2count[key] -= 1
            self.count2key[self.key2count[key]].add(key)

    def getMaxKey(self) -> str:


    def getMinKey(self) -> str:
        ...


allOne = AllOne()
allOne.inc("hello")
allOne.inc("hello")
assert allOne.getMaxKey() == "hello"
assert allOne.getMinKey() == "hello"
allOne.inc("leet")
assert allOne.getMaxKey() == "hello"
assert allOne.getMinKey() == "leet"
