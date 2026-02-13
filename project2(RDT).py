
print("-" * 15)

print("wellcome")

print("-" * 15)

print("MENU :\n")

print("1. BURGER - 120 TK")
print("2. pasta - 200  TK")
print("3. PIZZA - 400  TK")

item = int(input("choice ITEM (1-3) = "))

quantity = int(input("QANTITY  = "))

if item == 1:
    price = 120
elif item == 2:
    price = 200
elif item == 3:
    price = 400
else:
    price = 0 
if price == 0:
    print("Please select an Item ")
else:
    total = quantity * price    
    if total > 500:
        discount = total * 0.10
    else:
        discount = 0
    total_after_discount = total-discount
    
    tax = total_after_discount * 0.05
    
    final_ammount = total_after_discount + tax
    
    print("Total Price = " , total , "Tk")
    if discount > 0:
        print("discount applied" , discount,"Tk")
    else:
        print("NO discount")
    
    print("Total Tax = " ,tax , 'TK')
        
    print("Final Ammount " , final_ammount , 'TK')