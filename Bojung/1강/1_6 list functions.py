a=[1,2,3,4,5,6,7,8,9]
b=[2,4,8,10]
c=[1,3,5,7,9,10]
print a, b, c
a.append(10)
b.insert(2, 6)
c.remove(10)
print a,b,c

a2 = a.count(2)
a3 = a.count(3)
b2 = b.count(2)
b3 = b.count(3)
c2 = c.count(2)
c3 = c.count(3)

print 'There are %d 2s and %d 3s in list a.'%(a2, a3)
print 'There are %d 2s and %d 3s in list b.'%(b2, b3)
print 'There are %d 2s and %d 3s in list c.'%(c2, c3)
