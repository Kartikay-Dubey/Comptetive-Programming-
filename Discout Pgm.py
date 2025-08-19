amount = float(input("Enter the total amount: Rs."))

if amount >= 1000:
    discount = 0.50 
elif amount >= 500:
    discount = 0.30  
else:
    discount = 0  

discount_amount = amount * discount
final_amount = amount - discount_amount

print("Original Amount: Rs.", amount)
print("Discounted Amount: Rs.", discount_amount)
print("Final Amount to Pay: Rs.", final_amount)
