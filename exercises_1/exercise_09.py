# Variables
list = []

# Gets words from users
for x in range(5):
    list.append(input("Enter a word: "))

# Outputs
print("Words: " + str(list))
print("One string:", end = " ")
print(" ".join(list))