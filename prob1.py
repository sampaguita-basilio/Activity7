#Group Members: Jamaika Joy L. Dangkiw, ALliyah Mari T. Basilio, Gene Lorraine Machis

age = input("Enter your age: ")

valid_age = [12,13,14,15,16,17,18]

while not age.isdigit():
    age = input("Invalid input. Please enter a whole number: ")

age = int(age)

if age not in valid_age:
    print("Invalid age")

else:
    print("Valid age")