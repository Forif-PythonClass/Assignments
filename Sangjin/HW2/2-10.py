string=input("input: ")
num=int(string[:-1])
if (string[-1]=='F'):
    print("{} = {}C".format(string,(num-32)*5/9))
elif (string[-1]=='C'):
    print("{} = {}F'".format(string,num*9/5+32))
