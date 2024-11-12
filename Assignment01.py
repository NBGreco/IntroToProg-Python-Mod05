# --------------------------------------------------------------------------- #
# Title: Assignment01
# Desc:	 This assignment demonstrates using constants, variables, and print()
# Change Log: (Who, What, When)
#   N.Greco, 10/12/2024, Created script.
#   N.Greco, 10/16/2024, Added variables in definition section.
#   N.Greco, 10/19/2024, Updated filename to match title.
# --------------------------------------------------------------------------- #

# Setup Code
# Define the data variables.
COURSE_NAME: str = "Python 100"
student_first_name: str = ""
student_last_name: str = ""

# Main Body
# Prompt the user to input the student's first and last names.
student_first_name = input("Please enter the student's first name: ")
student_last_name = input("Please enter the student's last name:  ")
# Display that student is registered for the course.
print(student_first_name + " " + student_last_name + " is registered for " + COURSE_NAME + ".")
print(student_first_name + " " + student_last_name + " is registered for " \
      + COURSE_NAME + ".")



