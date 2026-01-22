# repeated-dna-sequences

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
repeated_set = {}
k = 10

end_i = len(s)-k + 1

for i in range(0,end_i):
    seq = s[i:i+10]
    if seq in repeated_set.keys():
        repeated_set[seq] = repeated_set[seq] +1
    else:
        repeated_set[seq] = 1

final_list = []
for key,value in repeated_set.items():
    if value>1:
        final_list.append(key)

print(final_list)
# return final_list