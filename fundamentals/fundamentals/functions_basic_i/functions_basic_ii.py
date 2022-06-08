

def countdown(a):
    the_final = []
    for i in range (a, -1, -1):
        the_final.append(i)
    return the_final

print (countdown (5))

def number2(p,r):
    print (p)
    return (r)

print (number2 (1,2))



def first_plus_length (a):
    return a [0] + len (a)

print (first_plus_length ([1,2,3,4,5]))



def values_greaterthan_second (list):
    if len (list) < 2:
        return False
    output = []
    for i in range (0, len(list)):
        if list[i] > list[1]:
            output.append(list[i])
    print(len(output))
    return output

print (values_greaterthan_second([5,2,3,2,1,4]))

print ([3])

def length_value (size,length):
    output = []
    for i in range (0, size):
        output.append(length)
    return output

print (length_value(4,7))