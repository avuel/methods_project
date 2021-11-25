def main():
    from login import get_password, get_username
    import os
    from time import sleep
    logged_in: bool = False
    run: bool = True
    username: str = None
    password: str = None

    while (run):

        while(not logged_in):
            prompt: str = ('1. Login\n'
                           '2. Create an Account\n'
                           'q. Exit the Program\n')
            print(prompt)
            user_input: str = input('Enter your choice: ')

            LOGIN: str = '1'
            CREATE_ACCOUNT: str = '2'
            EXIT: str = 'q'

            if user_input == LOGIN:
                username: str = get_username()
                if username is None:
                    print('Failed to log in!')
                    sleep(1.5)
                    continue

                password: str = get_password()
                if password is None:
                    print('Failed to log in!')
                    sleep(1.5)
                    continue

                logged_in: bool = True
                print('Successfully logged in!')
                sleep(1.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                

            elif user_input == CREATE_ACCOUNT:
                pass

            elif user_input == EXIT:
                run: bool = False
                break
                

        while(logged_in):
            prompt: str = ('---Welcome to the e-Commerce store---\n\n'
                           '1. Cart\n'
                           '2. Customer\n'
                           '3. Inventory\n'
                           '4. Item\n'
                           'p. Logout\n'
                           'q. Exit the Program\n')
            print(prompt)
            user_input: str = input('Enter your choice: ')
            loop: bool = True
            CART_MENU: str  = '1'
            CUSTOMER_MENU: str  = '2'
            INVENTORY_MENU: str  = '3'
            ITEM_MENU: str  = '4'
            LOGOUT: str = 'p'
            EXIT: str = 'q'
            GO_BACK: str = 'r'

            if user_input == CART_MENU:
                os.system('cls' if os.name == 'nt' else 'clear')
                while loop:
                    cart_prompt: str = ('---Cart---\n\n'
                                        '1. View Cart\n'
                                        '2. Remove an Item from Cart\n'
                                        '3. Add an Item to Cart\n'
                                        '4. Checkout\n'
                                        'r. Go Back\n'
                                        'p. Logout\n'
                                        'q. Exit the Program\n')
                    print(cart_prompt)
                    user_input: str = input('Enter your choice: ')
                    
                    if user_input == '1':
                        pass

                    elif user_input == '2':
                        pass

                    elif user_input == '3':
                        pass

                    elif user_input == '4':
                        pass

                    elif user_input == GO_BACK:
                        loop: bool = False
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue
                    
                    elif user_input == LOGOUT:
                        loop: bool = False
                        logged_in: bool = False
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue

                    elif user_input == EXIT:
                        loop: bool = False
                        logged_in: bool = False
                        run: bool = False
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue
                continue

            elif user_input == CUSTOMER_MENU:
                os.system('cls' if os.name == 'nt' else 'clear')
                while loop:
                    cart_prompt: str = ('---Customer---\n\n'
                                        '1. View Order History\n'
                                        '2. Edit Username\n'
                                        '3. Edit Password\n'
                                        '4. Edit Payment Information\n'
                                        '5. Edit Address Information\n'
                                        'd. Delete Account\n'
                                        'r. Go Back\n'
                                        'p. Logout\n'
                                        'q. Exit the Program\n')
                    print(cart_prompt)
                    user_input: str = input('Enter your choice: ')
                    
                    if user_input == '1':
                        pass

                    elif user_input == '2':
                        pass

                    elif user_input == '3':
                        pass

                    elif user_input == '4':
                        pass

                    elif user_input == '5':
                        pass

                    elif user_input == 'd':
                        pass

                    elif user_input == GO_BACK:
                        loop: bool = False
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue
                    
                    elif user_input == LOGOUT:
                        loop: bool = False
                        logged_in: bool = False
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue

                    elif user_input == EXIT:
                        loop: bool = False
                        logged_in: bool = False
                        run: bool = False
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue
                continue

            elif user_input == INVENTORY_MENU:
                os.system('cls' if os.name == 'nt' else 'clear')
                while loop:
                    cart_prompt: str = ('---Inventory---\n\n'
                                        '1. View Items\n'
                                        '2. Search Item\n'
                                        'r. Go Back\n'
                                        'p. Logout\n'
                                        'q. Exit the Program\n')
                    print(cart_prompt)
                    user_input: str = input('Enter your choice: ')
                    
                    if user_input == '1':
                        pass

                    elif user_input == '2':
                        pass

                    elif user_input == GO_BACK:
                        loop: bool = False
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue
                    
                    elif user_input == LOGOUT:
                        loop: bool = False
                        logged_in: bool = False
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue

                    elif user_input == EXIT:
                        loop: bool = False
                        logged_in: bool = False
                        run: bool = False
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue
                continue

            elif user_input == ITEM_MENU:
                os.system('cls' if os.name == 'nt' else 'clear')
                while loop:
                    cart_prompt: str = ('---Item---\n\n'
                                        '1. View Items\n'
                                        '2. Search Item\n'
                                        '3. View Name\n'
                                        'r. Go Back\n'
                                        'p. Logout\n'
                                        'q. Exit the Program\n')
                    print(cart_prompt)
                    user_input: str = input('Enter your choice: ')
                    
                    if user_input == '1':
                        pass

                    elif user_input == '2':
                        pass

                    elif user_input == '3':
                        pass

                    elif user_input == GO_BACK:
                        loop: bool = False
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue
                    
                    elif user_input == LOGOUT:
                        loop: bool = False
                        logged_in: bool = False
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue

                    elif user_input == EXIT:
                        loop: bool = False
                        logged_in: bool = False
                        run: bool = False
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue
                continue
            
            
            elif user_input == LOGOUT:
                logged_in: bool = False
                continue

            elif user_input == EXIT:
                logged_in: bool = False
                run: bool = False
                continue

if __name__ == '__main__':
    main()