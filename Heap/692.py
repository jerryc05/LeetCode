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

        def fixup(heap: 'list[str]', i: int):
            parent_i = (i - 1) // 2
            while i > 0 and (
                item_info[heap[i]].freq > item_info[heap[parent_i]].freq
                or (heap[i] > heap[parent_i])
            ):
                heap[i], heap[parent_i] = heap[parent_i], heap[i]
                item_info[heap[i]].idx, item_info[heap[parent_i]].idx = parent_i, i
                i = parent_i
                parent_i = (i - 1) // 2

        for word in words:
            if word not in item_info:
                item_info[word] = ItemInfo(1)
                if len(heap) < k:
                    item_info[word].idx = len(heap)
                    heap.append(word)
            else:
                item_info[word].freq += 1
                if item_info[word].idx >= 0:
                    fixup(heap, item_info[word].idx)
                else:
                    smallest_idx = min(
                        range(smallest_size - 1, len(heap)),
                        key=lambda x: item_info[heap[x]].freq,
                    )
                    if item_info[word].freq > item_info[heap[smallest_idx]].freq:
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
                if item_info[heap[i]].freq < item_info[heap[l]].freq or heap[i] < heap[l]:
                    heap[i], heap[l] = heap[l], heap[i]
                    i = l
                elif r < len(heap) and (
                    item_info[heap[i]].freq < item_info[heap[r]].freq or heap[i] < heap[r]
                ):
                    heap[i], heap[r] = heap[r], heap[i]
                    i = r
                else:
                    break

        sorted_arr: list[str] = []
        for _ in range(len(heap)):
            sorted_arr.append(heap[0])
            heap[0] = heap[-1]
            del heap[-1]
            fixdown(heap)

        return sorted_arr


print(
    Solution().topKFrequent(['i', 'love', 'leetcode', 'i', 'love', 'coding'], 2), ['i', 'love']
)
print(
    Solution().topKFrequent(
        ['the', 'day', 'is', 'sunny', 'the', 'the', 'the', 'sunny', 'is', 'is'], 4
    ),
    ['the', 'is', 'sunny', 'day'],
)
