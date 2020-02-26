# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:45:32 2019

@author: 1171101679
"""
    
    
x = 0
symbol = "!@#$%^&*"
while (x == 0):
    u = str(input("Please key in the username.\nUsername:"))
    if (u.isalpha()==False):
        print("Username must be alphabetical")
    else:
        x = 1
        
while (x == 1):
    p = str(input("Password:"))
    if (any(y.isupper() for y in p )) and (any(y.islower( )for y in p)) and (any(y.isdigit()for y in p) and (any(y in symbol for y in p)) and len(p)>=10 and len(p)<=30):
        print("Username and Password is valid.")
    else:
        print("Password must satisfy the below requirement.")
        print("1.AT LEAST 1 upper case.\n2.AT LEAST 1 lower case.\n3.AT LEAST 1 number.\n4.AT LEAST 1 symbol.\n5.MINIMUM length of 10 characters.\n6.MAXIMUM length of 30 characters")
        x = 1
    
    