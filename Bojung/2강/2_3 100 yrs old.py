print 'What is your name?'
name = raw_input()

print 'How old are you?'
age = raw_input()
age = int(age)

print '%s will become 100 yrs old in %d years.' % (name, (100-age))
