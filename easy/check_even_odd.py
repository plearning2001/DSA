def check_even_odd(num):
    if num%2 ==1:
        return f"{num} is odd"
    else:
        return f"{num} is even"

if __name__ == "__main__":
    num = 198398132
    print(check_even_odd(num))