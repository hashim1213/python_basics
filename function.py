#def is used as a special word by python to idicate the start of a function
def say_hello(name): #say_hello is the fuction name 
        print(f"Hey, {name}!") 

say_hello("Hashim")

def add_numbers(x, y):
        return x + y #retun sends a value back to whereever the fuction was called 
#when return is used it ends the function and returns the value 
#the returned value can be saved in the variable 

#Calculate salary 
def calculate_totals(hours, rate):
        pay = hours * rate
        return pay
salary = calculate_totals (35,132.95)
print(salary)

#calculate temp
def calc_temp(celcius):
        far = celcius * (9/5) + 32
        return far
convert = calc_temp(-20)
print(convert)

