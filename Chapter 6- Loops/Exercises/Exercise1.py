toppings = []
while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    if topping == 'quit':
        break
    toppings.append(topping)
    print(f"You have added a {topping} to your Pizza.")

print("Your pizza will have the following toppings:")
for topping in toppings:
    print(topping)
    