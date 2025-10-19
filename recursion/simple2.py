#Print Name five times

def print_name(n,i):
  if i == n:
    print("Name")
    return
  elif i>n:
    return
  print("Name")

  print_name(n,i+1)

n = 2
print_name(n,1)