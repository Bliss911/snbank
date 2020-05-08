import random
import sys

choice = input("Enter a choice: ")
if choice == "1":

    with open('staff', 'r') as reader:
        line_username1 = reader.readline()
        main_username1 = line_username1[10:]
        line_password1 = reader.readline()
        main_password1 = line_password1[10:]
        line_email1 = reader.readline()
        main_email1 = line_email1[7:]
        line_name1 = reader.readline()
        main_name1 = line_name1[11:]

        line_username2 = reader.readline()
        main_username2 = line_username2[10:]
        line_password2 = reader.readline()
        main_password2 = line_password2[10:]
        line_email2 = reader.readline()
        main_email2 = line_email2[7:]
        line_name2 = reader.readline()
        main_name2 = line_name2[11:]

    while True:
        username = input('Enter your correct Username: ')
        password = input('Enter your correct password: ')
        if username == main_username1 or username == main_username2 and password == main_password2 or password == \
                main_password2:
            print("\nLogin successful!!!")
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

                random_number = random.randint(1000000000, 9999999999)
                print("Your Account number is " + str(random_number) + "Thanks for Banking with us!")
                with open('customer.txt', 'w') as writer:
                    writer.write('Account Name: ' + account_name)
                    writer.write('Opening balance: ' + opening_balance)
                    writer.write('Account Type: ' + account_type)
                    writer.write('Email: ' + account_email)
                    break
            elif transaction == "2":
                account_number_entered = input('Enter account number: ')
                with open('customer.txt', 'r') as reader:
                    for line in reader.readlines():
                        print(line, end='')
                    break
            elif transaction == "3":
                print('Thanks for banking with us!')
                break
            break
elif choice == '2':
    print("Goodbye!!!")
    sys.exit(1)
