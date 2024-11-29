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
    