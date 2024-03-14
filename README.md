This Python script is designed to help users allocate their daily time efficiently across various activities based on the priority of each activity. The program guides users through inputting their activities, assigning priorities, and then calculates how much time should be dedicated to each activity within the constraints of the user's available time.

Features
Activity Input: Users can input up to 10 activities for the day.
Priority Assignment: Each activity is assigned a priority on a scale from 1 to 10, with 1 being the highest priority.
Time Allocation: The script calculates the distribution of the user's available time across the entered activities based on their priorities.
Flexible Time Availability: Users specify their total available time for the day, allowing for a customized and realistic schedule.
How to Use
Entering Activities:

Run the script.
When prompted, enter your activities one by one.
Type 'end' to finish entering activities or once you've entered the maximum of 10 activities.
Assigning Priorities:

After entering all your activities, you'll be asked to assign a priority to each one. Priorities range from 1 (highest priority) to 10 (lowest priority).
Specifying Available Time:

Specify how many hours you have available for these activities, between 2 to 7 hours.
Viewing Your Schedule:

The program calculates and displays your daily schedule, showing how much time you should dedicate to each activity.
Implementation Details
The script uses lists to store activities, their priorities, and the calculated time distribution.
It ensures that the total allocated time does not exceed the user's available time.
Adjustments are made to ensure that the sum of allocated times matches the total available time exactly.
Requirements
This script is written in Python and does not require any external libraries. It should run in any standard Python environment.

Conclusion
The Daily Activity Scheduler is a simple tool for managing daily tasks more effectively by prioritizing activities and allocating time based on those priorities. It's particularly useful for individuals looking to maximize productivity within a limited time frame each day.
