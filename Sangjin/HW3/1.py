def times(list):
    result = 1;
    for i in range (0,len(list)):
        result=result*list[i]
    return result

samplelist=[8,2,3,-1,7]
print(times(samplelist))
