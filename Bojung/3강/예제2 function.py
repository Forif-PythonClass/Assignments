def comparelist(a,b) :
     c = []
     for i in a :
          if i in b :
               c = c + [i]
     print c

comparelist([1,2],[1])
