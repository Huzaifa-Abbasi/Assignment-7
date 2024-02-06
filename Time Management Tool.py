'''Develop a tool to track time spent on various activities. Use variables to 
store task names and durations. Write expressions to calculate total time spent on each task and 
identify areas for improvement.'''

my_activities = []
my_durations = []

while True:
    activities = input("enter the activities ").lower()
    my_activities.append(activities)
    duration = int(input("Enter the duration in minutes "))
    my_durations.append(duration)
    users_input = input("do you want to add more activities yes/no ").lower()
    if users_input == "no":
        break

print("Your Activities are",my_activities)
print("The Durations are ",my_durations)
print("The Total time You spent on the activities are ",sum(my_durations))

for i in range(len(my_durations)):
    if my_durations[i] >= 60:
        print("You should Spent less time on", my_activities[i])
