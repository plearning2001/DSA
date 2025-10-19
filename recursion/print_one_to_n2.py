#Print reverse
def print_one_to_n(i,n):
  if i ==n:
    print(i)
    return
  # print(i)

  print_one_to_n(i+1,n)
  print(i)

print_one_to_n(1,5)