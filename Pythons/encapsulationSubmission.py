
#Creating class
class Protected:
    def __init__(self):
        self._privateVar = 0 #_private denotes protected var. no touchy!

    def getPrivate(self):
        print(self._privateVar)

    def setPrivate(self, private):
        self._privateVar = private

# Object gets the data of the private variable
# the variable was also set to a new value of 5 

obj = Protected()
obj.getPrivate()
obj.setPrivate(5)
obj.getPrivate()
    
