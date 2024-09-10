from datetime import datetime
# Get the current date and time
now = datetime.now()
# Format the date and time as desired
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
# Print the result
print("Current date and time:", formatted_now)