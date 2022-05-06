num1 = 42 #variable delclaration 
num2 = 2.3 #variable delclaration it's a number
boolean = True #variable delclaration, it's a boolean 
string = 'Hello World' #variable delclaration 
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable delclaration, is an array a variable? basically if not technically, data type array
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #creating an array called person
fruit = ('blueberry', 'strawberry', 'banana') # creating an array of fruits
print(type(fruit)) #prints to terminal , only prints the latest item in array?  
print(pizza_toppings[1]) 
    #prints sausage, position 1 of array pizza_topping
pizza_toppings.append('Mushrooms')
#this clearly adds mushrooms to the array, presumably at the end as thats what apend means
print(person['name'])# prints the name portion of array person, not sure how kt knows which part is name ? 
person['name'] = 'George' #changes name to George
person['eye_color'] = 'blue' #adds eyecolor to array, and sets variable to blue.  Nifty, you can assign names (ids?) to variables and store them in arrays nativly
print(fruit[2]) #prints position 2 of fruit, banana

# this is a loop that sorts num1 and prints a response based on it's value, an if loop
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
#this if else loop grads the string variable based on length
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
#its a for loop fo sho, and it prints counting up to 8
for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

#these modify the pizza array, removing the last and 1 postion variables?
pizza_toppings.pop()
pizza_toppings.pop(1)

print(person) #prints array person
person.pop('eye_color') #removes eye_color
print(person) #prints array again with now no eye clolor

#for loop that prints after 1st if statement until it is = to olives
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():#prints hello 10 times i beleive?  range appears to be the same as js using a for loop for incrementing but built in
    for num in range(10):
        print('Hello')

print_hello_ten_times() #cals the above functionbut doesn't print becaue no input?

def print_hello_x_times(x): # defines function print_hello_x_times, a variable version of the above function where a value is set to X
    for num in range(x):
        print('Hello')

print_hello_x_times(4) # calls above function

def print_hello_x_or_ten_times(x = 10):#defines a fuction that does the thing, pprinting hello 10 times or x times?
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() #prints 10 times
print_hello_x_or_ten_times(4)# prints 4 times?


"""
Bonus section (this is a multiline comment that is on a single line) unless you count the marks
"""

# print(num3)    these are all comments that are single line below this.  this prints an undefined variable, causing an error
# num3 = 72      this defines the variable above, likely allowing it to print
# fruit[0] = 'cranberry' changes the first postion of fruit to cherry
# print(person['favorite_team'])    prints an undefined position of array person, causing a type error?
# print(pizza_toppings[7])          prints an undfined pizza topping
#   print(boolean)                  prints true?
# fruit.append('raspberry')         adds raspberry
# fruit.pop(1)                      removes strawberry