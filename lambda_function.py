
'''
def add(a, b):
    return a + b

# print(add(3, 5))

print("Lambda version")
add = lambda a, b: a + b
print(add(3, 5))


# Syntax - lambda arg1,arg2 : expression

square = lambda x: x * x
print(square(4))

# Lambda inside a function as a parameter
def apply_operation(x, y, operation):
    return operation(x, y)

result = apply_operation(5, 3, lambda a, b: a + b)

print(result)

'''


# 1. Import the reduce function
from functools import reduce

# 2. Define a standard function that takes two arguments
def prod(x, y):
  """Returns the product of two numbers."""
  return x + y

# 3. Create a list of numbers
list1 = [1, 2, 3, 4]

# 4. Use reduce with the named function
product_result = reduce(prod, list1)

# 5. Print the result
print("Sum:", product_result)
