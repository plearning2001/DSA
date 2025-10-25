class maxheap:
    def __init__(self):
        self.A = []
    def max_heapify(self,parent):
        
        l_child = parent*2 +1
        r_child = parent*2 +2

        largest = parent

        if l_child < len(self.A) and self.A[l_child] > self.A[largest]:
            largest = l_child

        if r_child < len(self.A) and self.A[r_child] > self.A[largest]:
            largest = r_child
        
        if parent != largest:
            self.A[parent],self.A[largest] = self.A[largest], self.A[parent]
            
            # Againt heapify for largest element
            self.max_heapify(largest)


    def build_max_heap(self,arr):
        self.A = []
        for i in arr:
            self.A.append(i)
        
        mid_parent = int(len(self.A)//2-1)
        for j in range(mid_parent,-1,-1):
            self.max_heapify(mid_parent)


heap = maxheap()
arr = [1,2,3,4,5,6]
heap.build_max_heap(arr)
print(f"Hepify -- {heap.A}")