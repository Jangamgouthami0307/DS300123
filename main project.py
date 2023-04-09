import  admin as aa
import user as us

print('********** WELCOME TO FOODZY **********')

inp = int(input('\nPlease select an Option to Login 1. ADMIN \n2.USER \n3.EXIT' ))
if inp == 1:
    username = input('Enter the username of admin : ')
    password = input('Enter the admin password : ')
    if aa.admin_keys[username] == password:
        print('*****You are Successfully LoggedIn as admin')
        admin_crawler = True
        while admin_crawler:
            admin_choice = int(input('Please select an option from Admin panel : \n1. Add New Food Item \n2. Edit Food Item \n3. View Menu \n4. Remove Item from Menu \n5. Exit'))
            if admin_choice == 1:
                aa.add_food_item()
            elif admin_choice == 2:
                aa.edit_food_item()
            elif admin_choice == 3:
                aa.view_menu()
            elif admin_choice == 4:
                aa.remove_item()
            elif admin_choice == 5:
                print('You have opted to exit out of admin panel')
                admin_crawler = False
            else:
                print('Please select a valid Input!!')
    else:
        print('Username and Password doesnot Match \nPlease Login Again \nThank You')
        
elif inp == 2:
    print('***** WELCOME to FOODZY *****')
    inp2 = int(input('\nPress 1 to Create a New account \nPress 2 to Login \nPress 3 to Main Menu'))
    if inp2 == 1:
        print(' Welcome to user register panel ')
        pass
    elif inp2 == 2:
        print()
