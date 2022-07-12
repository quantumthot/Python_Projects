

# Creating the parent class
class User:
    name = 'Chip Putter'
    email = 'BigSwinger69'
    password = 'BestGolferEver'
    account_number = 113
    
# Child classes for the User

class Club_House(User):
    money_spent = 11,130.00
    money_won = 13,000,303.00

class Member(User):
    mailing_adress = '123 Fairway Drive'
    mailing_list = True
    
