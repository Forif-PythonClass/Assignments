a=[38,5,6,72,1,99]
b=[3,9,4,2,70,1]

c = a + b

c.sort(key=None,reverse=False)
print c

c.sort(key=int,reverse=False)
print c

c.sort(key=str,reverse=False)
print c

# int�� ���ڷ�, str�̸� ���ڷ� (���ڸ�����)
