# here 10 represent base of input numbers x and y
def Fast_Multiply(x,y,n):
    print(f"{x} {y} {n}")
    if n == 1:
        return x * y
    else:
        m = n/2
        xh = x//10**m
        xl = x % (10**m)
        yh = y//10**m
        yl = y % (10**m)
        a = xh + xl
        b = yh + yl
        p = Fast_Multiply(xh, yh, m)
        q = Fast_Multiply(xl, yl, m)
        r = Fast_Multiply(a, b, m)
        return p*(10**n) + (r - q - p) * (10**(n/2)) + q 
print(Fast_Multiply(3456,8902,4))