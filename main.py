import os
from Customer import *
from time import sleep


# Jacob's code #
def main():
    logged_in: bool = False
    run: bool = True

    while run:
        # Loop until we have logged in or exit
        while not logged_in:
            # Clear the screen and display the pre-login prompt
            os.system('cls' if os.name in ('nt', 'dos') else 'clear')
            prompt: str = ('1. Login\n'
                           '2. Create an Account\n'
                           'q. Exit the Program\n')
            print(prompt)

            # Grab the user's input
            user_input: str = input('Enter your choice: ')

            # Menu options for the user
            LOGIN: str = '1'
            CREATE_ACCOUNT: str = '2'
            EXIT: str = 'q'

            # After we make our choice, clear the screen
            os.system('cls' if os.name in ('nt', 'dos') else 'clear')

            # If we want to log in, attempt to get the username and password to login
            if user_input == LOGIN:
                # Get the user's input and create a Customer object
                username = input("Enter your username: ")
                password = input("Enter your password: ")

                CustomerObj = Customer(username, password)

                # Attempt to log the user in and get the result
                logged_in = CustomerObj.login()
                if logged_in is False:
                    print('Failed to log in!')
                    sleep(1.5)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue

                elif logged_in is True:
                    print('Successfully logged in!')
                    sleep(1.5)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue

                sleep(1.5)
                os.system('cls' if os.name == 'nt' else 'clear')

            # If we want to create an account, ask for a username and password (and validate the account can be made)
            elif user_input == CREATE_ACCOUNT:
                # Get the user's input and create a Customer object
                username = input("Enter your username: ")
                password = input("Enter your password: ")

                CustomerObj = Customer(username, password)

                create_result = CustomerObj.create_account()
                if create_result is False:
                    print('Failed to create account!')
                    sleep(1.5)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue

                elif create_result is True:
                    print('Successfully created account!')
                    sleep(1.5)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue

                sleep(1.5)
                os.system('cls' if os.name == 'nt' else 'clear')

            # Exit the program
            elif user_input == EXIT:
                run: bool = False
                print('---Exiting---\n')
                break

        # Display menus and allow the user to interact with the store once we are logged in
        while (logged_in):
            # Print the e-Commerce Store prompt to the user
            prompt: str = ('---Welcome to the e-Commerce store---\n\n'
                           '1. Cart\n'
                           '2. Customer\n'
                           '3. Inventory\n'
                           '4. Item\n'
                           'p. Logout\n'
                           'q. Exit the Program\n')
            print(prompt)

            # Grab the input from the user and set our loop variable to true (this will loop us in the sub-menu we choose)
            user_input: str = input('Enter your choice: ')
            loop: bool = True

            # After we make our choice, clear the screen
            os.system('cls' if os.name in ('nt', 'dos') else 'clear')

            # Menu options for the user
            CART_MENU: str = '1'
            CUSTOMER_MENU: str = '2'
            INVENTORY_MENU: str = '3'
            ITEM_MENU: str = '4'
            LOGOUT: str = 'p'
            EXIT: str = 'q'
            GO_BACK: str = 'r'

            # Display the cart menu and handle interacting with the user's cart
            if user_input == CART_MENU:
                # Loop until we want to return to the main menu, log out, or exit the program
                while loop:
                    # Clear the screen and print the Cart prompt to the user
                    os.system('cls' if os.name == 'nt' else 'clear')
                    cart_prompt: str = ('---Cart---\n\n'
                                        '1. View Cart\n'
                                        '2. Remove an Item from Cart\n'
                                        '3. Add an Item to Cart\n'
                                        '4. Checkout\n'
                                        'r. Go Back\n'
                                        'p. Logout\n'
                                        'q. Exit the Program\n')
                    print(cart_prompt)

                    # Grab the user's input
                    user_input: str = input('Enter your choice: ')

                    # Clear the screen after we get our input
                    os.system('cls' if os.name in ('nt', 'dos') else 'clear')

                    # Menu options for the user
                    VIEW_CART = '1'
                    REMOVE_ITEM = '2'
                    ADD_ITEM = '3'
                    CHECKOUT = '4'

                    # Display the user's cart
                    if user_input == VIEW_CART:
                        print(f'---{username}\'s Cart---\n')

                    # Attempt to remove the user specified item from their cart
                    elif user_input == REMOVE_ITEM:
                        print('---Remove Item---\n')
                        item_name = input('Please enter the name of the item you would like to remove from the Cart: ')
                        if (item_name is not None):
                            print(f'Successfully removed {item_name} from the Cart')
                        else:
                            print(f'{item_name} is not in the Cart')
                        sleep(1.5)
                        os.system('cls' if os.name in ('nt', 'dos') else 'clear')

                    # Attempt to add the user specified item to their cart
                    elif user_input == ADD_ITEM:
                        print('---Add Item---\n')
                        item_name = input('Please enter the name of the item you would like to add to the Cart: ')

                    # Check the user out
                    elif user_input == CHECKOUT:
                        print('---Checkout---\n')

                    elif user_input == GO_BACK:
                        loop: bool = False
                        continue

                    # Log the user out
                    elif user_input == LOGOUT:
                        loop: bool = False
                        logged_in: bool = False
                        print('Logging Out...\n')
                        sleep(1.5)
                        continue

                    # Exit the program
                    elif user_input == EXIT:
                        loop: bool = False
                        logged_in: bool = False
                        run: bool = False
                        print('Exiting...\n')
                        continue
                continue

            # Display the Customer Menu and handle interacting with the user's account
            elif user_input == CUSTOMER_MENU:
                # Loop until we want to go back to the main store menu, log out, or exit the program
                while loop:
                    # Clear the screen before displaying the Customer Menu
                    os.system('cls' if os.name == 'nt' else 'clear')

                    # Dispaly the Customer Menu
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

                    # Prompt the user for their input
                    user_input: str = input('Enter your choice: ')

                    # Clear the screen after we get our input
                    os.system('cls' if os.name in ('nt', 'dos') else 'clear')

                    # Menu options for the Customer Menu
                    ORDER_HIST = '1'
                    EDIT_USER = '2'
                    EDIT_PASS = '3'
                    EDIT_PAY = '4'
                    EDIT_ADDR = '5'
                    DEL_ACC = 'd'

                    # Display the user's order history
                    if user_input == ORDER_HIST:
                        print(f'---{username}\'s Order History---\n')

                    # Update the user's username (after prompting for the user's password)
                    elif user_input == EDIT_USER:
                        print('---Edit Username---\n')
                        password: str = input('Please enter your password: ')
                        username: str = input('Please enter your new username: ')

                    # Update the user's password (after prompting for the user's password)
                    elif user_input == EDIT_PASS:
                        print('---Edit Password---\n')
                        password: str = input('Please enter your password: ')
                        password: str = input('Please enter your new password: ')

                    # Update the user's payment info (after prompting for the user's password)
                    elif user_input == EDIT_PAY:
                        print('---Edit Payment Info---\n')
                        password: str = input('Please enter your password: ')
                        payment: str = input('Please enter your new payment information: ')

                    # Update the user's address (after prompting for the user's password)
                    elif user_input == EDIT_ADDR:
                        print('---Edit Address Info---\n')
                        password: str = input('Please enter your password: ')
                        address: str = input('Please enter your new address information: ')

                    # Delete the user's account (after having them verify they want to delete it)
                    elif user_input == DEL_ACC:
                        print('---Delete Account---\n')
                        password: str = input('Please enter your password: ')
                        if input('Please type DELETE if you are sure you want to delete your account: ') == 'DELETE':
                            pass

                    # Go back to the main store menu
                    elif user_input == GO_BACK:
                        loop: bool = False
                        continue

                    # Log the user out
                    elif user_input == LOGOUT:
                        loop: bool = False
                        logged_in: bool = False
                        print('Logging Out...\n')
                        sleep(1.5)
                        continue

                    # Exit the program
                    elif user_input == EXIT:
                        loop: bool = False
                        logged_in: bool = False
                        run: bool = False
                        print('Exiting...\n')
                        continue
                continue

            # Display the Inventory Menu and handle interacting with the store's inventory
            elif user_input == INVENTORY_MENU:
                # Loop until we want to go back to the main store menu, log out, or exit the program
                while loop:
                    # Clear the screen before display the Inventory Menu
                    os.system('cls' if os.name == 'nt' else 'clear')

                    # Display the inventory menu and prompt the user for their input
                    cart_prompt: str = ('---Inventory---\n\n'
                                        '1. View Items\n'
                                        '2. Search Item\n'
                                        'r. Go Back\n'
                                        'p. Logout\n'
                                        'q. Exit the Program\n')
                    print(cart_prompt)

                    # Grab the user's input
                    user_input: str = input('Enter your choice: ')

                    # Clear the screen after we have our input
                    os.system('cls' if os.name in ('nt', 'dos') else 'clear')

                    # Menu Options for the Inventory Menu
                    VIEW_ITEMS = '1'
                    SEARCH_ITEMS = '2'

                    # Print the items in the stores inventory
                    if user_input == VIEW_ITEMS:
                        print('---Items---\n')

                    # Search for an item in the store's inventory based on the user's input
                    elif user_input == SEARCH_ITEMS:
                        print('---Search Item---\n')
                        item_name: str = input('Please enter the name of the item: ')

                    # Go back to the store's main menu
                    elif user_input == GO_BACK:
                        loop: bool = False
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue

                    # Log the user out
                    elif user_input == LOGOUT:
                        loop: bool = False
                        logged_in: bool = False
                        print('Logging out...\n')
                        sleep(1.5)
                        continue

                    # Exit the program
                    elif user_input == EXIT:
                        loop: bool = False
                        logged_in: bool = False
                        run: bool = False
                        print('Exiting...\n')
                        continue
                continue

            # Display the item menu and handle the user interacting with items
            elif user_input == ITEM_MENU:
                # Loop until we want to go back to the main store menu, log out, or exit the program
                while loop:
                    # Clear the screen before displaying the Item Menu
                    os.system('cls' if os.name == 'nt' else 'clear')

                    # Display the Item Menu and prompt the user for their input
                    cart_prompt: str = ('---Item---\n\n'
                                        '1. View Items\n'
                                        '2. Search Item\n'
                                        '3. View Name\n'
                                        'r. Go Back\n'
                                        'p. Logout\n'
                                        'q. Exit the Program\n')
                    print(cart_prompt)

                    # Grab the user's input
                    user_input: str = input('Enter your choice: ')

                    # Clear the screen after we have our input
                    os.system('cls' if os.name in ('nt', 'dos') else 'clear')

                    # Menu options for the Item Menu
                    VIEW_ITEMS = '1'
                    SEARCH_ITEMS = '2'
                    VIEW_NAME = '3'

                    # Display the items to the user
                    if user_input == VIEW_ITEMS:
                        print('---Items---\n')

                    # Search for an item based on the user's input
                    elif user_input == SEARCH_ITEMS:
                        print('---Search Item---\n')
                        item_name: str = input('Please enter the name of the item: ')

                    # View the name of an item
                    elif user_input == VIEW_NAME:
                        pass

                    # Go back to the store's main menu page
                    elif user_input == GO_BACK:
                        loop: bool = False
                        continue

                    # Log the user out
                    elif user_input == LOGOUT:
                        loop: bool = False
                        logged_in: bool = False
                        print('Logging Out...\n')
                        sleep(1.5)
                        continue

                    # Exit the program
                    elif user_input == EXIT:
                        loop: bool = False
                        logged_in: bool = False
                        run: bool = False
                        print('Exiting...\n')
                        continue
                continue

            # Log the user out
            elif user_input == LOGOUT:
                logged_in: bool = False
                print('Logging Out...\n')
                sleep(1.5)
                continue

            # Exit the program
            elif user_input == EXIT:
                logged_in: bool = False
                run: bool = False
                print('Exiting...\n')
                continue


if __name__ == '__main__':
    main()