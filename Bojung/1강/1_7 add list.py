a=[38,5,6,72,1,99]
b=[3,9,4,2,70,1]

c = a + b

c.sort(key=None,reverse=False)
print c

c.sort(key=int,reverse=False)
print c

c.sort(key=str,reverse=False)
print c

# int면 숫자로, str이면 문자로 (앞자리부터)
