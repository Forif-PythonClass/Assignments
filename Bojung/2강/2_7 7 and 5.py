a = 1500
num = []
while a <= 2700 :
     num = num + [a]
     a = a+1

answer = []
for i in num :
     if i % 7 == 0 :
          if i % 5 == 0 :
               answer = answer + [i]
print answer
