from importlib import import_module
from validateRegister import *
from validateLogin import *


############################### Register Function ########################################


def register():
    print("******************** REGISTER ********************")
    firstName = input("Enter your first name: ")
    firstName = validateString(firstName)
    lastName = input("Enter your last name: ")
    lastName = validateString(lastName)
    email = input("Enter your email: ")
    email = validateEmail(email)
    password = input("Enter your password: ")
    confirmPassword = input("Confirm your password: ")
    password = validatePassword(password , confirmPassword)
    phoneNum = input("Enter your phone number: ")
    phoneNum = validatePhoneNumber(phoneNum)
    line_count = 0
    if(exists('csvFiles\\users.csv')):
        print("FILE EXITST!!!!!!!!!!!!1")
        with open('csvFiles\\users.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                line_count +=1

    row = { 'fname' : firstName,
              'lname' : lastName , 
              'email':email , 
              'password' : password , 
              'phone':phoneNum,
              'id':line_count
            }

    header = ['fname' , 'lname' , 'email' , 'password' , 'phone','id']

    with open('csvFiles\\users.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writerow(row)


##################################### Login Function ######################################3


def login():
    print("******************** LOGIN ********************")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    email,password,usrID = checkEntries(email,password)
    return usrID
    

