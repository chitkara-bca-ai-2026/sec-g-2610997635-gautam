print(" =" * 30)
print(f"              DATA CONVERSION UTILIY: ")
print(" =" * 30)

Product_name = input("Enter the product Name: ")
Prices = float(input("Enter the Prices      : "))
Quantity = int(input("Enter the Quantity    : "))
total_price =  Prices * Quantity
Amount_str = str(total_price)
print(" -" * 30)
print(f"          TYPE CASTING SUMMARY")
print(" -" * 30)
print(f"{'Variable'}:      {'Value'}         {'python Type'}")
print(" -" * 30)
print(f"Product_name  :{Product_name}   {type(Product_name)}")
print(f"Prices        :{Prices}  {type(Prices)}")
print(f"Quantity      :{Quantity}        {type(Quantity)}")
print(f"total price    :{total_price}    {type(total_price)}")
print(f"Amount_str     :{total_price}    {type(Amount_str)}")
print(" -" * 30)

print("- " * 30)
print(f"\           TAX INVOIVE     ")
print(" -" * 30)
print(f"Product Name   :{Product_name}")
print(f"Prices per unit:Rs. {Prices:}")
print(f"Quantity       :{Quantity}")
print(f"\n------------------------------------------------")
print(f"Invoice Total  :Rs. {total_price:}")
print(" =" * 30)


# p name = Laptop
# price = 45000.50
#qunitity = 2















