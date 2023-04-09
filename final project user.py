#The user will have the following functionalities:

#Register on the application. Following to be entered for registration:
#Full Name
#Phone Number
#Email
#Address
#Password
#Log in to the application

#The user will see 3 options:

#Place New Order
#Order History
#Update Profile

#Place New Order: The user can place a new order at the restaurant.
#Show list of food. The list item should as follows:
#1. Tandoori Chicken (4 pieces) [INR 240]
#2. Vegan Burger (1 Piece) [INR 320]
#3. Truffle Cake (500gm) [INR 900]
#Users should be able to select food by entering an array of numbers. For example, if the user wants to order Vegan Burger and Truffle Cake 
#they should enter [2, 3]
#Once the items are selected user should see the list of all the items selected. The user will also get an option to place an order.
#Order History should show a list of all the previous orders



class User:
    
    login_info = {}
    userprofile_info = {}
    
    def __init__(self, fullname, phoneno, email, address, password):
        self.fullname = fullname
        self.phoneno = phoneno
        self.email = email
        self.address = address
        self.password = password
        User.login_info[self.fullname] = self.password
        self.profile = {'Name' : fullname}
        self.order_history = {}
    
    
    def create_new_user(self):
        fullname = input('Enter your Full Name / Username : ')
        phoneno = int(input('Enter your Phone number : '))
        email = input('Enter your Email ID : ')
        address = input('Enter your Address : ')
        password = input('Enter your New Password : ')
        User.login_info[fullname] = {'Full Name ': fullname,
                                     'Phone Number': phoneno,
                                     'Email ID': email,
                                     'Address': address}
        
    @classmethod
    def login(cls, username, password):
        if cls.User_login_info.get(username) == password:
            print("You're are successfully logged in.....")
            return True
        else:
            print("SORRY! These are the Wrong Credentials")
            return False      
    
    def new_order(self):
        print('Please select the items you want to place order ')
        print(ad.view_menu())
        user_choice = int(input('If you want to place order Select 1.Yes or 2.No'))
        if user_choice == 1:
            
            n = int(input('Please enter the number of items you wish to place order : '))
            price = 0
            for i in range(n):
                foodID = int(input('Enter the foodId here: '))
                quant = int(input('Enter the quantity of item: '))
                price += ad.Menu[foodID]['Price'] * quant
                print(f'The price of your order is : {price} INR')
                
                ask_again = input('Please type YES to confirm your order to process or NO ??')
                if ask_again == 'YES' or ask_again == 'yes' or ask_again == 'Yes':
                    
                    print(f"The name of your food item is {ad.Menu[foodID]['Name']}")
                    print(f"This is you quantity {quant}")
                    print(f"It costs you {price} INR in total")
                    print("You're all set for this Order")
                    self.order_history[foodID] = {'Item Name': ad.Menu[foodID]['Name'],
                                                  'Quantity': quant,
                                                  'Item Price' : ad.Menu[foodID]['Price']}
                    
                    print('Order Placed Successfully')
            