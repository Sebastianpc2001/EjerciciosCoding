#Imprimir en la consola 
'''print("Hello World!")'''

# Variables example
name = "John"
age = 25
is_student = True
hobbies = ["reading", "gaming", "coding"]
person = {"name": "John", "age": 25, "is_student": True}


# Desafio 1 
def desaf1():
    name = input("What is your name? ") 

    print(f"Hello {name}! ")

# Desafio 2 
def desaf2(): 
    operation = check()
    value1 = int(input("Firts value?\n"))
    value2 = int(input("Second value?\n"))

    if operation == "add":
        final_value =  add(value1,value2)
        print(f"Your final value is: {final_value}")

    if operation == "sub":
        final_value =  sub(value1,value2)
        print(f"Your final value is: {final_value}")
    if operation == "multiply":
        final_value =  multiply(value1,value2)
        print(f"Your final value is: {final_value}")
    if operation == "divide":
        final_value =  divide(value1,value2)
        print(f"Your final value is: {final_value}")


def check():
    funtions = ['add','sub', 'multiply', 'divide' ]
    print(f"The available operations for this calculator are {funtions[0]}, {funtions[1]}, {funtions[2]}, {funtions[3]}.\n")
    user_funtion = input("What operations do you want? ")
    if user_funtion in funtions:
        return user_funtion
    else: 
        print(f"Funtion not available. The available operations for this calculator are {funtions[0]}, {funtions[1]}, {funtions[2]}, {funtions[3]}.\n")
        user_funtion = input("What operations do you want? ")



def add(value1,value2): 
    return value1 + value2
def sub(value1,value2): 
    return value1-value2
def multiply(value1,value2): 
    return value1*value2
def divide(value1,value2):
    return value1/value2


# Desf 3 Convert Temp Celcius to Fahrenheit

def def3():
    while True: 
        action = int(input("Press 1 to convert Celcius to Fahrenheit or 2 to convert Fahrenheit to Celcius: "))
        if action == 1:
            temp_C = int(input("What Celcius would you like to convert: "))
            temp_F = temp_C * 4.5 + 32
            print(f"{temp_C}C in Fahrenheit is {temp_F}F ")
            break 
        elif action == 2: 
            temp_F = int(input("What Fahrenheit would you like to convert: "))
            temp_C = (temp_F - 32)/4.5 
            print(f"{temp_F}F in Celcius is {round(temp_C,2)}C ")
            break
        else:
            print("Invalid option.")
def3()

        