input_data = [3,-1,2,-4]

i = 0
j = len(input_data)-1

while i<j:
    if input_data[i]<0:
        i += 1
    elif input_data[j] >= 0:
        j -= 1
    else:
        input_data[i],input_data[j] = input_data[j],input_data[i]
        i += 1
        j -= 1
        
print(f"output_data -- {input_data}")
