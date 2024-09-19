username = "fabihatariq04"
password = "04jan2006"
balance = 123456

print("Welcome to Fabiha's Bank, Bank of Development and Digitalizing")

CheckUser = str(input("Enter UserName : "))
CheckPass = str(input("Enter Password : "))

if CheckUser == "fabihatariq04" and CheckPass == "04jan2006":
    print("Login Successfully")
    print(".")
    print("..")
    print("...")
    print("....")
    print("...")
    print("..")
    print(".")
    pin = str(input("Enter Your PIN :"))

    if pin == "1234":
        Services = str(input("""Choose a Service:
                     a. Withdraw Money  b. Change PIN
                     c. Balance Enquiry   d. Paying bills

                     Choose a, b, c or d : """))

        if Services == "a":
            withdraw = str(input("""Enter Withdrawing Amount:
                     a. 1000        b. 2000
                     c. 10,000      d. 20,000
                     e. 50,000      f. Other Withdraw Amount

                     Choose a, b, c, d, e or f : """))

            if withdraw == "a":
                result = balance - 1000
                print("Rs 1000 is withdrawn from your account")
                print("Now your current balance is : Rs.", result)
                print("Thank you for using this ATM")
            elif withdraw == "b":
                result = balance - 2000
                print("Rs 2000 is withdrawn from your account")
                print("Now your current balance is : Rs.", result)
                print("Thank you for using this ATM")
            elif withdraw == "c":
                result = balance - 10000
                print("Rs 10,000 is withdrawn from your account")
                print("Now your current balance is : Rs.", result)
                print("Thank you for using this ATM")
            elif withdraw == "d":
                result = balance - 20000
                print("Rs 20,000 is withdrawn from your account")
                print("Now your current balance is : Rs.", result)
                print("Thank you for using this ATM")
            elif withdraw == "e":
                result = balance - 50000
                print("Rs 50,000 is withdrawn from your account")
                print("Now your current balance is : Rs.", result)
            elif withdraw == "f":
                f = int(input("Enter withdraw amount : "))

                if f < balance:
                    result = balance - f
                    print("Rs", f, " is withdrawn from your account")
                    print("Now your current balance is : Rs.", result)
                else:
                    print("Enter a valid amount")
            else:
                print("Choose something from the options!!!")

        elif Services == "b":
            PIN1 = str(input("Enter Your Current ATM PIN : "))
            PIN2 = str(input("Enter Your New PIN : "))
            print("Thank you for using this ATM")

        elif Services == "c":
            print("Your current balance is : Rs.", balance)
            print("Thank you for using this ATM")

        elif Services == "d":
            bill_type = str(input("""Enter the type of bill to pay:
                     a. Electricity    b. Gas
                     c. Internet       d. Water

                     Choose a, b, c or d : """))

            bill_amount = int(input("Enter bill amount: "))

            if bill_amount <= balance:
                balance -= bill_amount
                print(f"Your {bill_type} bill of Rs {bill_amount} has been paid.")
                print(f"Your remaining balance is: Rs. {balance}")
                print("Thank you for using this ATM")
            else:
                print("Insufficient balance to pay the bill.")

        else:
            print("Try Again !!")
else:
    print("Try Again")
