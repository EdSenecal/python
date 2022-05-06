for x in range (0,151):
    print (x)

for y in range (5,1001,5):
    print(y)

for dojo in range (0,101,5):
    print ("coding dojo")
    if dojo == 100:
        break    
    print(dojo + 1)
    print (dojo + 2)
    print (dojo + 3)
    print (dojo + 4)

number = 0

for huge in range (1,500001,2):
    number = number + huge
print (number)

for countdown in range (2018,0,-4):
    print (countdown)

lowNum = 2
highNum = 9
mult = 3

for i in range (lowNum,highNum + 1):
    if i %  mult == 0:
        print(i)
