Name = input("Enter the employee Name: ")
print(f" Data type:{type(Name)}")
Emp_id = int(input("Enter the Employee Id: "))
print(f" Data type:{type(Emp_id)}")
salary = float(input("Enter the salary: "))
print(f" Data type:{type(salary)}")
Daparment = str(input("Enter the Deparment: "))
print(f" Data type:{type(Daparment)}")
Active_input = input("Is the Employee Active? (yes/no) ").strip().lower()
is_Active = Active_input == 'yes'
print(f" Data type:{type(is_Active)}")
print("\n---Employee Deatails---" )
print(f"Name       :{Name}")
print(f"Emp_id     :{Emp_id}")
print(f"salary     :{salary}")
print(f"Daparment  :{Daparment}")
print(f"Active     :{is_Active}")

# name = Priya singh
# id = 1002
# salary = 52000.75
# department = IT
# active = yes
