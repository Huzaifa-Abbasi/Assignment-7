'''Write a program to manage a shopping list. Use variables to store item names, 
quantities, and prices. Calculate the total cost of items and check if you have enough budget.'''

item_name = []
quantities_of_items = 0
prices_of_items = 0
total_cost = 0
budget = int(input("Enter your Budget "))

while True:
    item = input("Enter the name of items ")
    item_name.append(item)

    quantity = int(input("Enter the Quantity of items "))
    quantities_of_items += quantity

    price = int(input("Enter the Price "))
    prices_of_items += price

    total = price * quantity
    total_cost += total

    user_input = input("add more items yes/no ")
    if user_input == "no":
        break

if total_cost <= budget:
    print("You can Purchase")
else:
    print("Insufficient Balance")

print("The Items are ",item_name)
print("The Quantities of Items are ",quantities_of_items)
print("the total cost of the items is  ", total_cost)