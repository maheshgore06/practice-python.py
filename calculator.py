num1=float(input("enter your first number"))
num2=float(input("enter your second number"))

print("enter 1 for 'addition' ,\n enter 2 for 'subtraction'\n , enter 3 for 'multiplication'\n ,enter 4 for 'division'")

Enter_number=int(input("choice a number from 1 to 10"))

if Enter_number == 1:
    print("addition of your num1 and nu2 :", num1 + num2)

elif Enter_number == 2:
    print("subtraction of your num1 and num2 :",num1 - num2)

elif Enter_number == 3 :
    print("multiplicaion of your num1 and num2 :", num1 * num2)

elif Enter_number == 4 :
    print("division of your num1 and num2 :", num1 % num2)

else :
    print("invalid input")
