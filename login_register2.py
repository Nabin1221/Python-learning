# Requirements
# Ask the user if he/she wants to login or register.
# Register - Ask username and password, we add the data to a file using file handling.
# Login - Ask username or password, then read data from the file whereuser data is being stored during register and 
# and check whether the username and password provided exists or not. If exists print login success else invalid login.

import json
user_choice = input('Do you want to login or register?').lower()

def register():
    user_username = input('Enter your username:')
    user_password = input('Enter your password:')

    user_data = {user_username:user_password}
    json_user_data = json.dumps(user_data)

    f = open('C:/Users/nabin/Desktop/Python Class/userdata.txt', 'a')

    f.write(json_user_data + '-')

    f.close()

register()

def login():
    user_username = input('Enter your  username:')
    user_password = input('Enter your password:')

    f = open('C:/Users/nabin/Desktop/Python Class/userdata.txt','r')

    json_user_data = f.read()

    f.close()
    
    list_user_data = json_user_data.split('-')
    user_login = False
    for i in list_user_data:
        if i != '':
            dict_data = json.loads(i)
            if user_username in dict_data and user_password == dict_data.get(user_username):
                user_login = True

            if user_login == True:    
                print('Login Successful')
            else:
                print('Invalid credentials!')    

    


user_choice = input('Do you want to login or register?').lower()

if user_choice == 'register':
    register()

elif user_choice == 'login':
    login()



