print 'Write down the temperature that you want to change.(e.g. 60F, 108C)'
temp = raw_input()

if temp[-1] == 'C' :
     print str(float(temp[0 : -1]) / 5 *9 +32) +'F'

if temp[-1] == 'F' :
     print str((float(temp[0 : -1]) -32) / 9 *5) +'C'
