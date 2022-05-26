import datetime
import time

class Payment:
    def __init__(self
        , drink_name
        , cost_p
    ):
        self.name = drink_name
        self.time = datetime.datetime.now()
        self.cost = cost_p

    def __str__(self):
        return f'Name: {self.name}, Time: {self.time}, Cost: {self.cost}'

def userPay(drinkList, userChoiceIndex):
    userPayment = True
    while userPayment:
        print ("Please pay " + str(drinkList[userChoiceIndex].cost) + "p by tapping on the card reader ( hit 'p' to simulate simulate)" + '\n')
        userTouch = input()
        if userTouch == 'p':
            print ('\n' + "Payment accepted, thank you!" + '\n')
            userPayment = False
            time.sleep(2)
        else:
           print('\n' + "Please pay for your coffee" + '\n')


