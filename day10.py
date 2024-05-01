# Exception Handling

try:
    num1 = int(input('Enter a number:'))
    print(num1)
except:
    print ('Not a valid number') 


try:
    num1 = int(input('Enter a number:'))
    print(num1)
except ValueError:
    print ('Not a valid number') 

try:
    num1 = int(input('Enter a number:'))
    print(num1)
except Exception as e:
    print(e)
    print ('Not a valid number')  


