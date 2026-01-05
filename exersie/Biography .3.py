# Get user,s name
name =input("Enter your name: ")
# Get user,r hometown
hometown = input("Enter your hometown: ")
# Get user,s age as text 
age = input("Enter your age: ")
# Check if age numeric
if  age.isdigit():
# Convert age to integer
    age = int(age) 
else:
# Invalid age message
    print("Age must be a number")
    exit()
# Store user info in a dictionary
   
information = {
    "name":name,
    "hometown": hometown,
    "age": age,
}
# Print each value on a new line 
print(information["name"], information["hometown"], information["age"], sep="\n")
