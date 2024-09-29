import re

# Prompt the user to enter the message
message = input("Enter the attendance message:\n")

# Prompt the user to specify if the provided roll numbers are absentees or presentees
attendance_type = (
    input(
        "Are the provided roll numbers absentees or presentees? (Enter 'A' for absentees or 'P' for presentees):\n"
    )
    .strip()
    .upper()
)

# Extract roll numbers using regular expression
roll_numbers = re.findall(r"\d+", message)
roll_numbers = list(map(int, roll_numbers))

# Generate the full list of roll numbers (1-61 and 501)
all_roll_numbers = list(range(1, 62)) + [501]

# Determine absentees based on the provided attendance type
if attendance_type == "P":
    absentees = [roll for roll in all_roll_numbers if roll not in roll_numbers]
elif attendance_type == "A":
    absentees = roll_numbers
else:
    print(
        "Invalid input for attendance type. Please enter 'A' for absentees or 'P' for presentees."
    )
    exit()

# Roll numbers to remove from the final result i.e. dropouts
roll_numbers_to_remove = [3, 4, 11, 32, 55, 60]  # Dropouts list

# Remove specific roll numbers from the absentees list
final_absentees = [roll for roll in absentees if roll not in roll_numbers_to_remove]

# Generate the complete attendance list with formatted roll numbers
attendance_list = []
for roll in all_roll_numbers:
    if roll in final_absentees:
        formatted_roll = f"AV.EN.U4CSE22{roll:03d}"
        attendance_list.append(formatted_roll)

# Print the complete attendance list
print("\n\nComplete Attendance List with Absentees Marked:")
for roll in attendance_list:
    print(roll)
