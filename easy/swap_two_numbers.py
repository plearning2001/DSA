def swap_function(a,b):
    a = a + b
    b = a - b
    a = a - b

    return a,b

if __name__ == "__main__":
    a = 4
    b = 6
    print(f" Before swapping --------- a : {a}, b : {b}")
    a,b = swap_function(a,b)
    print(f" After swapping swapping - a : {a}, b : {b}")