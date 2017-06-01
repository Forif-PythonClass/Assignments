money = 0
while money < 10000 :
     print '--OPEN--'
     print '''What do you want?
We have 1. Coke, 2. Juice, 3. Energy Drink.'''
     beverage = int(raw_input())
     if beverage == 1 :
          money = money + 1500
          print 'Here is your coke.'
     elif beverage == 2 :
          money = money + 1200
          print 'Here is your juice.'
     elif beverage == 3 :
          money = money + 2000
          print 'Here is your energy drink.'

print '--CLOSED--'
