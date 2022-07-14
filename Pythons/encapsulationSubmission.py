
#Creating Private class
class Private:
    def __init__(self):
        self.__privateVar = 0 #_private denotes protected 

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

# Object gets the data of the private variable
# the variable was also set to a new value of 5 

obj = Private()
obj.getPrivate()
obj.setPrivate(5)
obj.getPrivate()


#Creating Protected class    
class Protected:
    def __init__(self):
        self._protectedVar = 1

    def getProtected(self):
        print(self._protectedVar)

    def setProtected(self, protected):
        self._protectedVar = protected

# Object gets the data of the protected variable
# the variable was also set to a new value of 6 

obj = Protected()
obj.getProtected()
obj.setProtected(6)
obj.getProtected()



