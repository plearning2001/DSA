data =  [9,2,3,6]
target = 6
# output - (2,3)

my_dict = dict(enumerate(data))
print(f"my_dict -- {my_dict}")

for key,val in my_dict.items():
    print(f"key - {key}, val - {val}")
    if target%val == 0 and (target/val) in my_dict.values():
        print((val,int(target/val)))
        break
    else:
        print("Not found")