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