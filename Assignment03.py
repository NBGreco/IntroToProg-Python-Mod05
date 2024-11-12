# --------------------------------------------------------------------------- #
# Title: Assignment03
# Desc:	 This assignment demonstrates using conditional logic and looping.
# Change Log: (Who, What, When)
#   N.Greco, 10/19/2024, Created Script
#   N.Greco, 10/21/2024, Changed CSV open from "write" to "append"
# --------------------------------------------------------------------------- #

# Define the Data Constants
MENU: str = """
------ Course Registration Program ------
  Select from the following menu:
   1. Register a Student for a Course
   2. Show Current Data
   3. Save Data to a File
   4. Exit the Program
-----------------------------------------
"""
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables
course_name: str = ""
csv_data: str = ""
menu_choice: int = 0
student_first_name: str = ""
student_last_name: str = ""
file_obj: object = None

# Present and Process the Data
while True:
    # Present the Menu
    print(MENU)
    menu_choice = int(input("Menu Selection: "))
    match menu_choice:
        # Input User Data
        case 1:
            student_first_name = input("\nStudent's First Name: ")
            student_last_name = input("Student's Last Name: ")
            course_name = input("Course Name: ")
            csv_data = f"{student_first_name},{student_last_name},"\
                f"{course_name}"
        # Present the Current Data
        case 2:
            if student_first_name == "" or student_last_name == "" or \
                course_name == "":  # Skips operation if none registered
                print("\n---------------------------------------")
                print("!!! Please register a student first !!!")
                print("---------------------------------------")
            else:
                print("\nCurrent Data Input:")
                print(csv_data)
        # Save the Data
        case 3:
            if student_first_name == "" or student_last_name == "" or \
                    course_name == "":  # Skips operation if none registered
                print("\n---------------------------------------")
                print("!!! Please register a student first !!!")
                print("---------------------------------------")
            else:
                file_obj = open(FILE_NAME, "a")
                file_obj.write(csv_data + "\n")
                file_obj.close()
                print("\nStored the Following Data:")
                print(csv_data)
        # Stop the Loop
        case 4:
            print("\n-----------------------------------")
            print("*** Exiting Program. Thank you! ***")
            print("-----------------------------------")
            break
        # Error Processing
        case _:
            print("\n----------------------------------------------------")
            print("!!! Please choose a menu option (1, 2, 3, or 4). !!!")
            print("----------------------------------------------------")