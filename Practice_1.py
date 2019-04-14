# Coding challenges:
# 1 Define a method that ask the user for a number.
#    Depending on whether the number is even or odd, print out an appropriate message
# 2 Write a method that takes a number and print its square
# 3 Write a method to convert degrees of Fahrenheit to Celsius


# Importing a library to work with the square root function
import math 

# Defining a class Practice_1 with the 3 asked methods 
class Practice_1:

# Defining the method for the challenge 1
    def Check_even_odd(x):
        if x %2 == 0:
            print("Your number is even!")
        else:
            print("Your number is odd!")

# Defining the method for the challenge 2
    def Sqrt(y):
        print("The square root of your number is: ", math.sqrt(y))

# Defining the method for the challenge 3
    def Convert(z):
        c = (z-32)*5/9 
        print("The temperature in Celsius is: ", c)

# Getting input for the method 1
x = int(input("Please, enter a number: "))
# Calling method 1
Practice_1.Check_even_odd(x)

# Getting input for the method 2
y = int(input("Please, enter a number: "))
# Calling method 2
Practice_1.Sqrt(y)

# Getting input for the method 3
z = int(input("Please, enter the temperature in Fahrenheit to be converted in Celsius: "))
# Calling method 3
Practice_1.Convert(z)
