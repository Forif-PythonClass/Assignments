# coffee machine
coffee = 5


while coffee != 0 :
     print 'Hello! How much do you have?'
     money = raw_input()
     
     if int(money) == 300 :
          print 'Here is your coffee.'
          coffee = coffee -1
          
     elif int(money) > 300 :
          print 'Here is your coffee.'
          coffee = coffee - 1
          print 'Here is your change, %d won. ' % (int(money)-300)

     elif int(money) < 300 :
          print 'Your money is not enough. Here is your change, %d won. ' % int(money)

print "Today's coffee is done."
