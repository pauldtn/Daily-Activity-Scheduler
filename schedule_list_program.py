# Initialize lists to store activities, priorities, and time distribution
activities = []
priorities = []
time_distribution = [0] * 10

# Request user input for activities
print("Please enter your activities. Type 'end' when you've entered all \
activities (maximum 10).")
while len(activities) < 10:
    activity = input(f"Activity {len(activities) + 1}: ").strip()
    
    if activity.lower() == 'end':
        break
    
    activities.append(activity)

# Display a message about the maximum number of activities
print(f"\nYou have entered {len(activities)} activities. The maximum is 10.")

# Request user input to assign priorities to activities
print("\nNow, let's assign priorities to your activities.")
for activity in activities:
    priority = int(input(f"On a scale from 1 to 10, how important is '{activity}'? "))
    
    """
    Ensure that 1 is the top priority and the priority decreases with 
    increasing numbers
    """
    priority = max(1, min(priority, 10))
    
    priorities.append(priority)  # This line should be inside the loop

# Calculate daily time available
while True:
    time_available = int(input("\nHow many hours do you have available each \
day (between 2 and 7 hours)? "))
    
    if 2 <= time_available <= 7:
        break
    else:
        print("Please enter a valid time between 2 and 7 hours.")

# Calculate the total priority score
total_priority_score = sum([11 - priority for priority in priorities])

# Calculate time distribution based on priorities and the number of activities
for i, priority in enumerate(priorities):
    # Calculate the proportion of the total priority this activity represents
    priority_proportion = (11 - priority) / total_priority_score
    # Allocate time based on this proportion
    time_distribution[i] = round(priority_proportion * time_available)

# Ensure the total time does not exceed time_available
# Adjust the last activity's time if necessary
total_allocated_time = sum(time_distribution[:len(activities)])
if total_allocated_time != time_available:
    time_distribution[len(activities) - 1] += time_available - total_allocated_time

# Display the daily schedule
print("\nYour Daily Schedule:")
for i in range(len(activities)):
    print(f"{i + 1}. {activities[i]} - Priority {priorities[i]}, {time_distribution[i]} hours")