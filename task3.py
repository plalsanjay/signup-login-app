#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from task4 import *
import re


def login(data):
    userid = input('Please enter your Username (Mobile Number):')
    
    
    count =0
    #print(type(data))
    for i in data:
        if(i.contact == userid ):
            track =0
            passw = input('Please enter your password:')
            while(True):
                if track ==2 :
                    print('You have used the maximum attempts of login')
                    print('Please reset the password by entering the below details:')
                    i = reseta(i)
                    data[count]=i
                    print('Your password has been reset successfully.')
                    return data
                if(i.passw == passw):
                    print('You have successfully Signed in')
                    print('Welcome '+ i.name)
                    print('Press enter 1 for Resetting the Password')
                    print('Press enter 2 for Signout')
                    y = int(input())
                    if y == 1:
                        i = reset(i)
                        data[count]=i
                        print('Your password has been reset successfully.')
                        return data
                        
                    elif y == 2:
                        print('You have been logged out successfully')
                        return data
                        
                else:
                    print('Wrong Password')
                    passw = input('Please enter password again:')
                track = track +1
        else:
            print('Userid not found')
            return data
        count = count+1

