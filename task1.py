def calculator():
    num1 = int(input('Enter a number:'))
    num2 = int(input('Enter another number:'))

    math_opt = input('Which arithmetic operation do you want to perform [+,-,*,,/]')

    if math_opt == '+':
        print(num1 + num2)

    elif math_opt == '-':
        print(num1 - num2)

    elif math_opt =='*':
        print(num1 * num2)

    elif math_opt =='/':
        print(num1 / num2)
    else:
        print('Invalid operator!')
calculator()        

while True:
    user_choice = input('Do you want to run the calculator again? (yes/no):')   
    if user_choice == 'yes':
        calculator()
    else:
        break    






