def merge_(text):
    size=len(text)
    textfilename="연락처.txt"
    f_=open(textfilename,'w')
    for i in range (0,size):
        f=open(text[i],'r')
        line=f.readline()
        f.close()
        f_.write(line)
        f_.write("\n")
    f_.close()
    print("새 파일 생성")


text=[]
print("종료하려면 n 임력")
while(1):
    text_ = str(input("이름: "))
    if (text_!='n'):
        _text_="C:/Users/SANGJIN LEE/Desktop/github/HW3/3/"+text_+".txt"
        text.append(_text_)
    elif (text_=='n'):
        break;
merge_(text)

