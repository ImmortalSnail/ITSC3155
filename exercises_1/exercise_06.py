# Variables
num1 = int(input("Please input desired row (1 - 5): "))
num2 = int(input("Please input desired column (1 - 5): "))

# Generates a 2D array filled with 0's
list = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# Puts 1 in appropriate postion within array
list[num1 - 1][num2 - 1] = 1

# Prints results
for x in range(5):
    var = x
    for x in range(5):
        print(list[var][x], end = " ")
    print()