#dictionary 
# a look up table that connects keys to values 
# similar to a real dictionary, connects words to their definitions 
my_dict = {
    "key1": "value1", 
    "key2": "value2"
}

#some examples 

# Phone book
contacts = {
    "John": "555-1234",
    "Mary": "555-5678"
}

# Product prices
prices = {
    "apple": 0.50,
    "banana": 0.75,
    "orange": 0.60
}

# Student grades
grades = {
    "Alice": [90, 85, 88],
    "Bob": [78, 92, 86]
}

"""
Why use dictionaries:

Fast lookups - find values quickly using their keys
Clear relationships - each key has exactly one value
Meaningful labels - keys can be descriptive names
Flexible values - can store any type of data (numbers, strings, lists, etc.)

Common uses:

Contact lists (name → phone number)
Price lists (item → cost)
Configuration settings (setting → value)
Caching (input → output)
Counting occurrences (item → count)
"""

#example usage 

# step 1: create the dictionary 
menu = {
    "burger": 8.99,
    "fires": 1.99,
    "apple": 1.89
}

# step 2: Access price 
print(menu["burger"])

# step 3: add new item 
menu["drink"] = 1.99 

# step 4: chnage price 
menu["apple"] = 2.75

# calculte the total order 

order = ["burger", "apple"]
total = 0 
for item in order: 
    total += menu[item]
print(total)