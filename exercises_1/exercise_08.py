# By Ronnie Hampton
# Variables
list = []
unique = []

# Populates list[] with user inputs
for x in range(10):
    list.append(input(" Enter number " + str(x + 1) + ": "))

# Appends numbers to unique[] where appropriate
for x in list:
    if list.count(x) == 1:
        unique.append(x)

# Output
print("Original: " + str(list))
print("Unique: " + str(unique))
