# Lists of total students for each class
total_csea = [2, 5, 6, 8, 16, 22, 27, 34, 44, 46, 50, 51, 54, 61]
total_cseb = [
    104,
    109,
    113,
    114,
    119,
    122,
    123,
    126,
    128,
    129,
    130,
    131,
    134,
    135,
    137,
    138,
    140,
    144,
    146,
    148,
    155,
]
total_csec = [
    203,
    209,
    214,
    216,
    218,
    224,
    228,
    229,
    232,
    234,
    237,
    246,
    248,
    251,
    252,
    253,
    258,
    259,
    261,
]

# List of present students
# present = [2, 5, 6, 8, 16, 22, 27, 34, 44, 46, 50, 54, 61]
# present = [4, 9, 14, 19, 22, 23, 26, 28, 29, 30, 31, 35, 38, 40, 44, 46, 48, 55, 61, 62]
present = [3, 9, 14, 16, 18, 24, 28, 29, 32, 37, 46, 48, 51, 52, 53, 58, 59]
present.sort()
CLASS = 1


# Function to pad roll numbers
def pad_roll_numbers(roll_numbers, class_constant):
    return [class_constant * 100 + roll_number for roll_number in roll_numbers]


# Function to determine absentees
def determine_absentees(total_students, present_students, class_constant):
    padded_total_students = pad_roll_numbers(total_students, class_constant)
    padded_present_students = pad_roll_numbers(present_students, class_constant)
    absentees = set(padded_total_students) - set(padded_present_students)
    return absentees


# Dictionary to map class constants to total student lists
class_mapping = {0: total_csea, 1: total_cseb, 2: total_csec}

# Class constant (0 for CSE A, 1 for CSE B, 2 for CSE C)
CLASS = 0  # Change this value to 1 or 2 for other classes

# Get the total students for the selected class
total_students = class_mapping.get(CLASS)

# Determine absentees for the selected class
absentees = sorted(list(determine_absentees(total_students, present, CLASS)))

# Print absentees for the selected class
print(f"CSE {chr(66 + CLASS)} Absentees:", absentees)
