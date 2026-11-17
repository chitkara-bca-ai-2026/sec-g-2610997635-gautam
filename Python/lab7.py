print("= " * 40)
print("                 CELENDER VERIFICATION SYSTEM")
print("= " * 40)
year = int(input("Enter year: "))
if year <=0:
    print("Error: Year canot be 0 or negative!")
else:    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
       print("status: LEAP YEAR")
       print("Days in Year: 366 days")
       print("Days in february: 29 days")

       if year % 100 != 0:
          print("Reson: Divisible by 4 and not a centur year")
       else:
          print("Reson: century year Divisible by 4000")
    else:
        print("status: COMMON YEAR")
        print("Days in Year: 365 days")
        print("Days in febuary: 28 days")
        print("Reson: Not divisible by 4(or a century year not divisible by 400)") 
print("-" * 35)


# year = 2024
