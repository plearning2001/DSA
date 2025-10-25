
'''
Here we will not sort the entire array/heap for each itteration
Instead we will create heap of k items and n times we will sort only k items
so N X logK complexity
'''


# ---------------- HEAP IMPLEMENTATION ---------------- #
class MaxHeap:

    def __init__(self):
        self.arr = []

    def is_empty(self):
        return len(self.arr) == 0

    def max(self):
        return self.arr[0] if self.arr else None

    def heapify_down(self, i):
        n = len(self.arr)
        while True:
            largest = i
            left, right = 2 * i + 1, 2 * i + 2
            if left < n and self.arr[left] > self.arr[largest]:
                largest = left
            if right < n and self.arr[right] > self.arr[largest]:
                largest = right
            if largest != i:
                self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
                i = largest
            else:
                break

    def heapify_up(self):
        i = len(self.arr) - 1
        print(self.arr)
        while i > 0:
            parent = (i - 1) // 2
            if self.arr[i] > self.arr[parent]:
                print(self.arr[i], self.arr[parent])
                self.arr[i], self.arr[parent] = self.arr[parent], self.arr[i]
                i = parent
            else:
                break

    def insert(self, x):
        self.arr.append(x)
        self.heapify_up()

    def replace_max(self, x):
        if not self.arr:
            return None
        max_val = self.arr[0]
        self.arr[0] = x
        self.heapify_down(0)
        return max_val


def kmin_greater_than(arr, k, num):
    """Return True if the kth smallest element is >= num."""
    if k > len(arr):
        return False

    heap = MaxHeap()
    for i in range(k):
        heap.insert(arr[i])

    for i in range(k, len(arr)):
        if arr[i] < heap.max():
            heap.replace_max(arr[i])

    return heap.max() >= num




# ---------------- MAIN MENU ---------------- #
if __name__ == "__main__":

      arr = [6,5,4,3,7,1,9]
      k = 3
      num = 40
      result = kmin_greater_than(arr, k, num)
      if result:
          print("True")
      else:
          print("False")
