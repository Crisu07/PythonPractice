import sys #able to use the getsizeof function

n = 18

data = []
a_size1 = sys.getsizeof(data)

for k in range(n):
    a=len(data) #number of elements within 
    a_size2 = sys.getsizeof(data) #size in bytes

    if a_size2 > a_size1: 
        print("Length:", a-1, "Size in bytes:", a_size1)
    a_size1 = a_size2
    data.append(None)