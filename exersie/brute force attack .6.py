# Set the correct password
password = 12345
# Set number of allowed attempts
attempts = 5
while attempts > 0:
# Loop while attempts remain
    user_input = int(input("Enter your password: "))
# Get user input from user
    if user_input == password:
# Check if password is correct 
        print("Access granted.")
        break
    else:
# Reduce attempts after wrong input
        attempts -= 1
        print(f"Incorrect password. You have {attempts} attempts left.")
# If on attempts left, trigger final message
if attempts == 0:
    print("Authorities have been notified.")
