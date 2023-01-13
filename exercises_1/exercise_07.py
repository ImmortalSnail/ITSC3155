# By Ronnie Hampton
# Variables
quit = True
list = []
even_list = []

# Determines what should occur based on user input
while quit:
    var = input("Please enter an integer or type QUIT to stop: ")
    if var == "QUIT":
        quit = False
    elif int(var) % 2 == 0:
        list.append(int(var))
        even_list.append(int(var))
    else: 
        list.append(int(var))

# Outputs results after QUIT
print("Numbers entered: " + str(list))
print("Even numbers: " + str(even_list))