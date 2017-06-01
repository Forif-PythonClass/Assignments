import random
ranNum = random.randint(1,9)
print 'Hi! Please guess the number (1~9)'
playerNum= raw_input()

while str(ranNum) != playerNum :
     print 'Try again please.'
     playerNum = raw_input()

print 'Great Job!'
