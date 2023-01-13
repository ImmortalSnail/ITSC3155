# By Ronnie Hampton
# Variables
grade = float(input("Please enter a grade from 0 - 100: "))

# Compares variable, assignes grade,
if grade >= 90:
    print("Your grade is A.")
elif grade < 90 and grade >=80:
    print("Your grade is B.")
elif grade < 80 and grade >=70:
    print("Your grade is C.")
elif grade < 70 and grade >=60:
    print("Your grade is D.")
else:
    print("Your grade is F.")
