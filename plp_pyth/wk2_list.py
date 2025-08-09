#create an empty list called my_list

my_list = []

#append the following data [10, 20, 30, 40]

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#insert value 15 at second position

my_list[1] = 15

#extend list with another lis [50, 60, 70]

extend_list = [50, 60, 70]

my_list.extend(extend_list)

#remove last element from the list

my_list.pop()

#sort my_list in ascending order

my_list.sort()

#find and print the index of the value 30 in the list

print(my_list.index(30))

