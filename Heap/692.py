class ItemInfo:
    def __init__(self, freq: int, idx: int = -1):
        self.freq = freq
        self.idx = idx

    def __repr__(self) -> str:
        return f'ItemInfo({self.freq} @ {self.idx})'


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        item_info: 'dict[str,ItemInfo]' = {}
        heap: 'list[str]' = []
        smallest_size = (k + 1) // 2

        def cmp(l: str, r: str):
            l_freq, r_freq = item_info[l].freq, item_info[r].freq
            return l_freq > r_freq or (l_freq == r_freq and l < r)

        def fixup(heap: 'list[str]', i: int):
            parent_i = (i - 1) // 2
            while i > 0 and cmp(heap[i], heap[parent_i]):
                item_info[heap[i]].idx, item_info[heap[parent_i]].idx = parent_i, i
                heap[i], heap[parent_i] = heap[parent_i], heap[i]
                i = parent_i
                parent_i = (i - 1) // 2

        for word in words:
            try_insert = False
            if word not in item_info:
                item_info[word] = ItemInfo(1)
                if len(heap) < k:
                    item_info[word].idx = len(heap)
                    heap.append(word)
                    fixup(heap, len(heap) - 1)
                else:
                    try_insert = True
            else:
                item_info[word].freq += 1
                if item_info[word].idx >= 0:
                    fixup(heap, item_info[word].idx)
                else:
                    try_insert = True
            if try_insert:
                smallest_idx = smallest_size - 1
                for i in range(smallest_size, len(heap)):
                    if not cmp(heap[i], heap[smallest_idx]):
                        smallest_idx = i
                if cmp(word, heap[smallest_idx]):
                    item_info[heap[smallest_idx]].idx = -1
                    heap[smallest_idx] = word
                    item_info[heap[smallest_idx]].idx = smallest_idx
                    fixup(heap, smallest_idx)

        def fixdown(heap: 'list[str]'):
            i = 0
            while ...:
                l = i * 2 + 1
                if l >= len(heap):
                    break
                r = l + 1
                if r < len(heap) and cmp(heap[r], heap[l]):
                    l = r
                # now [l] is the "smaller" child
                if not cmp(heap[i], heap[l]):
                    heap[i], heap[l] = heap[l], heap[i]
                    i = l
                else:
                    break

        sorted_arr: list[str] = []
        for _ in range(len(heap)):
            sorted_arr.append(heap[0])
            heap[0] = heap[-1]
            del heap[-1]
            fixdown(heap)

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
