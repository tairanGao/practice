import heapq


class CacheNode(object):
    def __init__(self, key, val, use):
        self.use = use
        self.val = val
        self.key = key

    def __lt__(self, other):
        return self.use < other.use

    def update_use(self, use):
        self.use = use

    def update_val(self, val):
        self.val = val



class LRUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        # do intialization if necessary
        self.cache_dict = {}
        self.capacity = capacity
        self.count = 0
        self.use = 0
        self.heap = []

    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        # write your code here
        if key in self.cache_dict:
            node = self.cache_dict[key]
            self.use += 1
            node.update_use(self.use)

            return node.val
        return -1

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def set(self, key, value):
        # write your code here
        self.use += 1
        if key in self.cache_dict:
            node = self.cache_dict[key]
            node.update_use(self.use)
            node.update_val(value)
        else:
            node = CacheNode(key, value, self.use)
            self.heap.append(node)
            if self.count >= self.capacity:
                heapq.heapify(self.heap)
                deleted_node = heapq.heappop(self.heap)
                self.cache_dict.pop(deleted_node.key, None)
                self.count -= 1
            self.cache_dict[key] = node
            self.count += 1


a = LRUCache(10)
a.set(7, 28)
a.set(7, 1)
a.set(8, 15)
a.get(6)
a.set(10, 27)
a.set(8, 10)
a.get(8)
a.set(6, 29)
a.set(1, 9)
a.get(6)
a.set(10, 7)
a.get(1)
a.get(2)
a.get(13)
a.set(8, 30)
a.set(1, 5)
a.get(1)
a.set(13, 2)
a.get(12)