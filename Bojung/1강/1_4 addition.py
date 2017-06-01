a = '10,11,12,13,14,15'
start = 0
end = 2
add = 0
while end <= (len(a) +1) :
     add = add + int(a[start : end])
     start = start + 3
     end = end + 3

print add
