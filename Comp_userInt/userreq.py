import os
import time

def userOptions(drinkTypes):
    userSelection = True
    while userSelection:
        os.system('cls||clear')
        print ('\n' + "Welcome!  Please select the coffee you would like!" + '\n')
        for i in range(0,len(drinkTypes)):
            print("Press " + str(i+1) + " for " + drinkTypes[i])
        print ("Press 0 to cancel" + '\n')
        userSelect = input()
#       userChoiceIndex = int(userSelect)-1
        if userSelect.isnumeric() == False:
            userSelection = True
            print("Hmmmm, here incorrect selection, pls try again!")
            time.sleep(2)
        elif int(userSelect) in range(1,len(drinkTypes)+1):
            userChoiceIndex = int(userSelect)-1
            print ('\n' + "You have selected option " + str(userSelect) + " which is " + drinkTypes[userChoiceIndex] + '\n')
            userChoice = drinkTypes[userChoiceIndex]
            return userChoiceIndex, userChoice
        elif int(userSelect) == 0:
            userSelection = True
        else:
            userSelection = True
            print("Hmmmm, incorrect selection, pls try again!")
            time.sleep(2)




