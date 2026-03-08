
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

'''
# Lambda inside a function as a parameter
def apply_operation(x, y, operation):
    return operation(x, y)

result = apply_operation(5, 3, lambda a, b: a + b)

print(result)