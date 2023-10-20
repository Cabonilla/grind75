class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.length = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key]
            del self.cache[key]
            self.cache[key] = val
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
            self.cache[key] = value
        elif self.capacity == self.length:
            del self.cache[next(iter(self.cache))]
            self.cache[key] = value
        else:
            self.cache[key] = value
            self.length += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)