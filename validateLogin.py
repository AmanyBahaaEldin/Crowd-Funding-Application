import csv
import os

################################ Validation Function for Login ####################################


def checkEntries(email , password):
    with open('csvFiles\\users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if (row[2] == email and row[3] == password):
                os.system('cls')
                print(f' ------------- Welcome {row[0]} ^__^ -------------')
                return email , password , row[5]
            else:
                continue
        email = input("\nWrong Entries .... please Enter Your email:\n")
        password = input("\nplease Enter Your password:\n")
        return checkEntries(email,password)
