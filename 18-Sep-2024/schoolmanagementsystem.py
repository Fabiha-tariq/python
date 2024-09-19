class User:
    def __init__(self, username, password, designation, id, subject):
        self.username = username
        self.password = password
        self.designation = designation
        self.id = id
        self.subject = subject

    def login(self, username, password):
        return self.username == username and self.password == password


class Student:
    def __init__(self, std_Fname, std_Lname, std_username, std_password, std_age, std_subject):
        self.std_Fname = std_Fname
        self.std_Lname = std_Lname
        self.std_username = std_username
        self.std_password = std_password
        self.std_age = std_age
        self.std_subject = std_subject


# Creating User objects
check1 = User("fabihatariq04", "04jan2006", "teacher", 1, "english")
check2 = User("fabihatariq", "04jan", "teacher", 2, "urdu")
check3 = User("fabiha", "pass", "teacher", 3, "math")
check4 = User("tariq", "teacher12", "teacher", 4, "biology")

users = [check1, check2, check3, check4]

# List to store registered students
students = []

CheckUser = input("Enter Username: ")
CheckPassword = input("Enter Password: ")

logged_in = False

# Loop to check if the user credentials are correct
for user in users:
    if user.login(CheckUser, CheckPassword):
        print("Login successful! Welcome!!")
        logged_in = True
        print("Your Subject Is:", user.subject)

        # Provide the user with action options
        action = str(input("""Choose an Option:
                            a. Register a Student
                            b. Logout: """))

        # Register a student if the action is "a"
        if action == "a":
            new_student = Student(
                str(input("Enter First Name: ")),
                str(input("Enter Last Name: ")),
                str(input("Enter Username: ")),
                str(input("Enter Password: ")),
                int(input("Enter Age: ")),
                str(input("Enter Subject: "))
            )
            students.append(new_student)
            print(f"Student {new_student.std_Fname} {new_student.std_Lname} registered successfully!")
        elif action == "b":
            print("Logging out...")
            break
        else:
            print("Invalid option!")

        break  # Exit loop after successful login

# If the user is not logged in
if not logged_in:
    print("Login failed. Invalid credentials.")
