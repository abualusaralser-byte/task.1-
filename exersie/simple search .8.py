# List of names
names = ["ali", "omar", "ahmed", "mohamed"]
# Get name to search for
search = input("Enter name to search: ")
# Check hf the name exists (case-insensitive)
if search.lower() in [name.lower() for name in names]:
    print(f"{search} found in the list.")
else:
    print(f"{search} not found in the list.")
