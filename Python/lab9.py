r=int(input("Enter the number of rows: "))
print("1.Pattern Star Triangle")
print("-------------------------------")
rows = 5
for i in range(1,6):
    for j in range(1,(i+1)):
        print("*",end=" ")
    print()    

print("2.Pattern Number Tringle") 
print("-------------------------------")
rows = 5
for i in range(1,6):
    for j in range(1,(i+1)):
        print(j, end=" ")
    print()

print("3.Inverted Star Triangle")
print("-------------------------------")
rows = 5
for i in range(5,0,-1):
    for j in range(1,(i+1)):
        print("*", end=" ")
    print()

print("4. Pryamid")
print("-------------------------------")
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end=" ")

    for k in range(2 * i - 1):
        print("*", end=" ")

    print()