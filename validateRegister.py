import re
from os.path import exists


##################### Validation Functions for Registeration ########################
def validateNum(num):
    if num.isdigit():
        return int(num)
    else:
        num = input("\nNOT VALID ... try again: ")
        return validateNum(num)

def validateDate(date):
    dateExp =r'[\d]{1,2}-[\d]{1,2}-[\d]{4}'
    if(re.fullmatch(dateExp,date)):
        return date
    else:
        date=input("\nNOT VALID .. Enter valid date: ")
        return validateDate(date)


def validateString(str):
    if str.isalpha():
        return str
    else:
        str=input("\nNOT VALID ... try again: " )
        return validateString(str)

def validateEmail(email):
    mail=r'\b[A-Za-z0-9._]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(mail,email)):
        return email
    else:
        email=input("\nNOT VALID .. Enter valid email: ")
        return validateEmail(email)

def validatePassword(passWord , confirmPassword):
    if passWord==confirmPassword:
        print("\nPassword Confirmed") 
        return passWord
    else:
        passwd=input("\nNOT CONFIRMED Password ... try again") 
        return validatePassword(passWord , passwd)

def validatePhoneNumber(phoneNumber):
    phone = r'\b01+[0-9]{9}\b'
    if(re.fullmatch(phone , phoneNumber) and len(phoneNumber)==11):
        return phoneNumber
    else:
        phonenum = input("\nNOT VALID .. Enter valid phone number: ")
        return validatePhoneNumber(phonenum)