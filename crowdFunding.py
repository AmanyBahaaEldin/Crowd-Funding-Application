from loginAndRegister import *
from projectMenu import *


def viewMainMenu():
    while(True):
        print("------------------- Crowd Fundraising App -------------------")
        print("1) Login                       2) Register")

        response=input("--> ")
        response=validateNum(response)
        if response ==1:
            userID =login()
            viewProjectMenu(userID)
        elif response ==2:
            register()
            os.system('cls')
        else:
            print("Invalid choice")


viewMainMenu()