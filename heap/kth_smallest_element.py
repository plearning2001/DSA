class Heap:

    def __init__(self):
        self.arr = []

    def is_empty(self):
        return len(self.arr) == 0

    def max(self):
        return self.arr[0] if self.arr else None
    
    def heapify(self):
        length = len(self.arr)
        i = length

        while i > 0:
            parent = (i-1) // 2
            if arr[parent] < arr[i]:
                arr[parent],arr[i] = arr[i],arr[parent]

                i = parent
            else:
                break


    def insert(self,element):
        self.arr.append(element)
        self.heapify()

    def heapifyDown(self,m):
        while True:
            child_l = (m*2)+1
            child_r = (m*2)+2
            largest = m
            if child_l and self.arr[child_l] > self.arr[largest]:
                largest = child_l

            if child_r and self.arr[child_r] > self.arr[largest]:
                largest = child_r
            
            if largest != m:
                self.arr[largest], self.arr[m] = self.arr[m], self.arr[largest]
                i = largest
            else:
                break


def kminfunc(arr, k, num):
    heap = Heap()
    
    # Create first heap of k elements
    for i in range(k):
        heap.arr.append(i)
        heap.insert(i)

    # iterate over remaining elements
    for i in range(k, len(arr)-1):
        if heap.arr[0] < arr[i]:
            heap.arr[0], arr[i] = arr[i],heap.arr[0]
            heap.heapifyDown(0)

    return(heap.max() > num)



if __name__ == "__main__":
    arr = [6,5,4,3,7,1,9]
    k = 2
    num = 20
    result = kminfunc(arr, k, num)
    print(result)