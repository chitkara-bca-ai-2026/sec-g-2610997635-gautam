tuition_fee = float(input("Enter the tuition fee: "))
lab_fee = float(input("Enter the lab fee: "))
Library_fee = float(input("Enter the library fee: "))
Exam_fee = float(input("Enter the exam fee: "))
Discount = float(input("Enter the discount: "))

total_fee = tuition_fee + lab_fee + Library_fee + Exam_fee 
discount_amount = Discount
fee_after_discount = total_fee - discount_amount
annual_fee = fee_after_discount * 2
monthly_installment = annual_fee / 12

print("Total fee: ", total_fee)
print("Lab fee: ", lab_fee)
print("Library fee: ", Library_fee)
print("Exam fee: ", Exam_fee)
print("total fee: ", total_fee)
print("Discount amount: ", discount_amount)
print("Fee after discount: ", fee_after_discount)
print("Annual fee: ", annual_fee)
print("Monthly installment: ", f"{monthly_installment:.2f}")

# tuition fee = 25000
# lab = 5000
# libarary = 2000
# exam = 3000
# discount = 2500

