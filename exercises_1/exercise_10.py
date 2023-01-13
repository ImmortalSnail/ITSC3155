# Variables
inp = input("Enter a string: ")
list = []
leng = 0
add = []

# Add characters to list
for x in range(len(inp)):
    if leng == 3:
        leng = 0
        list.append(add[:])
        add.clear()
    leng +=1
    add.append(inp[x])
list.append(add[:])

# Prints
print(list)