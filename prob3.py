#Group Members: Jamaika Joy L. Dangkiw, ALliyah Mari T. Basilio, Gene Lorraine Machis

grade_level = input("Enter your grade level:  ")

valid_grade_level = [7,8,9,10,11,12]

while not grade_level.isdigit():
    grade_level = input("Invalid grade level. Please enter a whole number:  ")

grade_level = int(grade_level)

if grade_level in valid_grade_level:
    print("Valid Grade Level")

else:
    print("Invalid Grade Level")