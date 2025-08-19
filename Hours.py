# Input
hour = int(input("Enter hour between 1-12: "))
hours_ahead = int(input("How many hours ahead: "))

# Calculation
new_hour = (hour + hours_ahead) % 12
if new_hour == 0:
    new_hour = 12

# Output
print(f"Time at that time would be: {new_hour} o'clock.")
