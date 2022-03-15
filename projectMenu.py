from tempfile import NamedTemporaryFile
import shutil
from email import header
import validateRegister 
import json 
import pandas as pd
from tabulate import tabulate
import csv
import os 

def buildProject(usrId):
    projectTitle = input("Enter your project title: ")
    details = input("Enter your project details: ")
    target = input("Enter your project target: ")
    startDate = input("Enter your project's start date: ")
    startDate = validateRegister.validateDate(startDate)
    endDate = input("Enter your project's end date: ")
    endDate = validateRegister.validateDate(endDate)
    
    project = {
        "title" : projectTitle,
        "details" : details,
        "target" : target,
        "stDate" : startDate,
        "endDate" : endDate,
        "userID" : usrId
    }
    return project


def createProject(usrId):
    project=buildProject(usrId)
    header =['title' , 'details' , 'target' , 'stDate' , 'endDate','userID']
    
    with open('csvFiles\\projects.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        if os.stat('csvFiles\\projects.csv').st_size == 0:
            writer.writeheader()
        writer.writerow(project)

def viewProjects():
    with open('csvFiles\\projects.csv', 'r') as f:
        reader = csv.DictReader(f)
        df = pd.DataFrame(reader)
        print(tabulate(df, headers = 'keys', tablefmt = 'psql'))

def editProjects(usrID):
    header =['title' , 'details' , 'target' , 'stDate' , 'endDate','userID']
    projectTitle = input("Please Enter the title you want to edit: ")
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    with open('csvFiles\\projects.csv', 'r') as f, tempfile:
        reader = csv.DictReader(f)
        writer = csv.DictWriter(tempfile,fieldnames=header)
        if os.stat(tempfile.name).st_size == 0:
                        writer.writeheader()
        for row in reader:
            if(row['userID'] == usrID):
                if(row['title'] == projectTitle):
                    project=buildProject(usrID)
                    writer.writerow(project)
                    continue
            writer.writerow(row)
    shutil.move(tempfile.name, 'csvFiles\\projects.csv')


def deleteProjects(usrID):
    header =['title' , 'details' , 'target' , 'stDate' , 'endDate','userID']
    projectTitle = input("Please Enter the title you want to delete: ")
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    with open('csvFiles\\projects.csv', 'r') as f, tempfile:
        reader = csv.DictReader(f)
        writer = csv.DictWriter(tempfile,fieldnames=header)
        if os.stat(tempfile.name).st_size == 0:
                        writer.writeheader()
        for row in reader:
            if(row['userID'] == usrID):
                if(row['title'] == projectTitle):
                    print("Deleted Successfully ......")
                    continue
            writer.writerow(row)
    shutil.move(tempfile.name, 'csvFiles\\projects.csv')
    
        



    
def viewProjectMenu(userID):
    while(True):
        print("1) Create Project                       2) View Projects")
        print("3) Edit Project                         4) Delete Project")
        response=input("--> ")
        response=validateRegister.validateNum(response)
        if response ==1:
            createProject(userID)
        elif response ==2:
            viewProjects()
        elif response ==3:
            editProjects(userID)
        elif response ==4:
            deleteProjects(userID)
        else:
            print("Invalid choice")