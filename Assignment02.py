# --------------------------------------------------------------------------- #
# Title: Assignment02
# Desc:	 This assignment demonstrates using constants, variables, operators,
#            formatting, and files.
# Change Log: (Who, What, When)
#   N.Greco, 10/16/2024, Created script.
#   N.Greco, 10/19/2024, Updated filename to match title.
# --------------------------------------------------------------------------- #

# Define the Data Constants
COURSE_NAME: str = "Python 100"
COURSE_PRICE: float = 999.98
STATE_TAX: float = .09
TOTAL_PRICE: float = COURSE_PRICE + (COURSE_PRICE * STATE_TAX)
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
csv_data: str = ""
file_obj: object = None

# Get data from the user
student_first_name = input("Student's First Name: ")
student_last_name = input("Student's Last Name:  ")

# Present the data to the user
csv_data = f"{student_first_name},{student_last_name},{COURSE_NAME},"\
    f"{float(COURSE_PRICE):.2f},{float(TOTAL_PRICE):.2f}\n"
print(csv_data)

# Process the data to a file
file_obj = open(FILE_NAME, "w")
file_obj.write(csv_data)
file_obj.close()
# print("Data Recorded\n")  # Used for debugging.
