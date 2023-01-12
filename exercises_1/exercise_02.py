word1 = input("Enter a string: ")
word2 = input("Enter a different string: ")

result1 = word1.endswith(word2)
result2 = word2.endswith(word1)

if result1:
    print(result1)
elif result2:
    print(result2)
else:
    print(False)