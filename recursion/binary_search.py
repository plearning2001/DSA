def f(a,L,R,T):
    M = L + (R-L)//2
    print(f"Middle -- {M}")
    if T == a[M]:
        return M
    else:
        if T < a[M]:
            R = M-1
            return f(a,L,R,T)
        else:
            L = M+1
            return f(a,L,R,T)            


a = [1,3,4,6,7,9,10]
T = 10
print(f(a,0,len(a)-1,T))