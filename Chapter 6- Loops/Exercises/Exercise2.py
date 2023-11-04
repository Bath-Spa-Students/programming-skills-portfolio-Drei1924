
while True:
    age = input("Enter age (or 'quit' to finish):  ")
    
    if age == 'quit':
        break
    
    age = int(age)

    if age < 3:
        print("The ticket is for free")

    elif age <13:
        print("Your ticket is 10$")

    else:
        print("Your ticket is 15$")

    

