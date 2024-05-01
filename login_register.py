# Requirements
# Ask the user if he/she wants to login or register
# If register, ask for username and password and add the data to the a variable
# Else login, ask for username and password then check whether it is in the variable,, if it is in the a variable print login succesful, else invalid login
# This whole program should be in loop.


a = {} 
while True:
    user_input = input('Do you want to login or register?')
    if user_input == 'register':
        user_name = input('Enter username you want to create:')
        user_password = input('Create a password:')
        a[user_name] = user_password
        print('Registared Successfully')

    elif user_input == 'login':
        user_name = input('Enter your username:')
        user_password = input('Enter your password:')

        if a.get(user_name) == user_password:
            print('Login Successful')
        else:
            print('Invalid Login')

    user_choice = input('Do you want to continue? (yes/no):')
    if user_choice == 'yes':
        continue
    else:
        print('Thank you')
        break
    
         
        



    







