# Create and empty list
my_list = []

# Append element to the empty list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)


# Insert the value of 15 at the send position
my_list.insert(1, 15)
print(my_list)

# Extend my_List with another list: [50,60,70]
my_list.extend([50, 60, 70])
print(my_list)

# remove the last element from the list
my_list.pop()
print(my_list)

# Sort my_list in ascending order
my_list.sort()
print(my_list)

# Find and print the index of the value of 30
new_index = my_list.index(30)
print(new_index)