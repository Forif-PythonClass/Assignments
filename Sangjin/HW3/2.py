def print_even_number(list):
    result=[]
    for i in range (0,len(list)):
        if (list[i]%2==0):
            result.append(list[i])
    return result;

samplelist=[1,2,3,4,5,6,7,8,9]
print(print_even_number(samplelist))
