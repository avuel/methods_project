def main():
    import os
    from Customer import Customer
    from Cart import Cart
    from Inventory import Inventory
    from Item import Item
    from time import sleep

    logged_in: bool = False
    run: bool = True
    customer: Customer = None
    inventory: Inventory = None
    cart: Cart = None

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
                username: str = input("Enter your username: ")
                password: str = input("Enter your password: ")

                # Create a customer object of the specified username and password
                customer: Customer = Customer(username, password)

                # Attempt to log the user in and get the result
                logged_in: bool = customer.login()
                if logged_in is False:
                    print('\nFailed to log in!')

                elif logged_in is True:
                    print('\nSuccessfully logged in!')
                    inventory: Inventory = Inventory()
                    cart: Cart = Cart(customer.getUsername())
                    inventory.load()
                    cart.load()

                # Sleep to let the user read the output and then clear the menu
                sleep(1.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                continue

            # If we want to create an account, ask for a username and password (and validate the account can be made)
            elif user_input == CREATE_ACCOUNT:
                print('---Create Account---\n')
                
                # Get the user's input and create a Customer object
                username: str = input("Enter your username: ")
                password: str = input("Enter your password: ")

                if username == "" or password == "":
                    print("Account credentials cannot be blank.")
                    sleep(1.5)
                    # Clear the screen after we get our input
                    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                    break

                # Create a customer object of the specified username and password
                customer: Customer = Customer(username, password)

                # Try to create the accoutn and output the result
                create_account: bool = customer.create_account()
                if create_account is False:
                    print('\nFailed to create account!')

                elif create_account is True:
                    print('\nSuccessfully created account!')

                # Sleep to let the user read the output and then clear the menu
                sleep(1.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                continue

            # Exit the program
            elif user_input.lower() == EXIT:
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
                                        '2. Add an Item to the Cart\n'
                                        '3. Remove an Item from the Cart\n'    
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
                    VIEW_CART: str = '1'
                    ADD_ITEM: str = '2'
                    REMOVE_ITEM: str = '3'
                    CHECKOUT: str = '4'

                    # Display the user's cart
                    if user_input == VIEW_CART:
                        while (user_input.lower() != GO_BACK):
                            print(f"---{customer.getUsername()}\'s Cart---\n")
                            cart_copy, total = cart.getCart()
                            for row in cart_copy:
                                item: Item = row
                                print(f"{item}Quantity: {cart_copy[item]}\n")
                            print(f"Total cost: {total:.2f}\n")
                            user_input: str = input('Enter r to go back to the Inventory Menu: ')

                    # Attempt to add the user specified item to their cart
                    elif user_input == ADD_ITEM:
                        # Prompt the user for the name of the item they wish to add to their cart
                        print('---Add Item---\n')
                        name: str = input('Please enter the name of the item: ')
                        items: list[Item] = inventory.getItem(name)
                        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                        stock: int = 0

                        # Print the list of items in the inventory with the specified item name
                        print('---Add Item---\n')
                        if items is not None:
                            for row in items:
                                item: Item = row
                                stock: int = inventory.getStock(item.getName(), item.getCategory())
                                print(item, end='\b')
                                print(f"Quantity: {stock}", end='\n\n')

                        # Print that there are no items of the item name in the inventory
                        else:
                            print(f"{name} is not in inventory")
                            sleep(1.5)
                            continue
                        
                        # Get the category we want to add to the cart for the item and check if its in the inventory
                        category: str = input('Please enter the category of the item: ')
                        category_exists: bool = False
                        for row in items:
                            item: Item = row
                            if item.getCategory() == category:
                                category_exists: bool = True
                                break
                        
                        # Check if the category exists
                        if category_exists:
                            # Try to find the item in the inventory, ask for a quantity to add, and try to add it to cart
                            for row in items:
                                item: Item = row
                                if item.getCategory() == category:
                                    quantity: str = input(f"Please enter the quantity of the item {name} you want to purchase: ")
                                    try:
                                        quantity: int = int(quantity)
                                        if stock < quantity:
                                            print(f"\nThere are only {stock} {name} {category} in stock")
                                            break
                                        elif quantity < 1:
                                            print(f"\n{quantity} is an invalid quantity to add to your cart")
                                        else:
                                            cart.addItem(item, quantity)
                                            print(f"\nSuccessfully added {quantity} of the {name} {category} to your cart")
                                    except TypeError:
                                        print(f"\n{quantity} is not a valid quantity")
                                    except ValueError:
                                        print(f"\n{quantity} is not a valid quantity")

                        # Print out the category that we want to buy does not exist for that item
                        else:
                            print(f"\nThere is not an item called {name} of the category {category} in the inventory")

                        sleep(1.5)
                        continue

                    # Attempt to remove the user specified item from their cart
                    elif user_input == REMOVE_ITEM:
                        # Prompt the user for the name of the item they wish to remove from their cart
                        print('---Remove Item---\n')
                        name: str = input('Please enter the name of the item: ')
                        items: list[Item] = cart.getItem(name)
                        os.system('cls' if os.name in ('nt', 'dos') else 'clear')

                        # Print the list of items in the cart with the specified item name
                        print('---Remove Item---\n')
                        if items is not None:
                            for row in items:
                                item: Item = row
                                stock: int = inventory.getStock(item.getName(), item.getCategory())
                                print(item, end='\b')
                                print(f"Quantity: {stock}", end='\n\n')

                        # Print that there are no items of the item name in the cart
                        else:
                            print(f"{name} is not in the cart")
                            sleep(1.5)
                            continue
                            
                        # Get the category we want to add to the cart for the item and check if its in the inventory
                        category: str = input('Please enter the category of the item: ')
                        category_exists: bool = False
                        for row in items:
                            item: Item = row
                            if item.getCategory() == category:
                                category_exists: bool = True
                                break

                        # Check if there is an item with the right name and category in the cart
                        if category_exists:
                            # Find the item we want to remove and try to remove it from the cart
                            for row in items:
                                item: Item = row
                                if item.getCategory() == category:
                                    if cart.removeItem(name, category):
                                        print(f"\nSuccessfully removed {name} from your cart")
                                    else:
                                        print(f"\nFailed to remove {name} from your cart")

                        # Print out the category that we want to buy does not exist for that item
                        else:
                            print(f"There is not an item called {name} of the category {category} in the inventory")
                        sleep(1.5)
                        continue

                    # Check the user out
                    elif user_input == CHECKOUT:
                        # Check the user out
                        while user_input.lower() != GO_BACK:
                            os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                            print(f"---{customer.getUsername()}\'s Receipt---\n")
                            # Print out the users receipt
                            cart_copy, total = cart.getCart()
                            for row in cart_copy:
                                item: Item = row
                                print(f"{item}Quantity: {cart_copy[item]}\n")
                            print(f"Total cost: {total:.2f}\n")
                            user_input: str = input('Enter y to buy the items or r to go back to the Inventory Menu: ')
                                # Go back to the main store menu
                            if user_input.lower() == 'y':
                                if len(cart_copy) == 0:
                                    print('No items to checkout')
                                    user_input = GO_BACK
                                    sleep(1.5)
                                else:
                                    cart.checkOut(customer.getAddress(), total)
                                    print(f"Purchase Successful")
                                    inventory: Inventory = Inventory()
                                    inventory.load()
                                    sleep(1.5)
                                    user_input = GO_BACK
                                    
                            elif user_input.lower() == 'r':
                                user_input = GO_BACK
                        continue

                    
                    # Go back to the main store menu
                    elif user_input.lower() == GO_BACK:
                        loop: bool = False
                        continue

                    # Log the user out
                    elif user_input.lower() == LOGOUT:
                        loop: bool = False
                        logged_in: bool = False
                        print('Logging Out...\n')
                        sleep(1.5)
                        continue

                    # Exit the program
                    elif user_input.lower() == EXIT:
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
                    ORDER_HIST: str = '1'
                    EDIT_USER: str = '2'
                    EDIT_PASS: str = '3'
                    EDIT_PAY: str = '4'
                    EDIT_ADDR: str = '5'
                    DEL_ACC: str = 'd'

                    # Display the user's order history
                    if user_input == ORDER_HIST:
                            
                        while (user_input.lower() != GO_BACK):

                            orders = customer.getOrderHistory()

                            # If the list is empty 
                            if len(orders) == 0:
                                print("You have no exisitng orders.")
                                sleep(2)
                                # Clear the screen after we get our input
                                os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                                break

                            else:
                                print("-----Order history-----")
                                print('r. Go Back\n')

                                for row in orders:
                                    print(f"{row[1]}\'s Order: \tTotal: ${float(row[2]):.2f} \t\tShipping address: {row[3]}")
                                    # row[1] + "'s ","Order: \tTotal: ", "$", total, "\tShipping address: ", row[3]

                                user_input = input("\nEnter \'r\' to go back: ")

                    # Update the user's username (after prompting for the user's password)
                    elif user_input == EDIT_USER:
                        print('---Edit Username---\n')
                        password: str = input('Please enter your password: ')
                        username: str = input('Please enter your new username: ')

                        # If the user did not enter a valid password send the back to the menu
                        if password != customer.getPassword():
                            print("Action failed. Please check credentials.")
                            sleep(1.5)
                            # Clear the screen after we get our input
                            os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                            break

                        # If the user did not enter a valid username send them back to the menu
                        elif username == "":
                            print("Action failed. username cannot be blank.")
                            sleep(1.5)
                            # Clear the screen after we get our input
                            os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                            break

                        # If the user enter a valid password delete their account
                        else:
                            customer.setUsername(username)
                            continue

                    # Update the user's password (after prompting for the user's password)
                    elif user_input == EDIT_PASS:
                        print('---Edit Password---\n')
                        password: str = input('Please enter your password: ')
                        newPassword: str = input('Please enter your new password: ')

                        # If the user did not enter a valid password send the back to the menu
                        if password != customer.getPassword():
                            print("Action failed. Please check credentials.")
                            sleep(1.5)
                            # Clear the screen after we get our input
                            os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                            break

                        # If the user did not enter a valid password send them back to the menu
                        elif newPassword == "":
                            print("Action failed. password cannot be blank.")
                            sleep(1.5)
                            # Clear the screen after we get our input
                            os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                            break

                        # If the user enter a valid password delete their account
                        else:
                            customer.setPassword(newPassword)
                            continue

                    # Update the user's payment info (after prompting for the user's password)
                    elif user_input == EDIT_PAY:
                        print('---Edit Payment Info---\n')
                        password: str = input('Please enter your password: ')
                        payment: str = input('Please enter your new payment information: ')

                        # If the user did not enter a valid password send the back to the menu
                        if password != customer.getPassword():
                            print("Action failed. Please check credentials.")
                            sleep(1.5)
                            # Clear the screen after we get our input
                            os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                            break

                        # If the user did not enter valid payment info send them back to the menu
                        elif payment == "":
                            print("Action failed. payment info cannot be blank.")
                            sleep(1.5)
                            # Clear the screen after we get our input
                            os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                            break

                        # If the user enter a valid password delete their account
                        else:
                            customer.setPaymentInfo(payment)
                            continue

                    # Update the user's address (after prompting for the user's password)
                    elif user_input == EDIT_ADDR:
                        print('---Edit Address Info---\n')
                        password: str = input('Please enter your password: ')
                        address: str = input('Please enter your street address: ')
                        city: str = input('Please enter your city: ')
                        state: str = input('Please enter your state: ')
                        zipCode: str = input('Please enter your zip: ')

                        # If the user did not enter a valid password send the back to the menu
                        if password != customer.getPassword():
                            print("Action failed. Please check credentials.")
                            sleep(1.5)
                            # Clear the screen after we get our input
                            os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                            break

                        # If the user did not enter a valid password send them back to the menu
                        elif address == "" or city == "" or state == "" or zipCode == "":
                            print("Action failed. address information cannot be blank.")
                            sleep(1.5)
                            # Clear the screen after we get our input
                            os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                            break

                        # If the user enter a valid password delete their account
                        else:
                            customer.setAddress(address)
                            customer.setCity(city)
                            customer.setState(state)
                            customer.setZip(zipCode)
                            continue

                    # Delete the user's account (after having them verify they want to delete it)
                    elif user_input.lower() == DEL_ACC:
                        print('---Delete Account---\n')
                        password: str = input('Please enter your password: ')

                        # If the user did not enter a valid password send the back to the menu
                        if password != customer.getPassword():
                            print("Action failed. Please check credentials.")
                            sleep(1.5)
                            # Clear the screen after we get our input
                            os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                            break
                        # If the user enter a valid password delete their account
                        else:
                            if input('Please type DELETE if you are sure you want to delete your account: ') == 'DELETE':
                                customer.delete_account()
                                logged_in: bool = False
                                loop: bool = False
                                continue
                            else:
                                break

                    # Go back to the main store menu
                    elif user_input.lower() == GO_BACK:
                        loop: bool = False
                        continue

                    # Log the user out
                    elif user_input.lower() == LOGOUT:
                        loop: bool = False
                        logged_in: bool = False
                        print('Logging Out...\n')
                        sleep(1.5)
                        continue

                    # Exit the program
                    elif user_input.lower() == EXIT:
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
                                        '2. View Items of Category\n'
                                        '3. Search Item\n'
                                        'r. Go Back\n'
                                        'p. Logout\n'
                                        'q. Exit the Program\n')
                    print(cart_prompt)

                    # Grab the user's input
                    user_input: str = input('Enter your choice: ')

                    # Clear the screen after we have our input
                    os.system('cls' if os.name in ('nt', 'dos') else 'clear')

                    # Menu Options for the Inventory Menu
                    VIEW_ITEMS: str = '1'
                    SEARCH_CATEGORY: str = '2'
                    SEARCH_ITEMS: str = '3'

                    # Print the items in the stores inventory
                    if user_input == VIEW_ITEMS:
                        while (user_input.lower() != GO_BACK):
                            print('---Items---\n')
                            inv: dict = inventory.getInv()
                            for row in inv:
                                item: Item = row
                                print(f"{item}Stock: {inv[item]}\n")
                            print()
                            user_input: str = input('Enter r to go back to the Inventory Menu: ')

                    elif user_input == SEARCH_CATEGORY:
                        while (user_input.lower() != GO_BACK):
                            print('---View Category--\n')
                            category: str = input('Please enter which category: ')
                            os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                            print(f"---{category}---\n")
                            inv: dict = inventory.getInv()
                            for item in inv:
                                if item.getCategory() == category:
                                    print(f"{item}Stock: {inv[item]}\n")
                            print()
                            user_input: str = input('Enter r to go back to the Inventory Menu: ')

                    # Search for an item in the store's inventory based on the user's input
                    elif user_input == SEARCH_ITEMS:
                        while (user_input.lower() != GO_BACK):
                            print('---View Item---\n')
                            name: str = input('Please enter the name of the item: ')
                            items = inventory.getItem(name)
                            os.system('cls' if os.name in ('nt', 'dos') else 'clear')

                            print('---View Item---\n')
                            if items is not None:
                                for row in items:
                                    item: Item = row
                                    print(item)
                                user_input: str = input('Enter r to go back to the Inventory Menu: ')

                            else:
                                print(f"{name} was not found")
                                sleep(1.5)
                                user_input = GO_BACK

                    # Go back to the store's main menu
                    elif user_input.lower() == GO_BACK:
                        loop: bool = False
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue

                    # Log the user out
                    elif user_input.lower() == LOGOUT:
                        loop: bool = False
                        logged_in: bool = False
                        print('Logging out...\n')
                        sleep(1.5)
                        continue

                    # Exit the program
                    elif user_input.lower() == EXIT:
                        loop: bool = False
                        logged_in: bool = False
                        run: bool = False
                        print('Exiting...\n')
                        continue
                continue

            # Log the user out
            elif user_input.lower() == LOGOUT:
                logged_in: bool = False
                print('Logging Out...\n')
                sleep(1.5)
                continue

            # Exit the program
            elif user_input.lower() == EXIT:
                logged_in: bool = False
                run: bool = False
                print('Exiting...\n')
                continue


if __name__ == '__main__':
    main()
