def MOM7POS(arr):
    if len(arr) <= 7:
        arr.sort()
        if len(arr) %2 == 0:
            return (arr[int((len(arr)+1)//2)] + arr[int((len(arr))//2)])//2
        else:
            return arr[int((len(arr)-1)//2)]

    
    # new_arr = arr[:7]
    # print(new_arr)
    # new_arr.sort()

    med_arr = []
    count = 0
    # arr.sort()
    for i in range(0,len(arr),7):
        new_arr = arr[i:i+7]
        new_arr.sort()
        print(new_arr)
        if len(new_arr) %2 == 0:
            med_arr.append((new_arr[int((len(new_arr)+1)//2)] + new_arr[int((len(new_arr))//2)])//2)
        else:
            med_arr.append(new_arr[int((len(new_arr)-1)//2)])
        print(med_arr)



    print(f"medians -- {med_arr}")
    return(MOM7POS(med_arr))


if __name__ == "__main__":
    arr = [44,9,31,12,15,98,48,45,13,75,23,6,35,74]
    print(MOM7POS(arr))