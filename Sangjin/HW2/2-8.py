import random
target_num=int(random.randint(1,10))
while (1):
    num=int(input("숫자를 입력하시오: "))
    if num==target_num:
        print ("Good")
        break;
    else:
        print("Try Again")
