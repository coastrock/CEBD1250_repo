# Coding challenges:
#1 Create a method that takes a list of numbers. Return the largest number in the list
# 2 Define a method that ask the user for a string and print out whether this string is a palindrome or not
# 3 Create a method that returns the number of vowels per string

# Importing a library to work with the random function 
import random

# Defining a class Practice_2 with the asked methods
class Practice_2:
# Defining the method for the challenge 1
    def Largest(l):
        list = []
        for i in range(l):
            list.append(random.randint(1, l))
        print(list)
        print("The largest number in this list is: ", max(list))

# Defining the method for the challenge 2 (adapted from https://stackoverflow.com/questions/29446433/reversing-a-string-and-palindrom-time-complexity-in-python)
    def Check_palindrom(s):
        s_reverse = s[::-1]
        if s == s_reverse:
            print("This string is palindrom!")
        else:
            print("This string is not palindrom...")

# Defining the method for the challenge 3 (adapted from https://stackoverflow.com/questions/36136215/count-the-vowels-in-a-string)
    def Check_vowels(s):
        s = s.casefold()
        count = {}.fromkeys('aeiou',0)
        total = 0
        for k in s:
            if k in count:
                total += 1
        print("Number of vowels in this string is: ", total)

# Getting the input for the method 1
l = int(input("Please, enter the lengh of your list: "))
# Calling the method 1
Practice_2.Largest(l)

# Getting the input for the methods 2 and 3 
s = input("Please, enter string: ")
# Calling the methods 2 and 3
Practice_2.Check_palindrom(s)
Practice_2.Check_vowels(s)
