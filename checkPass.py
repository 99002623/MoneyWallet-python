import re
    

def checkPassword(password):
   
    flag = 1

    while True:   
        if (len(password)<8): 
            flag = 1
            break
        elif not re.search("[a-z]", password): 
            flag = 1
            break
        elif not re.search("[A-Z]", password): 
            flag = 1
            break
        elif not re.search("[0-9]", password): 
            flag = 1
            break
        elif not re.search("[_@$]", password): 
            flag = 1
            break
        elif re.search("\s", password): 
            flag = 1
            break
        else: 
            flag = 0
            print("Valid Password") 
            break
  
    if flag == 1: 
        print("Not a Valid Password") 
    
    return flag

def getPassword():
    a_pass = input('Enter Your Password (WITHOUT SPACES): ')

    while checkPassword(a_pass):
        a_pass = input('Enter Your Password (WITHOUT SPACES): ') 
    
    return a_pass