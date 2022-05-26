# from enum import Enum
# from Comp_payment.payment import *
# from Comp_drinkTypes.drinks import *
# from Comp_ingredients.hoppers import *
# from Comp_transactions.reports import *
# from Comp_userInt.userreq import *
from operations import *
from machineStates import *

#class state(Enum):
#    OFF = 1
#    RUNNING = 2
#    PAYMENT = 3
#    REPORTING = 4

cm_state = state.RUNNING

def stateMachine(status):
    match status:
        case state.OFF:
           current_state = state.OFF
        case state.RUNNING:
           current_state = chooseCoffee()
        case state.PAYMENT:
           userCoughUp()
           current_state = takePayment()       
        case state.REPORTING:
         current_state = busReports()
#       case state.MAINTMODE:
#       case state.VALIDATION:
#       case state.STANDBY:
    return current_state

if __name__ == "__main__":  
    stateMachine(state.RUNNING)
      

