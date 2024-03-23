# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("lester the great\n")
        file.write("12345\n")
        file.write("lester the master\n")
except IOError as e:
    print(f"An error occurred: {e}")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("File Contents:")
        print(content)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Additional line 1\n")
        file.write("67890\n")
        file.write("Last line of text\n")
except IOError as e:
    print(f"An error occurred: {e}")