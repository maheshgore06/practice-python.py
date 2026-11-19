print("---------------- ATM MACHINE ------------------")

name = str(input("Enter your name first:"))
amount = int(input("enter your total amount:"))
bank =str(input("Enter your bank name:"))
print("---------------* WELCOME *---------------------")
print("-------choose your trasaction")


print( "Enter 1 for 'withdraw' ,\n  Enter 2 for 'check balance', \n  Enter 3 for 'bank name' ")

Enter = int(input("choice number from 1 to 3 :"))

if Enter == 1 :
    withdraw = int(input("enter your amount:"))
    if withdraw > 0 and withdraw <=amount:
        amount = amount - withdraw
        print("your remaining balance is:",amount)
    else:
        print("insufficient balance, please check again")
elif Enter == 2 :
 print('check balance plz wait:',amount)

elif Enter == 3 :
 print('bank name: ',bank)

else:
 print("Invalid choice")


   


      
