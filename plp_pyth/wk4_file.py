#ask user for a filename
#check if file exist

try:
	with open(input("Enter filename: "), "r") as file:
		output = file.read()
		print(output)
except FileNotFoundError:
	print("File not found")