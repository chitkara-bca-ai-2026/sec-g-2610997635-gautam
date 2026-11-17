print(" =" * 30)
print(f"          COTHING STORE BILLING SYSTEM      ")
print(" =" * 30)
name = (input("Enter Customer Name: "))
Garment_Name = (input("Enter Garment Name: "))
Price_of_one_garment = float(input("Enter Prices of one garment: "))
Garment =  int(input("Enter Number of Garment: "))



Total_Amount = Garment * Price_of_one_garment
print(" =" * 30)
print(f"                    BILL")
print(" =" * 30)
print(f" Customer Name           : {name}")
print(f" Garment Name            : {Garment_Name}")
print(f" Price per Unit          : Rs. {Price_of_one_garment}")
print(f" Quantity                : {Garment}")
print(f" Total Amount            : {Total_Amount}")
print(" =" * 30)

# customer name  = Ravi kumar
#garment name = shirt
#one price = 500
#number of garment = 3
