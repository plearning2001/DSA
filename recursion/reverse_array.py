# reverse an array
def rev_arr(a,l,r):
  print(f"array -- {a}")
  if l==r:
    return a

  a[r] = a[r] + a[l]
  a[l] = a[r] - a[l]
  a[r] = a[r] - a[l]



  l += 1
  r -= 1
  rev_arr(a,l,r)





a = [1,2,3,4,5]
print(rev_arr(a,0,len(a)-1))