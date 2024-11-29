# Comparison operators
# == equal to
# != not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

# You can combine conditions with:
# and (both must be true)
# or (at least one must be true)

#if statements 
age = 18
if age >= 18: 
    print("you are an adult")

#if-else statement 
temp = 25 
if temp > 30: 
    print("It hot outside")
else:
    print("it cold bruh!!")

# if-elif-else (multiple conditions)
score = 50
if score >= 90:
    print("A+")
elif score >= 80:
    print("B+")
elif score >= 70:
    print("C+")
else:
    print("below C")

# for "and" both of the conditions have to be true
age = 2
has_licence = True 

if age >= 18 and has_licence:
    print("you can leaglly drive")
else:
    print("you can not leaglly drive")

#check if soemthing is in a list 
fruits = ["apple", "banana", "orange"]
if "apple" in fruits:
    print("we have apples!")

