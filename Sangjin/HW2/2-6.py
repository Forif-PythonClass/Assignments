dup_list = [10,20,30,20,10,50,60,40,80,50,40]
dup_list_ = [10,20,30,20,10,50,60,40,80,50,40]
for i in range (0,10):
    for j in range (i+1,11):
        if (dup_list[i] == dup_list[j]):
            dup_list_.remove(dup_list[i])
            dup_list_.remove (dup_list[j])
print (dup_list_)
