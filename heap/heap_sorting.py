'''
Optimised way of selection sort
In selection sort, we take consider one min element and compare it with each in every iteration

Time complexity O(n log n)
'''

class maxheap:
    def __init__(self):
        self.A = []
    def max_heapify(self,parent,arr_length=None):
        if arr_length is None:
            arr_length = len(self.A)
        
        l_child = parent*2 +1
        r_child = parent*2 +2

        largest = parent

        if l_child < arr_length and self.A[l_child] > self.A[largest]:
            largest = l_child

        if r_child < arr_length and self.A[r_child] > self.A[largest]:
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
            self.max_heapify(j)
        
        for k in range(len(self.A)-1,0,-1):
            self.A[k],self.A[0] = self.A[0],self.A[k]
            self.max_heapify(0)


heap = maxheap()
arr = [9, 4, 3, 8, 10, 2, 5]
heap.build_max_heap(arr)
print(f"Hepify -- {heap.A}")