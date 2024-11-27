#creating lists 
numbers = [0,1,2,3,4,5] #number list 
names =["Hashim", "Asit", "Liam"] #string list
mixed = [1,"hey", 3.141, False] #mixed data types 

print(names) #outputs the list of names 

#accessing the items inside the string 
print(names[0]) #indexing starts at 0 (first pos is 0)
#the above should output Hashim 
print(names[1]) #should print Asit
print(names[-1]) #should print Liam, negative indexies start from the end 

#how to change items in lists?
names[0] = "Asit"
names[1] = "Hashim"
print(names)
#add a new name to the list 
names.append("David")
print(names)
#add a new name to the list in a specific position in the list
names.insert(2, "Mike")
print(names)

#remove items from lists 
names.remove("Asit") 
print(names)
#remove and return last item 
popped = names.pop()
print(names, popped)
#remove names at specific index 
del names[1]
print(names)

names.insert (0,"Zelous")

###Useful List Opertaions###
#get the length of list 
length = len(names) 
print(length)
#auto storts the names in alpha. order 
sorted_names = sorted(names) 
print(sorted_names)
names.sort()
names.reverse()

#slicing a list 
print(numbers[:3])
print(numbers[1:4])
print(numbers[2:])