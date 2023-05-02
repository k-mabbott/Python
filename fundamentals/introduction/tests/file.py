num1 = 42  #- variable declaration / initialize number
num2 = 2.3  #- variable declaration / initialize float
boolean = True  #- variable declaration / initialize boolean
string = 'Hello World'  #- variable declaration / initialize string  
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  #- variable declaration / initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}    #- variable declaration / initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana')    #- variable declaration / initialize tuple
print(type(fruit))  #log statement / type check 'tuple'
print(pizza_toppings[1])  # log statement / 'Sausage'
pizza_toppings.append('Mushrooms')  #add value / pizza_toppings 'Mushrooms'
print(person['name'])  #log statement / 'John'
person['name'] = 'George'  #change value / 'name': 'George'
person['eye_color'] = 'blue'  #add value / 'eye_color' = 'blue'
print(fruit[2])  #log statement / 'banana'

if num1 > 45: #conditional if num1(42) is less than 45
    print("It's greater")  #log statement "It's greater" if condition true
else:  #conditional else / if num1 less than 45 / 
    print("It's lower")  #log statement "It's lower" if the 'if' condition is not satisfied 

if len(string) < 5:  #conditional if string is less than 5 char long.
    print("It's a short word!")  #log statement "It's a short word!" / if previous condition True
elif len(string) > 15:  #conditional if string is greater than 15 char long.
    print("It's a long word!")  #log statement "It's a long word!" / if previous condition True
else:  #conditional else/ catch whats left after previous conditions 
    print("Just right!")  # if else log statement "Just right!"

for x in range(5):  #for loop
    print(x)  #log statement 0 1 2 3 4
for x in range(2,5):  #for loop
    print(x)  #log statement 2 3 4 
for x in range(2,10,3):  #for loop
    print(x)  #log statement 2 5 8 
x = 0  #initiate variable / assign value type number
while(x < 5):  #while loop
    print(x)  #log statement 0 1 2 3 4  
    x += 1  # change value increases x by one

pizza_toppings.pop()  #change list / remove last item 
pizza_toppings.pop(1) #change list / remove item at index 1

print(person)  #log statement / {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False 'eye_color': 'blue'} 
person.pop('eye_color') #removes key value eye_color
print(person)  #log statement {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

for topping in pizza_toppings:  #for loop
    if topping == 'Pepperoni':  #if condition
        continue  #continues loop
    print('After 1st if statement')  #log statement 'After 1st if statement' (*4)
    if topping == 'Olives':  # if condition
        break  #stops loop

def print_hello_ten_times():  #function / function name inititalized
    for num in range(10):  #for loop
        print('Hello')  # log statement 'Hello'

print_hello_ten_times()  #function call / logs statement 'Hello' (*10)

def print_hello_x_times(x):  #function / function name inititalized
    for num in range(x):  #for loop
        print('Hello')  # log statement 'Hello'


print_hello_x_times(4)  #function call / logs statement 'Hello' (*4)

def print_hello_x_or_ten_times(x = 10):   #function / function name inititalized
    for num in range(x):  #for loop
        print('Hello')  # log statement 'Hello'

print_hello_x_or_ten_times()  # log statement 'Hello'  (*10)
print_hello_x_or_ten_times(4)  # log statement 'Hello'  (*4)


"""
Bonus section
"""

# print(num3)  - NameError: name 'num3' is not defined
# num3 = 72  
# fruit[0] = 'cranberry' - TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team'])  - KeyError: 'favorite_team'
# print(pizza_toppings[7])  - IndexError: list index out of range
#   print(boolean)  - NameError: name 'boolean' is not defined
# fruit.append('raspberry')  - AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)  - AttributeError: 'tuple' object has no attribute 'pop'