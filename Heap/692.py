class ItemInfo:
    def __init__(self, freq: int, idx: int = -1):
        self.freq = freq
        self.idx = idx

    def __repr__(self) -> str:
        return f'ItemInfo({self.freq} @ {self.idx})'


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        item_info: 'dict[str,ItemInfo]' = {}
        min_heap: 'list[str]' = []

        def cmp(l: str, r: str):
            l_freq, r_freq = item_info[l].freq, item_info[r].freq
            return l_freq < r_freq or (l_freq == r_freq and l > r)

        def fixup(i: int):
            parent_i = (i - 1) // 2
            while i > 0 and cmp(min_heap[i], min_heap[parent_i]):
                item_info[min_heap[i]].idx, item_info[min_heap[parent_i]].idx = parent_i, i
                min_heap[i], min_heap[parent_i] = min_heap[parent_i], min_heap[i]
                i = parent_i
                parent_i = (i - 1) // 2

        def fixdown(i: int):
            while ...:
                l = i * 2 + 1
                if l >= len(min_heap):
                    break
                r = l + 1
                if r < len(min_heap) and cmp(min_heap[r], min_heap[l]):
                    l = r
                # now [l] is the "smaller" child
                if cmp(min_heap[l], min_heap[i]):
                    item_info[min_heap[i]].idx, item_info[min_heap[l]].idx = l, i
                    min_heap[i], min_heap[l] = min_heap[l], min_heap[i]
                    i = l
                else:
                    break

        for word in words:
            try_insert = False
            if word not in item_info:
                item_info[word] = ItemInfo(1)
                if len(min_heap) < k:
                    item_info[word].idx = len(min_heap)
                    min_heap.append(word)
                    fixup(len(min_heap) - 1)
                else:
                    try_insert = True
            else:
                item_info[word].freq += 1
                if item_info[word].idx >= 0:
                    fixdown(item_info[word].idx)
                else:
                    try_insert = True
            if try_insert:
                if not cmp(word, min_heap[0]):
                    item_info[min_heap[0]].idx = -1
                    min_heap[0] = word
                    item_info[min_heap[0]].idx = 0
                    fixdown(0)

        sorted_arr: list[str] = [''] * len(min_heap)
        for j in range(len(sorted_arr)):
            i = len(sorted_arr) - 1 - j
            sorted_arr[i] = min_heap[0]
            min_heap[0] = min_heap[-1]
            del min_heap[-1]
            fixdown(0)

        return sorted_arr


def test_1():
    assert Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2) == [
        "i",
        "love",
    ]

def test_2():
    assert Solution().topKFrequent(
        ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4
    ) == ["the", "is", "sunny", "day"]

def test_3():
    assert Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 3) == [
        "i",
        "love",
        "coding",
    ]


def test_4():
    assert Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 1) == [
        "i"
    ]


def test_5():
    assert Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 5) == [
        "i",
        "love",
        "coding",
        "leetcode",
    ]


def test_6():
    assert Solution().topKFrequent(['aaa', 'aa', 'a'], 2) == ['a', 'aa']


def test_7():
    assert Solution().topKFrequent(['aaa', 'aa', 'a'], 3) == ['a', 'aa', 'aaa']
