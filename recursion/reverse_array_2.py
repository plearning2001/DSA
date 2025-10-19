def swap_half(a,i,n):
  if i >= n//2:
    return a
  
  a[i],a[n-i-1] = a[n-i-1],a[i]

  return swap_half(a,i+1,n)

a = [1,2,3,4,5]
print(swap_half(a,0,len(a)))