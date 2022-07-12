#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import re

def reset(i):
    a = input('Please enter your Username (Mobile Number):')
    b = input('Please enter your old password:')
    while(True):
        if b != i.passw:
            print('entered password is wrong')
            b = input('Please enter your old password again:')
        else:
            break
    c = check(input('Please enter your new password:'))
    while(True):
        if i.passw ==c:
            print('You cannot use the password used earlier.')
            c = input('Please enter password again:')
        else:
            break
    i.passw=c
    return i

def check(passw):
    flag = True
    pattern = '^[a-zA-Z]+[@#$]+[0-9]$'
    while(flag):
        if(re.match(pattern, passw)):
            break
        else:
            print("Entered password is in wrong format")
            passw = input('Please start again:')
    return passw
def reseta(i):
    a = input('Please enter your Username (Mobile Number):')
    b = input('Please enter your Date of Birth in DD/MM/YYYY, to confirm:')
    while(True):
        if b != i.dob:
            print('entered dob is wrong')
            b = input('Please enter dob again:')
        else:
            break
    c = check(input('Please enter your new password:'))
    while(True):
        if i.passw ==c:
            print('You cannot use the password used earlier.')
            c = input('Please enter password again:')
        else:
            break
    d = input('Please re-enter your new password:')
    while(True):
        if(c==d):
            i.passw=c
            break
        else:
            print('Password didn\'t match.')
            d = input('Please re-enter password again:')
    return i


    

