# write a function to calculate  the dicount of a price
def  calculate_discount(price, discount_percent):
#	#takes input from user
#	price = float(input("Enter price"))
#	discount_percent = float(input("Enter discount"))
	
	#execute the condition
	if discount_percent >= 20:
		#calculate discount
		return price * discount_percent/100
	return price

#takes input from user
price = float(input("Enter price: "))
discount_percent = float(input("Enter discount: "))
print(calculate_discount(price, discount_percent))

