data = ["h","e","l","l","o"]

def fun1(data,start,end):
    if start < end:
        data[start],data[end] = data[end],data[start]
        fun1(data,start+1,end-1)
    else:
        return



fun1(data,0,len(data)-1)