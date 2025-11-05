'''
We  can use simple for loop or recursion O(n)
But this solution will give result in constant time i.1 O(1)
'''

def add_all_sq(n):
    value = (n*(n+1) * ((2*n) + 1)) /6
    return int(value)

if __name__ == "__main__":
    n = 1
    print(f" Sum of squares is - {add_all_sq(n)}")