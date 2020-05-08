choice = input("Enter a choice: ")
if choice == "1":
    username = input('Enter your correct Username: ')
    password = input('Enter your correct password: ')
    with open('staff', 'r') as reader:
        line_username = reader.readline()
        main_username = line_username[10:]
        line_password = reader.readline()
        main_password = line_password[10:]
        line_email = reader.readline()
        main_email = line_email[7:]
        line_name = reader.readline()
        main_name = line_name[11:]

    while username != main_username and password != main_password:
        print("Incorrect username or password! ")
        username = input('Enter your correct Username: ')
        password = input('Enter your correct password: ')

    print("""
1. Create New Bank Account
2. Check Account details
3.  Logout
    """)

    transaction = input('Make a choice of transaction: ')

    while True:
        if transaction == "1":
            print('The following details are needed:-')
            account_name = input('Please enter your account name: ')
            opening_balance = input('What would be your opening balance: ')
            account_type = input('Please enter the type of account: ')
            account_email = input('Enter your preferred account email ID: ')

            with open('customer.txt', 'w') as writer:
                writer.writelines()