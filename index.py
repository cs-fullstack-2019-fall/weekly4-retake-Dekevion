# 1. Ask a user for their first name and age. Print "[NAME] is [AGE] years old"

# name = input('what is your first name?')
# age = int(input('what is your age'))
# nameAGE = (f'{name} is {str(age)} years old')
# print(nameAGE)


#2. Ask the user to enter their age. Check if they entered a value between 0 and 125. If valid, print "REAL AGE". If invalid print “NOT A REAL AGE!!!”

# age = int(input('enter your age'))
# if age >= 0 and age <= 125:
#     print('Real Age')
# else:
#     print('not a real age')

# 3. Use a for loop to print every 4 numbers from -50 to 50.

# for i in range(-50, 51, 4):
#     print(i)

# 4. Ask the user to enter a number to add to a total. Keep asking the user to enter a number until they enter 0. Afterward, print the total of all numbers entered.
#

ask = -1
total = -2
while ask != 0:
    total = 0
    ask = int(input('enter a number to add to the total, press 0 to exit'))
    print(total + ask)
print(ask)

# 5. Create an array of 4 names. Print one string that has all of the arrays separated by commas.

# nameArray = ['A','B','C','D']
#
# print(nameArray[::])

## 6. Create a function that’s passed three integer numbers. Print the sum of the first two numbers and return the product of the second two numbers.

# def threeInt(a,b,c):
#    sum = (a + b)
#    print(sum)
#    product = (b * c)
#    print(product)
#
# threeInt(5,5,5)

# 7. Create the class Boardgame with name, price, pieceCount, and publisher properties/attributes. Create a class method that will change the price of the book. Outside of the class, create three objects of the class Boardgame. Print the three boardgame objects using the newly created objects.
#
# class Boardgame():
#     def __init__(self, name, price, pieceCount, publisher):
#         self.name = name
#         self.price = price
#         self.pieceCount = pieceCount
#         self.publisher = publisher
#
#     def printProp(self):
#         print(f'{self.name}, {self.price}, {self.pieceCount}, {self.publisher}')
#
#     def priceChange(self,newPrice):
#         self.price = newPrice
#
# boardgame1 = Boardgame('snakes and ladder', '2.5','10pieces', 'mono')
# boardgame2 = Boardgame('oranges and fruits', '3.5','15pieces', 'poly')
# boardgame3 = Boardgame('Balls and Bells', '12','5pieces', 'hasbro')
#
# print(boardgame1.printProp())
# print(boardgame2.printProp())
# print(boardgame3.printProp())
#

# 8. Create a function that takes a string array and returns a string array with the letter 's' at the end of each element. Call the function.

# def stringArray():
#     stringsInArray = ['gun', 'rose']
#     for i in stringsInArray:
#         print(i + 's')
#
# stringArray()

# 9. Create a function that has a parameter of an integer array and returns only the positive numbers in the array. Call the function
# numArray =[]
#
# def int(a):
#     if a > 0:
#         numArray.append(a)
#         print(numArray)
#     else:
#         print('invalid')
#
# int(-1)



# 10. Create a Puppy class. It should have properties name and color. Create a program that will ask a user to enter the name, then the color of a puppy until they enter 'q' to quit. Put each entry in an array.

#
# class Puppy:
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color
#     def __str__(self):
#         return 'string'
#
#
# array = []
# menu = ''
# menu2 = menu
# while menu != 'q':
#     menu = input('enter the name of a puppy')
#     menu2 = input('enter the color of puppy')
#     OtherPuppy = Puppy(menu,menu2)
#     array.append(OtherPuppy)
#     print(array)
#
