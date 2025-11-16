class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for i in range(self.size)]
    def hash(self,key):
        return key % self.size
    

        

    def add(self, key: int) -> None:
        h = self.hash(key)
        bucket = self.buckets[h]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        h = self.hash(key)
        bucket = self.buckets[h]
        if key in bucket:
            bucket.remove(key)        
        

    def contains(self, key: int) -> bool:
        h = self.hash(key)
        bucket = self.buckets[h]
        return key in bucket



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)