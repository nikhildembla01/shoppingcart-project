# Shopping Cart Program
foods = []
prices = []
total = 0

while True:
    food = input("Enter the food you want to buy (q to quit): ").strip()
    if food.lower() == "q":
        break
    else:
        try:
            price = float(input(f"Enter the price of {food}: $"))
            foods.append(food)
            prices.append(price)
        except ValueError:
            print("Invalid price! Please enter a numeric value.")

# Display Cart Items
print("\n----------------- YOUR CART ----------------")
if foods:
    print("Item\t\tPrice")
    print("-" * 30)
    for i in range(len(foods)):
        print(f"{foods[i]:<15} ${prices[i]:.2f}")
    print("-" * 30)
    total = sum(prices)  # Calculate total
    print(f"Total Bill: ${total:.2f}")
else:
    print("Your cart is empty.")
print("-------------------------------------------")

