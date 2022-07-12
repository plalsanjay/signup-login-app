#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
import datetime
from task3 import *

class Signup:
    def __init__(self, name = None, contact = None, email = None, dob = None, passw = None):
        self.name = name
        self.contact = contact
        self.email = email
        self.dob = dob
        self.passw = passw
    def ck(self):
        print(self.name)
        print(self.contact)
        print(self.email)
        print(self.dob)
        print(self.passw)

data = []


while(True):
    print('Please enter 1 for Sign up.')
    print('Please enter 2 for Log in.')
    print('Please enter 3 for Exit.')
    x = int(input())
    if x == 3:
        print('Thank You for using the Application.')
        break
    elif x == 1:
        flag = True
        name = str(input('Please enter your name:'))
        pattern= '^0[0-9]{9}'
        contact = input('Please enter your mobile number:')
        while(flag):
            #print(re.match(pattern, contact))
            if(re.match(pattern, contact) and len(contact)==10):
                #print('l')
                break
            else:
                if(len(contact)<10):
                    print('Entered number has less than 10 digits.')
                    contact = input('Please start again:')
                elif(len(contact)>10):
                    print('Entered number has greater than 10 digits.')
                    contact = input('Please start again:')
                else:
                    if(re.match(pattern, contact)):
                        #print('k')
                        continue
                    else:
                        print('Entered number does not start with 0')
                        contact = input('Please start again')
        email = input('Please enter email id:')
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        flag = True
        while(flag):
            if(re.match(pattern, email)):
                break
            else:
                print("Entered email is in wrong format")
                email = input('Please start again:')
        flag = True
        pattern = '^[a-zA-Z]+[@#$]+[0-9]$'
        passw = input('Please enter your Password:')
        while(flag):
            if(re.match(pattern, passw)):
                break
            else:
                print("Entered password is in wrong format")
                passw = input('Please start again:')
        passc = input('Please confirm your Password:')

        while(flag):
            if(passw==passc):
                break
            else:
                print('Your passwords are not matching')
                passc = input('Please start again:')
        dob = input('Please Enter your Date of Birth # DD/MM/YYYY (No Space):')
        while(True):

            day, month, year = dob.split('/')

            isValidDate = True
            today = datetime.date.today()
            try:
                datetime.datetime(int(year), int(month), int(day))
            except ValueError:
                isValidDate = False

            if(isValidDate):
                if(today.year - int(year) >=18):
                    break
                else:
                    print('User Should be atleast 18 years older.')
                    #print('exit code 0')
                    dob = input('Please start again:')
            else:
                print("You have entered the Date of Birth in invalid format.")
                dob = input('Please start again:')
        p = Signup()
        p.name = name
        p.contact=contact
        p.email = email
        p.dob =dob 
        p.passw = passw
        data.append(p)
        #p.ck()
        print('You have Successfully Signed up.')
    elif x == 2:
        data = login(data)
        
        

