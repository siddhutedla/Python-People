#!/usr/bin/env python3
# Name: Siddhu Tedla
# Date: Febuary 17th, 2021
# Project: PROJECT 3
from datetime import date #imports necesarry packages regarding the date
import datetime

class Person():#This creates the class person
    def __init__(self):#This is the enmpty constructor
      self.FIRST = ""#This is where future firstname values will go
      self.middleI = ""#This is where future middle initial values will go
      self.LAST = ""#This is where future lastname values will go
      self.DOB = ""#This is where future DOB values will go

    def setFirst(self, first) : #this is the setter for the firstname
      if first.isalpha(): #this checks that only alphabetical characters are in the string
        self.FIRST = first#string printed if only alphabetical characters
      else:
        print("Hey no, only letters allowed for the First Name!!")#string printed if non alphabetical cahracters
        
    def setMiddle(self, middle) : #this is the setter for the middle initial
      if middle.isalpha() and len(middle) == 1:#This checks the string to make sure it is alphabetical and also only 1 character long
        self.middleI = middle#this prints the middle initial if it is alphabetical and one character long
      else:
        print("Only 1 Character allowed also no numbers or special cahracters for the Middle Initial!!")#this prints if the middle initial is not alphabetical or not one character long
    def setLast(self, last) :#this is the setter for the lastname
      if last.isalpha():#this checks that only alphabetical characters are in the string
        self.LAST = last#string printed if only alphabetical characters
      else:
        print("Hey no, only letters allowed for the Last Name!!")#string printed if non alphabetical characters
    def setDOB(self, dob) :#this is the setter for the DOB
      isValidDate = True#this checks if inputed date is valid
      try :
        day,month,year = dob.split('/')#this basically says that inputed code gets split into day month and year based on where the '/' is
        datetime.datetime(int(year),int(month),int(day))#this makes the day month and year into integers and checks it
      except ValueError :#this is what happens when the date is invalid
        isValidDate = False#this sets the 'isValidDate' to False
      if(isValidDate) :#if the 'isValidDate' variable is true then it will print the date normally.
        self.DOB = dob#what will be printed if date is correct
      elif any (dob.isalpha() for dob in dob):#this checks if there are any alphabetical characters in the date inputted
        print ("DOB not valid: has to be in dd/mm/yyyy format!!")#this will send an error message saying to fix the format
      else :
        print ("DOB not valid!!")#if neither of those if statements work then it will say that the DOB is invalid
    def getName(self):#creates a name method
      return self.FIRST + " " + self.middleI+ " " + self.LAST + '\n'#This adds the firstname middle initial and lastname all together and even addds a new line at the end
    
