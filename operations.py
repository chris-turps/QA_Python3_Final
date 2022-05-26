from Comp_payment.payment import *
from Comp_drinkTypes.drinks import *
from Comp_ingredients.hoppers import *
from Comp_transactions.reports import *
from Comp_userInt.userreq import *
from machineStates import *

# Business logic: define which drinks, prices, and components are listed here

americano_obj = Drink("americano",150,10,0,249)
latte_obj = Drink("latte",100,10,50,279)
cappuccino_obj = Drink("cappuccino",75,10,75,299)
espresso_obj = Drink("espresso",50,10,0,219)

drinkList = [americano_obj,latte_obj,cappuccino_obj,espresso_obj]
drinkTypes = [drink.name for drink in drinkList]

# Call a function to offer customer a drink, should return drink.name as userChoice

userChoice = ""
userChoiceIndex = ""
thispay = ""
thistrans = ""

def chooseCoffee():
    global userChoice, userChoiceIndex
    userChoiceIndex, userChoice = userOptions(drinkTypes)
    return state.PAYMENT

# Call a function to process payment, should return transaction details as a string

def userCoughUp():
    userPay(drinkList,userChoiceIndex)
    
def takePayment():
    global thispay, thistrans
    thispay = Payment(userChoice, drinkList[userChoiceIndex].cost)
    thistrans = str(thispay)
    return state.REPORTING

# Call a function to record transactions, should record all transactions in a file (no return)

def busReports():
    recordTrans(thistrans)
    return state.RUNNING

# Call a function to update monitor hopper state




