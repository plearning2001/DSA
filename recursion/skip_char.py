
def skip_str(ip_str,new_str):
    if not ip_str:
        return new_str

    char = ip_str[0]
    if char == "a":
        
        return skip_str(ip_str[1:],new_str)
    else:
        new_str = new_str + ip_str[0]
        return skip_str(ip_str[1:],new_str)

    


input_str = "data"
#Remove a from input
new_str = ''
print(skip_str(input_str,new_str))