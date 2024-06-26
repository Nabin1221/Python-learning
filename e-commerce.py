# Requirements
# Ask the user if he/she wants to login or register
# If register : Ask username, password, usertype(buyer/seller) and store it in a file.
# Else login - Ask username and password, if the username and password exists on userdata file then print login successfull. Check the usertype. 
# If the user is buyer, give him choices : View all products, view bills, Purchase products. If the user is seller : Add products, view his/her products, view his/her product bills.

import json


def register():
    user_username = input('Enter your username:')
    user_password = input('Enter your password:')
    user_usertype = input('Are you a buyer or seller? (b/s)')

    user_data = {'user_username':user_username,'user_password':user_password,'usertype':user_usertype}
    json_user_data = json.dumps(user_data)

    f = open('C:/Users/nabin/Desktop/Python Class/buyer_seller.txt', 'a')
    
    f.write(json_user_data + '-')

    f.close()               


def login():
    user_username = input('Enter your username:')
    user_password = input('Enter your password:')

    f = open('C:/Users/nabin/Desktop/Python Class/buyer_seller.txt','r')

    json_user_data = f.read()

    f.close()

    list_user_data = json_user_data.split('-')
    user_login = False
    for i in list_user_data:
        if i != '':
            dict_data = json.loads(i)
            if (user_username == dict_data.get('user_username')) and user_password == dict_data.get('user_password'):
                user_login = True
                type = dict_data.get('usertype')
                break
                


    if user_login == True:
        print('Login Successful!')
        if type == 'b':
            print(f'Hi {dict_data.get('user_username')}! Welcome to your buyer account.')
            print('What would you like to do?')

            user_operation = input('[view products/ purchase/ view bills]:').lower()
            if user_operation == 'view product' or user_operation == 'view products':
                view_all_products()
            elif user_operation == 'view bill' or user_operation == 'view bills':
                view_bills(user_username)
            elif user_operation == 'purchase':
                purchase(user_username)
            else:
                print ('Invalid Selection!')  

        else:
            print(f"Hi {dict_data.get('user_username')}! Welcome to your seller account.")
            print('What would you like to do? ')

            user_operation = input('[add product/ view product/ view bills/ my products] :').lower() 
            if user_operation == 'add product' or user_operation == 'add products':
                add_product(user_username)              
            elif user_operation == 'view product' or user_operation == 'view products':
                view_all_products()
            elif user_operation == 'view bill' or user_operation == 'view bills':
                view_bills_seller(user_username)
            elif user_operation == 'mr product' or user_operation == 'my products':
                view_products(user_username)
        
            else:
                print('Invalid selection!!!')

    else:
        print('Invalid Credentials!')

def view_bills(user_username):

    f = open('C:/Users/nabin/Desktop/Python Class/bill_data.txt','r')
    json_bill = f.read()
    f.close()
    list_json = json_bill.split('-')
    total_amount = 0
    for i in list_json:
        if i != '':
            dict_data = json.loads(i)
            if (user_username == dict_data.get('user_username')):
                print(f'{dict_data.get('product')} * {dict_data.get('quantity')}: Rs. {dict_data.get('total')}')
                total_amount = total_amount + int(dict_data.get('total'))
    print (f'Your total is {total_amount}')

def view_bills_seller(user_username):

    f = open('C:/Users/nabin/Desktop/Python Class/bill_data.txt','r')
    json_bill = f.read()
    f.close()
    list_json = json_bill.split('-')
    total_amount = 0
    print(f'For the seller account {user_username}:')
    for i in list_json:
        dict_data = json.loads(i)
        if (user_username == dict_data.get('sellername')):
            print(f'Buyer: {dict_data.get('user_username')} || {dict_data.get('product')} * {dict_data.get('quantity')}: Rs. {dict_data.get('total')}')
            total_amount = total_amount + int(dict_data.get('total'))
    print(f'Total : Rs. {total_amount}')        


def purchase(user_username):
    purchase_product_name = input('Which product do you want to buy? ')
    
    purchase_quantity = int(input('How much quantity? '))

    f = open('C:/Users/nabin/Desktop/Python Class/product_data.txt','r')

    product_json_data = f.read()

    f.close()

    list_product_data = product_json_data.split('-')
    available = False
    for i in list_product_data:
        if i != '':
            dict_data = json.loads(i)
            if purchase_product_name == dict_data['product_name']:
                price = int(dict_data['product_price'])
                available = True
                break

    if available == True:
        print(f'Purchase of {purchase_product_name} completed!')
        total = purchase_quantity * price
        print(f'Your total is {total}')  

        total_bill = {'user_username':user_username,'product':purchase_product_name,'quantity':purchase_quantity,'total':total, 'sellername': dict_data.get('sellername')}
        json_bill_data = json.dumps(total_bill)
        g = open('C:/Users/nabin/Desktop/Python Class/bill_data.txt','a')
        g.write(json_bill_data + '-')
        g.close()
    else:
        print(f'Product with name {purchase_product_name} not available!')

def view_all_products():
    f = open('C:/Users/nabin/Desktop/Python Class/product_data.txt','r')
    product_json_data = f.read()
    f.close()
    list_user_data = product_json_data.split('-')
    for i in list_user_data:
        if i != '':
            dict_data = json.loads(i)
            print(f"{dict_data.get('product_name')}   |   Rs. {dict_data.get('product_price')}  |   seller: {dict_data.get('sellername')}")

def view_products(user_username):
    f = open('C:/Users/nabin/Desktop/Python Class/product_data.txt','r')
    product_json_data = f.read()
    f.close()
    list_user_data = product_json_data.split('-')
    for i in list_user_data:
        if i!= '':
            dict_data_json.loads(i)
            if (user_username == dict_data.get('sellername')):
                print(f"{dict_data.get("product_name")}   |   Rs. {dict_data.get("product_price")}  ")


def add_product(user_username):
    product_name = input('Enter product name: ')
    product_description = input('Enter product description: ')
    product_price = int(input('Enter product price: '))

    product_dict_data = {'product_name':product_name , 'product_description': product_description , 'product_price': product_price, 'sellername': user_username}
    product_json_data = json.dumps(product_dict_data)
    f = open('C:/Users/nabin/Desktop/Python Class/product_data.txt','a')
    f.write(product_json_data + '-')
    f.close()

    print(f'Your product with name {product_name} is added!!')


while True:
    user_choice = input('Do you want to login or register?').lower()

    if user_choice == 'register':
        register()

    elif user_choice == 'login':
        login()
    else: 
        print('Invalid option!!')
    user_choice = input('Do you want to use the program again? (y/n)')
    if(user_choice =='y' or user_choice == 'Y'):
        continue
    elif(user_choice =='n' or user_choice =='N'):
        print('Thankyou for using this program')
        break    


        


    

