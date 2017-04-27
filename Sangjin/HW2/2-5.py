a=['abc','xyz','aba','1221']
index=0;
for i in range (0,4):
    if a[i][0]==a[i][-1]:
        index=index+1
print (index)
