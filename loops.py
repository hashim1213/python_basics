#For loops - when you want to do something with each item
fruits = ["apple", "banana", "orange"]

#this for loop will print all the fruits
for fruit in fruits:
    print(fruit)

#prints all the numbers from 0-9
for num in range(10):
    print(num)

#While loops keep going while something is true
#this should print 0,1,2
count = 0 
while count < 3: 
    print(count)
    count = count + 1

# Common loop patterns
# Sum all numbers in a list
numbers = [1, 2, 3, 4]
total = 0
for num in numbers:
    total = total + num
print(total)  # Output: 10

# Find something in a list
search = "banana"
for fruit in fruits:
    if fruit == search:
        print("Found it!")
        break  # 'break' exits the loop early