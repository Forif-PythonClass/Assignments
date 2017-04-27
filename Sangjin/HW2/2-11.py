arr=[]
for i in range (0,50):
    if i==0 or i==1:
        arr.append(1)
    else:
        arr.append(arr[i-1]+arr[i-2])
print (arr)
