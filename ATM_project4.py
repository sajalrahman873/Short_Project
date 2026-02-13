
#ATM (Simple code )

print("_" *15)
print("\n")
print(" Wellcome To My ATM\n ")
print("_" *15)
print("\n")


balance = 50000     

pin = 7252

user_pin = int(input("Enter Your  4 Digit Pin = "))

if user_pin == pin:
    
    print("Menu:")
    
    print("1. Chack Balance ")
    
    print("2. Withdraw Your Balance ")
    
    print("3. Deposite TK ")
    
    print("4. Exit ")
    
    choice = int(input("Enter Your Choice (1 - 4 )  = "))
    
    if choice == 1:
        
        print(f"Your balance = {balance}")
        
    elif choice == 2:
        
        amount = int(input("you want to withdarw = "))
        
        if amount > 0:
            
            if amount < balance:
                
                balance = balance - amount
                
                print(f"Withdraw {amount} TK Successful!")
                
                print(f"Your new {balance}!")
            else :
                print("Not Enough Money ")
                     
        else :
            print("invaliad amount ")
    
    elif choice == 3:
        
        deposite = int(input("Enter ammount to Deposite = ")) 
        
        if deposite > 0:
            
            balance = balance + deposite
            
            print(f"Deposite {deposite} Tk Successful!" )
            
            print(f"Your new {balance} !")
        else:
            print("Eter valiad ammount ")
    
    elif choice == 4:
        
        print("Thanks for using ATM")
        
    
          
    else:
        print("please select right option")
        
        
    
    
else:
    print("Please chack Your pin")