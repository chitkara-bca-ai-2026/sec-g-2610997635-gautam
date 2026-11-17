print("= " * 30)
print("         SCHOOL RESULT PROCESSING")
print("= " * 30)
Student_Name = input("Enter the Student Name: ")
Roll_Number = int(input("Enter the Roll Number: "))
print(f"Student Name :{Student_Name}")
print(f"Roll Number  :{Roll_Number}")

print("--- Enter Marks for 5 Subject (0-100) --- ")
sub1 = int(input(f"Enter Mark for Subject 1 : "))
sub2 = int(input(f"Enter Marks for Subject 2: "))
sub3 = int(input(f"Enter Marks for Subject 3: " ))
sub4 = int(input(f"Enter Marks for Subject 4: "))
sub5 = int(input(f"Enter Marks for Subject 5: "))

print("= " * 30)
print(f"           STUDENT REPORT CARD")
print(f" Student Name : {Student_Name:}")
print(f" Roll Number  : {Roll_Number:}")
print("- " * 30)

Total_marks = float(sub1) + float(sub2) + float(sub3) + float(sub4) + float(sub5)

percentage = (Total_marks / 500) * 100

if percentage >=40:
    result = "PASS"
else:
    result = "FAIL" 
   

if percentage >= 90:
    grade = "A+"
    remark = "outstanding"
elif percentage >=80:
    grade = "A"
    remark = "Excellent"
elif percentage >=70:
    grade = "B"
    remark = "Very Good"
elif percentage >=60:
    grade = "C"
    remark = "Good"
elif percentage >=50:
    grade = "D"
    remark = "Satisfactory"
elif percentage >=40:
    grade = "E"
    remark = "Pass"
else:
    grade = "F"
    remark = "Fail"                

print (f"Total marks:{Total_marks} /500.0")
print(f"Percentage: {percentage:.2f}%")
print(f"Result    : {result}")  
print(f"Grade     : {grade}")
print(f"Remarks   : {remark}")
print("= " * 30)

#name = Aarav Sharma
#roll = 1024
#s1 = 85
#s2 = 92
#s3 = 78
#s4 = 88
#s5 = 90




