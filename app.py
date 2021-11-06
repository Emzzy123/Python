name = input('What is your name?')
favorite_color = input('what is your favorite color?')
print(name + ' likes '+ favorite_color)

#numbers
birth_year = input('Birth year: ')
print(type (birth_year))
age = 2021 - int (birth_year)
print(type(age))
print(age)

# string
course = "Python 'for' Beginners"
print(course)
course = 'Python "for" Beginners'
print(course)
course = '''
Hi Emeka,

Here is our first email to you.

Thank you,
The support team

'''
print(course)
course = "Python 'for' Beginners"
print(course[3])
print(course[0:6])
print(course[0:])
print(course[:])  #python assumes start and end index

#formatted string
first = 'Emeka'
last = 'Chidoka'
msg = f'{first} [{last}] is a coder'
print(msg)

#string method
course = 'Python for Beginners'
print(len(course))
print(course.isdigit())
print(course.upper())
print(course)
print(course.find('B'))
print(course.replace('Beginners','Absolute Beginners'))
print('Python' in course)

#arithmetic operator
print(10 // 3)
print(10 ** 3)
x=10
x=x+3
print(x)
x+=3  #argumented assigned operator
print(x)

# operator precedent
x=10+3*2
print(x)
# exponentiation 2 ** 3
# multiplication or division
# addition
#
# math function
import math

x=2.9
print(round(x))
print(abs(2.9))
print(math.ceil(2.9))

# if/else statement

is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("Its a cold day")
    print("Wear warm clothes")
else:
    print("Its a lovley day")
print("Enjoy your day")

price = 1000000

has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")

#logical operator
has_high_income = True
has_good_credit = True
has_criminal_record = True

if has_high_income and has_good_credit:
    print("Eligible for loan")

if has_high_income or has_good_credit:
    print("Eligible for loan")

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")

# Comparison operator
temperature = 35

if temperature > 30:
    print("its a hot day")
else:
    print("its not a hot day")

name = "John Smith"

if len(name) < 3:
    print("Name must be at least 3 character")
elif len(name) > 50:
    print("Name must be a maximum of 50 character")
else:
    print("Name looks good!")

# weight
weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")

#while loops - used to execute a block of code multiple times
i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Done")

#guessing number
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print('Sorry, you failed 😪')

# Building the car game
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print('''
start - to start the car
stop - to stop the car
quit -  to quit
        ''')
    elif command == 'quit':
        break
    else:
        print("Sorry, I don't understand that")
# great car game
#
# for loop - used for iterating over items of collection
for item in 'Python':
    print(item)
for item in ['Mosh','John','Sarah']:
    print(item)
for item in [1,2,3]:
    print(item)
for item in range(10):
    print(item)
for item in range(5,10):
    print(item)
for item in range(5,10,2):
    print(item)

prices =[10,20,30,40,50]

total = 0
for price in prices:
    total += price
print(f"Total {total}")

# nested loop
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')
numbers = [5,2,5,2,5]
for x in numbers:
    print('x' * x)
# E shape
numbers = [5,2,5,2,5]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
 #L shape
numbers = [2,2,2,2,5]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

# List
name = ['John','Bob','Mosh','Sarah','Mary']
print(name[2:4])
print(name)
name[0]="Daniel"
print(name)


# largest number
numbers = [3,4,5,6,3,2,56,54,43]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

# 2D List- A case when each item of a list is another list
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)
print (matrix[2][2])
matrix[0][1]=20
print(matrix)

for row in matrix:
    for item in row:
        print(item)

numbers = [5,2,1,7,4,5]
numbers.append(20)
print(numbers)
numbers.insert(2,4)
print(numbers)
# numbers.remove(5)
print(numbers)
# numbers.clear()
print(numbers)
print(numbers.index(1))
print(50 in numbers)
print(numbers.count(5))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
numbers.append(10)
print(numbers2)
print(numbers)

numbers = [2,2,4,6,4,56,4,6,3,4]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

# Tuples
numbers = (1,2,3,1,1)
# print(numbers.count(1))

# Unpacking
coordinates = (1,2,3)
x,y,z = coordinates
print(x,y,z)

# Dictionaries - Store Information as key value pairs
customer = {
    "name":"John smith",
    "age":30,
    "is_verified":True
}
# print(customer['name'])
# print(customer.get("birthdate","Jan 1 1980"))
customer["name"] = "Jack smith"
print(customer["name"])

phone = input("Phone: ")
digits_mapping = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    # "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine",
    "10":"Ten"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

message = input(">")
words = message.split(" ")
emojis = {
    ":)":"😊",
    ":(":"😔"
}
output = ""
for word in words:
     output += emojis.get(word, word) + " "
print(output)

# function
def greet_user(firstname,lastname):
    print("Hi " + firstname + lastname)
    print(f"Hope you good {firstname} {lastname}")
    print("Welcome abroad")


print('start')
greet_user("John","Smith")
print("Finish")

def square(number):
    return number * number

print(square(3))

def emoji_converter(msg):
    words = msg.split(" ")
    emojis = {
        ":)":"😊",
        ":(":"😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))


try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print('Invalid value')

# classes - we use classes to define new types
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

#Constructors - A function that get called at the time of creating an object.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
point.x = 112
print(point.x)

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("Emeka Chidoka")
john.talk()

bob = Person("Bob Smith")
bob.talk()

# Inheritance
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")


dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.be_annoying()




































































