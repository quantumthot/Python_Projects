class name:
    def __init__(self, firstName, lastName):
        #Intitializing values for future objects created from this class
        self.firstName=firstName
        self.lastName=lastName
    def printName(self):
        print("Hello, I am {0} {1}".format(self.firstName, self.lastName))

#Passing in the actual object values
person=name('Tyler', 'Hatch')
person.printName()
    
