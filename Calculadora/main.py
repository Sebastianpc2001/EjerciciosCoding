#Git Challenge from Majo & Sebas

from multiplication import multiplication 
from exponentiation import exponentiation
from sum import sum 

print("Hello this is Majo & Sebas Calculator \n We have the following available operations \n 1.- Sum \n 2.- Multiplication \n 3.- Exponential \n \n")
while True: 
    funtionality = int(input("Press the numer to acces the funtionality."))
    if funtionality > 0:
        break 
    else: 
        print("Please enter correct value")        

match funtionality:
    case 1:
        sum()
    case 2:
        multiplication()
    case 3: 
        exponentiation()

print("\n \n Thanks for using our calculator :)")

