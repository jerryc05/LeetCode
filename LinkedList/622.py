class MyCircularQueue:
    def __init__(self, k: int):
        self.i = 0
        self.size = 0
        self.capacity = k
        self.l = [-1 for _ in range(self.capacity)]

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.l[(self.i + self.size) % self.capacity] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size >= 1:
            self.inc()
            self.size -= 1
            return True
        return False

    def Front(self) -> int:
        return self.l[self.i] if self.size else -1

    def Rear(self) -> int:
        return self.l[(self.i + self.size - 1) % self.capacity] if self.size else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

    def dec(self):
        self.i = (self.i + self.capacity - 1) % self.capacity

    def inc(self):
        self.i = (self.i + 1) % self.capacity
