'''Design a recipe calculator that adjusts ingredient quantities based on the 
number of servings. Use variables to store recipe ingredients and amounts, and write 
expressions to calculate adjusted quantities.'''

recipe = {}
serving = int(input("Enter the Number of Servings: "))
while True:
    ingredient = input("enter the ingredients / Person: ").lower()
    ingredient_quantity = int(input("Enter the quantity of ingredient / Person: "))
    recipe[ingredient] = ingredient_quantity
    users_input = input("Do you want to add More ingredients: ").lower()
    if users_input == "no":
        break

print("Adjusted Recipe for", serving, "servings:")
for ingredient, quantity in recipe.items():
    adjusted_quantity = (serving * quantity)
    print(f"{ingredient}: {adjusted_quantity} units")