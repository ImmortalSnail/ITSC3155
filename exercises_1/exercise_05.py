# Lists
list = []
list2 = []
result_list = []

# Populate lists
for x in range(5):
    list.append(int(input("Enter a number for list 1: ")))
for x in range(5):
    list2.append(int(input("Enter a number for list 2: ")))

# Generates results
for x in list:
    var = list[x - 1]
    for x in list:
        if var == list2[x - 1] and result_list.count(var) == 0:
            result_list.append(var)

# Prints finished lists
print(str(list) + "\n" + str(list2) + "\n" + str(result_list))