#question 1: 
# Write a function that takes a temperature and returns if it's "Hot" (over 30°C), 
# "Warm" (20-30°C), or "Cold" (under 20°C)

def tempcalc(temp):
    if temp >= 30: 
        return "its hot"
    elif 20 <= temp <= 30:
        return "its warm"
    else:
        return "its cold"

print(tempcalc(90))

#question 2 
# Write a function that:
# - Takes a list of numbers
# - Returns how many are positive, how many are negative, and how many are zero

def count_nums(numbers):

    positive = 0
    negative = 0 
    zero = 0 

    for num in numbers: 
        if num > 0: 
            positive = positive + 1
        elif num < 0: 
            negative = negative + 1
        else: 
            zero = zero + 1

    return positive, negative, zero

numbers = [1, -2, 0, 3, -4, 0, 5]
pos, neg, zero = count_nums(numbers)

print(f"positive: {pos}")
print(f"negative: {neg}")
print(f"zero: {zero}")

#question 3 
# Write a function that takes a sentence and returns:
# - The longest word
# - The shortest word
# - Average word length

def word_counter(sentance):
    words = sentance.split() #split the sentance into a list

    longest_word = words[0]
    shortest_word = words[0]
    total_length = 0

    #loop through each of the wod to find the longest, shortest, and total length 

    for word in words: 
        #checks if the current word is longer than our longest 
        if len(word) > len(longest_word):
            longest_word = word 
        
        #check if curretnt word is shorter than our shortest 
        if len(word) < len(shortest_word):
            shortest_word = word 

        total_length = total_length + len(word)
    #clac the avg
    average_length = total_length / len(words)

    return longest_word, shortest_word, average_length 

sentence = "Python is an amazing programming language"
longest, shortest, average = word_counter(sentence)

print(f"Longest word: {longest}")
print(f"Shortest word: {shortest}")
print(f"Average word length: {average:.2f}")

#question 4
# Create a function that:
# - Takes a list of items and their prices
# - Gives 20% discount if buying 3 or more items
# - Gives additional 10% discount if total is over 100
# - Returns final price

def cart_total(cart):
    #calculate the initial total 
    total = 0 
    for item, price in cart: 
        total = total + price 
    #length of cart greater than 3 
    if len(cart) > 3: 
        total = total * 0.8
    #10% discount if total is over than $100
    if total > 100: 
        total = total * 0.9 
    
    return total 

#test function 
cart = [("shirt", 20), ("pants", 45), ("shoes", 40)]
final_price = cart_total(cart)
print(f"Final price: ${final_price:.2f}")

#question 5 
# Write a function that takes a list of numbers and:
# - Doubles the even numbers
# - Triples the odd numbers
# - Returns the new list

def list_manipulate (numbers):
    new_list = []
    for num in numbers: 
        if num % 2 == 0: #if even 
            new_list.append(num * 2)
        else: #if odd
            new_list.append(num * 3)
    return new_list 
#test case 
numbers = [1, 2, 3, 4, 5]
result = list_manipulate(numbers)
print(result)

#question 6 
# Create a function that checks if a password is strong:
# - At least 8 characters
# - Contains at least one uppercase letter
# - Contains at least one number
# - Returns True or False

def pass_check(password):

    if len(password) < 8: 
        return False 
    has_upper = False 
    has_number = False 

    for char in password: 
        if char.isupper(): 
            has_upper = True 
        if char.isdigit():
            has_number = True 
    return has_upper and has_number 

print(pass_check("Python"))  # True

#question 7 

# Write a function that:
# - Takes a list of anything (numbers, strings, etc)
# - Removes all duplicate items
# - Removes any strings that are less than 3 characters
# - Returns the cleaned list


def double_remove (mixed_list):
    new_list = []
    
    for items in mixed_list: 

        if isinstance(items, str) and len(items) < 3: 
            continue 
        if items not in new_list: 
            new_list.append(items)

    return new_list

mixed_list = [1, "a", "hello", 3, "hi", 1, "hello", "python", 2]
result = double_remove(mixed_list)
print (result)