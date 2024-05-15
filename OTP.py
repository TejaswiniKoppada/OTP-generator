import random
generatorotp=random.randint(0000,1000)
username=input("Username:")
print('Hello..!',username)
print('Here is your otp for login',generatorotp)
password=input("Enter the otp to login:")

if password==str(generatorotp):
    print('login successfull')
    
elif password!=str(generatorotp):
    print('login failed')