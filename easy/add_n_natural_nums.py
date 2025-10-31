
'''
We  can use simple for loop or recursion O(n)
But this solution will give result in constant time i.1 O(1)
'''

def add_all(n):
    return int((n*(n-1))/2)

if __name__ == "__main__":
    n = 487
    print(add_all(n))