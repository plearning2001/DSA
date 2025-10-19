def rec_func(num):
  print(f"before -- {num}")
  if num == 4:
    return
  num += 1
  rec_func(num)
  print(f"after -- {num}")

num =0
rec_func(num)