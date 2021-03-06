import datetime
from random import randint
import sys

def loginloop():
    login = str(input("For Staff login type 'yes'. To Close app type 'no'. \n"))
    if login == "yes":

        file = open("staff.txt","r")
        for row in file:
            field = row.split(",")
            username = field[0]
            password = field[1]

            print("Please enter your details to log in")
            username1 = input("Please enter your username: ")
            password1 = input("Please enter your password: ")

            while username1 != username or password1 != password:
                print("incorrect username or password, Try again")
                username1 = input("Please enter your username: ")
                password1 = input("Please enter your password: ")

            else:
                file = open("session.txt", "a")
                file.write(username)
                file.write(",")
                file.write(password)
                file.write(",")
                file.write(datetime.datetime.now().ctime())
                file.write("\n")
                file.close()
                print("You have successfully logged in! and your session has been saved.", username)

                def createloop():
                    print("Type '1' to create bank account, type '2' to check account details or type '3' to logout" )
                    option = input("Type your option:")
                    if option == "1":
                        print("Please enter minimum of four characters (A-Z) as Customer's fullname")
                        customerName = input()
                        while len(customerName) < 4:
                            print("Entry does not meet requirement, re-enter a minimum of four characters (A-Z) as Customer's fullname")
                            customerName = input()

                        print('Please enter minimum of three digits (A-Z) as Customer account balance')
                        accountBalance = input()
                        while len(accountBalance) < 3:
                            print('Entry does not meet requirement, re-enter a minimum of nine digits (A-Z) as account balance')
                            accountBalance = input()

                        print('Please enter minimum of three characters (A-Z) as account type')
                        accountType = input()
                        while len(accountType) < 3:
                            print('Entry does not meet requirement, re-enter minimum of three characters (A-Z) as account type')
                            accountType = input()

                        print('Please enter minimum of six characters (A-Z) as email address')
                        email = input()
                        while len(email) < 6:
                            print('Entry does not meet requirement, re-enter minimum of six characters (A-Z) as email address')
                            email = input()
                        accountNumber = str(2000000000+randint(1000000, 9999999))
                        file = open("customer.txt", "a")
                        file.write(customerName)
                        file.write(",")
                        file.write(accountBalance)
                        file.write(",")
                        file.write(accountType)
                        file.write(",")
                        file.write(email)
                        file.write(",")
                        file.write(accountNumber)
                        file.write(",")
                        file.write(datetime.datetime.now().ctime())
                        file.write("\n")
                        file.close()
                        print("The customer details has been saved and his/her NUBAN number is: ",accountNumber)
                        create_again = str(input("To create another account, type 'yes'. To return to the login page type 'no'. \n"))
                        if create_again == "yes":
                            createloop()
                    elif option == "2":
                        print("please enter account number to search for a customer details")
                        lookup = input()
                        with open('customer.txt', 'r') as myFile:
                            for num, line in enumerate(myFile, 1):
                                if lookup in line:
                                    print('This is the details of the customer:', line)
                                    createloop()
                    elif option == "3":
                        loginloop()
                    else:
                        print("Incorrect entry, type '1' to create bank account, type '2' to check account details or type '3' to logout" )
                        createloop()
                createloop()
    elif login == "no":
        sys.exit("The application is now closed")
loginloop()

#file.close()

