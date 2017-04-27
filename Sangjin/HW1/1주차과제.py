import turtle

while(1):
    a = int(input("Input -1 to break;\nInput the question number:"))
    if (a==1):
        print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!")
        print("\t\tUp above the world so high,\n\t\tLike a diamond in the sky.")
        print("Twinkle, twinkle, little star,\n\tHow I wonder what you are")
        print("\n")
    elif (a==2):
        firstname=input("Input first name:")
        lastname=input("input last name:")
        print("Your name is {} {}".format(lastname,firstname))
        print("\n")
    elif (a==3):
        filename=input("Sample filename:")
        filename_=filename[filename.find('.')+1:]
        print("Output:{}".format(filename_))
        print("\n")
    elif (a==4):
        a="101112131415"
        total=0
        for i in range(0,12):
            total=total+int(a[i:i+1])
        print("sum=",total)
        print("\n")
    elif(a==5):
        color_list=["Red","Green","White","Black"]
        print("{},{}".format(color_list[0],color_list[1]))
        print("\n")
    elif(a==6):
        a=[1,2,3,4,5,6,7,8,9]
        b=[2,4,8,10]
        c=[1,3,5,7,9,10]
        a.append(10)
        b.insert(2,6)
        c.remove(10)
        print("a=",a)
        print("b=",b)
        print("c=",c)
        count2=a.count(2)+b.count(2)+c.count(2)
        count3=a.count(3)+b.count(3)+c.count(3)
        print("2:{} and 3:{}".format(count2,count3))
        print("\n")
    elif(a==7):
        a=[38,5,6,72,1,99]
        b=[3,9,4,2,70,1]
        c=a+b
        c.sort()
        print("answer=",c)
        print("\n")
    elif(a==8):
        milk=2.50
        icecream=1.2
        energydrink=3.50
        total=2*milk+5*icecream+energydrink
        if (total<20):
            print("거스름돈 = ",20-total)
        print("\n")
    elif(a==9):
        t=turtle
        t.penup()
        t.goto(-250,100)
        t.pendown()
        for i in range (0,6):
            t.forward(100)
            t.left(60)
        t.penup()
        t.goto(150,100)
        t.pendown()
        for i in range(0,3):
            t.forward(120)
            t.left(120)
        t.penup()
        t.goto(-250,-250)
        t.pendown()
        index=50
        for i in range(0,5):
            for j in range(0,4):
                t.forward(index)
                t.left(90)
            index=index+20
        t.penup()
        t.goto(150,-250)
        t.pendown()
        for i in range(0,3):
            for j in range(0,4):
                t.forward(100)
                t.left(90)
            t.left(30)
        t.done()
        print("\n")
    elif(a==10):
        t=turtle
        for i in range(0,20):
            t.circle(100)
            t.left(18)
        t.done()
        print("\n")
    elif(a==-1):
        break
    elif (a==11):
        index=1
        for i in range (0,7):
            for j in range(0,index): print("*")
            if (index==4): index=index-1
            else: index=index+1
            print("\n")
