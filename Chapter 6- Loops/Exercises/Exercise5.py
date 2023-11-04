sandwich_orders = ['hatdog', 'turkey', 'pastrami', 'chicken', 'pastrami', 'ham', 'pastrami']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    print("Sorry, pastrami is not available.")
    sandwich_orders.remove('pastrami')

print("Available sandwich choices: " + ', '.join(sandwich_orders))

while sandwich_orders:
    current_order = input("What type of sandwich do you want (choose from the available options): ")
    if current_order == 'quit':
        break
    if current_order in sandwich_orders:
        sandwich_orders.remove(current_order)
        print(f"I made your {current_order} sandwich.")
        finished_sandwiches.append(current_order)
    else:
        print("Sorry, we don't have that sandwich on the menu.")

print("\nThis is the sandwhich which you ordered:")
for sandwich in finished_sandwiches:
    print(sandwich)