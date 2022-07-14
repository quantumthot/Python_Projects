
#Creating Private class
class Private:
    def __init__(self):
        self.__private_protectedVar = 0 #_private denotes protected 

    def getPrivate(self):
        print(self.__private_protectedVar)

    def setProtected(self, private):
        self.__private_protectedVar = private

# Object gets the data of the private variable
# the variable was also set to a new value of 5 

obj = Private()
obj.getPrivate()
obj.setProtected(5)
obj.getPrivate()


