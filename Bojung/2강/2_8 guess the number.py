# Guess the number game
import random

number = random.randint(1,10)
print ("Take a guess between number 1 to 10.")

guess = ''
while guess != number : 
     guess = raw_input()
     guess = int(guess)

     if guess != number : 
          print 'Please try again.'
     
     if guess == number :
          break
     
print 'Great job! The answer was %d' %(number)


     

     
