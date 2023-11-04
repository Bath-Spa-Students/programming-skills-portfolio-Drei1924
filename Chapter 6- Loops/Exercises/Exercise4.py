sandwich_orders = []
finished_sandwiches = []

while True:
    print("Choices: (hatdog sandwhich) (ham sandwhich) (chicken sandwhich) (turkey sandwich) (pastrami sandwhich)")
    order = input("What type of sandwich would you like to order (or 'quit' to finish): ")
    
    if order.lower() == 'quit':
        break
    
    sandwich_orders.append(order)
    print(f"I made your {order} sandwich.")
    finished_sandwiches.append(order)

print("\nThis is the sandwhich you ordered:")
for sandwich in finished_sandwiches:
    print(sandwich)
