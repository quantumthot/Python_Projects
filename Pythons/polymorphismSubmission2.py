# Parent Class User
class User:
    name = "Mark"
    email = "mark@gmail.com"
    password = "1234abcd"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

# Child Class Employee
class Employee(User):
    name = "John"
    email = "John@gmail.com"
    base_pay = 15.00
    department = "Produce"
    pin_number = "3980"

# This is the same method in the parent class "User".
# The difference is that, instead of using entry_password, we're using entry_pin.

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect.")

# Another Child Class Employee
class Manager(User):
    name = "Mary"
    email = "Mary@gmail.com"
    id_badge = "369DW"
    base_pay = 44.00
    department = "Operations"
    Insurance = True



# This is the same method in the parent class "User".
# The difference is that, instead of using entry_password, we're using id_badge.

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_id = input("Enter your ID number: ")
        if (entry_email == self.email and entry_id == self.id_badge):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect.")

# The following code invokes the methods inside each class for User and Employee.

customer = User()
customer.getLoginInfo()

employee = Employee()
employee.getLoginInfo()

manager = Manager()
manager.getLoginInfo()
