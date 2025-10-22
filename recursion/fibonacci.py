#fibonacci
#multiple recursion calls
#1,1,2,3,5,8,13,21,34,55,89,144

def fibo(n):
  if n<=1:
    return n
  else:
    last = fibo(n-1)
    second_last = fibo(n-2)
    return last + second_last

n = 6
print(fibo(n))