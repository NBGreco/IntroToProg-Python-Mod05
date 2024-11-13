# --------------------------------------------------------------------------- #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception
#       handling.
# Change Log: (Who, When, What)
#   N.Greco, 11/10/2024, Created Script
#   N.Greco, 11/12/2024, Added Exception Handling
# --------------------------------------------------------------------------- #

import json

# Define the Data Constants
MENU: str = """
----- Course Registration Program -----
  Select from the following menu:
   1. Register a Student for a Course
   2. Show Current Data
   3. Save Data to a File
   4. Exit the Program
---------------------------------------
"""
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
course_name: str = ""               # Holds the input course name
file = None                         # Holds a reference to an opened file
json_data: str = ""                 # Holds the JSON file name
menu_choice: str = ""               # Holds the choice made by the user
student_data: dict = {}             # Holds the student data
student_first_name: str = ""        # Holds the input first name
student_last_name: str = ""         # Holds the input last name
students: list = []                 # Holds all combined student data

# Read Data from the JSON File
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError as e:  # Handles file not found error
    print("\nJSON file must exist before running this script!")
    print("\n" + "-" * 20 + " Technical Error Message " + "-" * 20)
    print(e, e.__doc__, type(e), sep = '\n')
    print("-" * 65 + "\n")
except Exception as e:  # Handles all other errors
    print("\nThere was a non-specific error!")
    print("\n" + "-" * 20 + " Technical Error Message " + "-" * 20)
    print(e, e.__doc__, type(e), sep = '\n')
    print("-" * 65 + "\n")
finally:    # Closes the file if not already done
    if not file.close():
        file.close()

# Present and Process the Data
while (True):

    # Present the Menu
    print(MENU)
    menu_choice = input("Menu Selection: ")

    # Input User Data
    if menu_choice == "1":
        try:
            student_first_name = input("\nStudent's First Name: ")
            if not student_first_name.isalpha(): # Checks for letters only
                raise ValueError("The first name must only contain letters.")
            student_last_name = input("Student's Last Name: ")
            if not student_last_name.isalpha(): # Checks for letters only
                raise ValueError("The last name must only contain letters.")
            course_name = input("Course Name: ")
            student_data = ({"FirstName": student_first_name, "LastName":\
                student_last_name, "CourseName": course_name})
            students.append(student_data)
            print(f"\n{student_first_name} {student_last_name} is now registered "\
                  f"for {course_name}.\n*** Please Save data to file to confirm. "\
                  f"***")
        except ValueError as e: # Handles incorrect character error
            print("\n" + "-" * 17 + " Error Message " + "-" * 17)
            print("\t" + e.__str__())
            print("-" * 49)
        except Exception as e: # Handles all other errors
            print("\nThere was a non-specific error!")
            print("\n" + "-" * 20 + " Technical Error Message " + "-" * 20)
            print(e, e.__doc__, type(e), sep='\n')
            print("-" * 65 + "\n")
        continue

    # Present the Current Data
    elif menu_choice == "2":
        print("\nCurrent List of Students:")
        for data in students:  # Displays all registered students
            print(f"\t{data["FirstName"]}, {data["LastName"]}, "\
                f"{data["CourseName"]}")
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            print("\nThe following data was saved to file:")
            for student in students:    # Displays all enrolled students
                print(f"\t{student["FirstName"]} {student["LastName"]} is " \
                    f"enrolled in {student["CourseName"]}.")
        except TypeError as e:  # Handles incorrect formatting of JSON file
            print("\nData must be in valid JSON format!")
            print("\n" + "-" * 20 + " Technical Error Message " + "-" * 20)
            print(e, e.__doc__, type(e), sep='\n')
            print("-" * 65 + "\n")
        except Exception as e:  # Handles all other errors
            print("\nThere was a non-specific error!")
            print("\n" + "-" * 20 + " Technical Error Message " + "-" * 20)
            print(e, e.__doc__, type(e), sep='\n')
            print("-" * 65 + "\n")
        finally:    # Closes the file if not already done
            if not file.close():
                file.close()
        continue

    # Stop the Loop
    elif menu_choice == "4":
        print("\n" + "-" * 35)
        print("*** Exiting Program. Thank you! ***")
        print("-" * 35)
        break   # Exit the loop

    # Menu Input Error Processing
    else:
        print("\n" + "-" * 52)
        print("!!! Please choose a menu option (1, 2, 3, or 4). !!!")
        print("-" * 52)
        continue