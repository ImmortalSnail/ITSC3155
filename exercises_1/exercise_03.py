# By Ronnie Hampton
# Variables
cube = int(input("Enter an integer greater than 1: "))

# Cubes sequentially
for x in range(cube + 1):
    print('Cube of ' + str(x) + ' is ' + str(x**3))