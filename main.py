# 1
print("1.")
Name = input("Enter Your Name: ")
if (Name == ""):
    print("Hello Stranger!")
else:
    print("Hello",Name)
print()

#2
print("2.")
SetPassword = input("Set a New Password: ")
PasswordAtt = input("Enter the Password: ")
if (SetPassword == PasswordAtt):
    print("Password Correct!")
else:
    print("Password Incorrect Error!")
print()

#3
print("3.")
Password = input("Set a New Password: ")
PassLeng = len(Password)
if (PassLeng < 8 or PassLeng > 12):
    print("Password Range Incorrect")
else:
    print("Password accepted!")
print()

#4
print("4.")
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
Password = input("Set a New Password: ")
Pass = True
for i in range (5):
    if (Password == BAD_PASSWORDS[i]):
        Pass = False
if (Pass == True):
    print("Password accepted!")
else:
    print("Bad Password!")
print()

# 5
print("5.")
correct = False
SetPassword = input("Set a New Password: ")
while (correct == False):
    PasswordAtt = input("Enter the Password: ")
    if (SetPassword == PasswordAtt):
        print("Password Correct!")
        correct = True
    else:
        print("Password Incorrect Try Again!")
print()

#6
print("6.")
for i in range (13):
    calc = i * 7
    print (i,"X 7 =",calc)
print()

#7
print("7.")
Multiplier = int(input("Enter a times table num (0,12): "))
for i in range (13):
    calc = i * Multiplier
    print (i,"X",Multiplier,"=",calc)
print()

#8
print("8.")
