'''Fitness Tracker: You're building a fitness tracker app. Create variables to store daily steps, 
distance walked, and calories burned. Write expressions to calculate average steps per week 
and total distance covered in a month.'''

calories_burn = 0
total_steps = 0 
distance_walked = 0
for _ in range(30):
    steps = int(input("enter the steps "))
    total_steps += (steps)
    distance = int(input("enter the distance walked "))
    distance_walked += (distance)
    calories_burn += (steps) * 0.1
print("the total steps are",total_steps)
print("Average Steps in a week are",total_steps / 7)
print("the total Distance Walked is",distance_walked) 
print("the total calories Burn are ",calories_burn)