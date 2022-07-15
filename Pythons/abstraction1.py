from abc import ABC, abstractmethod
class rent(ABC):
    def paySlip(self, amount):
        print("Your purchase amount: ",amount)
# This function is telling us to pass in an arguement,
# but wont tell you how or what kind of data it will be
    @abstractmethod
    def payment(self,amount):
        pass

class DebitCardPayment(rent):
# Here we've defined how to implement the
# payment function from its parent paySlip class.
    def payment(self, amount):
        print("Your purchase amount of {} exceeded your $500 limit ".format(amount))


obj = DebitCardPayment()
obj.paySlip("$750")
obj.payment("$750")
