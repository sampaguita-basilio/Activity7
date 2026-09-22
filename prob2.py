#Group Members: Jamaika Joy L. Dangkiw, ALliyah Mari T. Basilio, Gene Lorraine Machis

username = input("Please enter your username (username must be letters and numbers only and must contain 5 to 10 characters: ").lower()

valid_characters = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
                   "n","o","p","q","r","s","t","u","v","w","x","y","z",
                    "1","2","3","4","5","6","7","8","9"]

if all(char in valid_characters for char in username) and 5<= len(username) <=10:
    print("Valid username")

else:
    print("Invalid username")