class maxheap:
    def __init__(self):
        self.A = []

    def max(self):
        return self.arr[0] if self.arr else None
    
    def heapify_up(self):
        lenth = len(self.A) - 1
        while lenth > 0:
            parent = int((lenth-1)//2)

            if self.A[lenth] > self.A[parent]:
               self.A[lenth], self.A[parent] = self.A[parent], self.A[lenth] 
               lenth = parent
            else:
                break


    def heapify_down(self, i):
        n = len(self.A)
        while True:
            largest = i
            left, right = 2 * i + 1, 2 * i + 2
            if left < n and self.A[left] > self.A[largest]:
                largest = left
            if right < n and self.A[right] > self.A[largest]:
                largest = right
            if largest != i:
                self.A[i], self.A[largest] = self.A[largest], self.A[i]
                i = largest
            else:
                break

    def build_min_heap(self,arr,k):
        self.A = []
        for i in range(0,k):
            self.A.append(arr[i])
            self.heapify_up()
        print(self.A)

        for j in range(k,len(arr)):
            if self.A[0] > arr[j]:
                max_val = arr[0]
                self.A[0] = arr[j]
                self.heapify_down(0)                


heap = maxheap()
k = 3
arr = [5,4,1,2,3]
heap.build_min_heap(arr,k)
print(f"Hepify -- {heap.A}")