#!/usr/bin/env python3
# Name: Siddhu Tedla
# Date: Febuary 17th, 2021
# Project: PROJECT 3
from person import Person #imports necesarry packages regarding the date
from datetime import date

# This is the first example of my name and my birthdate
siddhu = Person()#creates subclass with first name wrong
first = "S1ddhu"#I putposely put a 1 instead of an "i" so that you could see how the code catches the problem
middle = "S"#middle initial
last = "Tedla"#lastname
dob = '05/09/2004'#valid DOB

firstname = siddhu.setFirst(first)#sets the .setFIRST to firstname
middleI = siddhu.setMiddle(middle)#sets the .setMiddle to middleI
lastname = siddhu.setLast(last)#sets the .setLast to lastname
dateoB = siddhu.setDOB(dob)#sets .setDOB to dateoB
print(siddhu.FIRST)#prints the firstname
print(siddhu.middleI)#prints the middle initial
print(siddhu.LAST)#prints the lastname
print(siddhu.DOB)#prints the DOB
print(siddhu.getName())#prints the full name

   
# This is another example
bobby = Person()#creates subclass with the middlie initial wrong
first = "Bobby"#firstname
middle = "BR"#this is an on purpose incorrect middle inital that has two characters so you can see how the program catches mistakes
last = "Gy"#last name
dob = '23/12/1978'#valid DOB

firstname = bobby.setFirst(first)#sets the .setFIRST to firstname
middleI = bobby.setMiddle(middle)#sets the .setMiddle to middleI
lastname = bobby.setLast(last)#sets the .setLast to lastname
dateoB = bobby.setDOB(dob)#sets .setDOB to dateoB
print(bobby.FIRST)#prints the firstname
print(bobby.middleI)#prints the middle initial
print(bobby.LAST)#prints the lastname
print(bobby.DOB)#prints the DOB
print(bobby.getName())#prints the full name

# This is another example
Roberto = Person()#creates subclass with the lastname wrong
first = "Roberto"#firstname
middle = "G"#middle initial
last = "Georg3"#I putposely put a 3 instead of an "e" so you could see how the program catches msitakes in the lastname
dob = '17/04/2010'#valid DOB

firstname = Roberto.setFirst(first)#sets the .setFIRST to firstname
middleI = Roberto.setMiddle(middle)#sets the .setMiddle to middleI
lastname = Roberto.setLast(last)#sets the .setLast to lastname
dateoB = Roberto.setDOB(dob)#sets .setDOB to dateoB
print(Roberto.FIRST)#prints the firstname
print(Roberto.middleI)#prints the middle initial
print(Roberto.LAST)#prints the lastname
print(Roberto.DOB)#prints the DOB
print(Roberto.getName())#prints the full name

#his is another example
Sai = Person()#creates subclass with the DOB wrong
first = "Sai"#firstname
middle = "K"#middle initial
last = "Tedla"#last name
dob = 'June/02/2001'#this is an invalid DOB I did this on purpose so you could see how my program catches it.

firstname = Sai.setFirst(first)#sets the .setFIRST to firstname
middleI = Sai.setMiddle(middle)#sets the .setMiddle to middleI
lastname = Sai.setLast(last)#sets the .setLast to lastname
dateoB = Sai.setDOB(dob)#sets .setDOB to dateoB
print(Sai.FIRST)#prints the firstname
print(Sai.middleI)#prints the middle initial
print(Sai.LAST)#prints the lastname
print(Sai.DOB)#prints the DOB
print(Sai.getName())#prints the full name
   
#This is another example
Henry = Person()#creates subclass with nothing wrong
first = "Henry"#firstname
middle = "L"#middle initial
last = "Sroil"#last name
dob = '13/03/1943'#valid DOB

firstname = Henry.setFirst(first)#sets the .setFIRST to firstname
middleI = Henry.setMiddle(middle)#sets the .setMiddle to middleI
lastname = Henry.setLast(last)#sets the .setLast to lastname
dateoB = Henry.setDOB(dob)#sets .setDOB to dateoB
print(Henry.FIRST)#prints the firstname
print(Henry.middleI)#prints the middle initial
print(Henry.LAST)#prints the lastname
print(Henry.DOB)#prints the DOB
print(Henry.getName())#prints the full name