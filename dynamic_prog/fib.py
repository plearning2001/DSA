from datetime import datetime
def fibrec(n):
    if n <= 1:
        return n 
    return fibrec(n - 1) + fibrec(n - 2)

memo ={}
def fib(n):
    if n <= 1:
        memo[n] = n
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]


x = datetime.now()
print(fibrec(25))
y = datetime.now()
print(f"time -- {y-x}")

print(fib(25))
z = datetime.now()
print(f"time -- {z-y}")


