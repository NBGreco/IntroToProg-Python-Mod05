# --------------------------------------------------------------------------- #
# Title: Assignment04
# Desc:	 This assignment demonstrates using lists and files to work with data
# Change Log: (Who, What, When)
#   N.Greco, 10/28/2024, Created Script
# --------------------------------------------------------------------------- #

# Define the Data Constants
MENU: str = '''
----- Course Registration Program -----
  Select from the following menu:
   1. Register a Student for a Course
   2. Show Current Data
   3. Save Data to a File
   4. Exit the Program
---------------------------------------
'''
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables
course_name: str = ''           # Holds the input course name
# csv_data: str = ''            # No longer used, kept for posterity
file = None                     # Holds a reference to an opened file
menu_choice: str = ''           # Holds the choice made by the user
# student_data: list = []       # No longer used, kept for posterity
student_first_name: str = ''    # Holds the input first name
student_last_name: str = ''     # Holds the input last name
students: list = []             # Holds all combined student data

# Read Data from CSV File
file = open(FILE_NAME, 'r')     # Opens the CSV file to read existing data
for row in file.readlines():    # Imports data row by row via for loop
    data = row.strip().split(',')  # Cleans and splits into list elements
    students.append([data[0], data[1], data[2]])  # Adds student to log

# Present and Process the Data
while True:

    # Present the Menu
    print(MENU)
    menu_choice = input("Menu Selection: ")

    # Input User Data
    if menu_choice == "1":
        student_first_name = input("\nStudent's First Name: ")
        student_last_name = input("Student's Last Name: ")
        course_name = input("Course Name: ")
        students.append([student_first_name, student_last_name, course_name])
        print(f'\n{student_first_name} {student_last_name} is now registered '\
              f'for {course_name}.\n*** Please Save data to file to confirm. '\
              f'***')
        continue

    # Present the Current Data
    elif menu_choice == "2":
        print("\nCurrent List of Students:")
        for data in students:  # Displays all registered students
            print(f'\t{data[0]}, {data[1]}, {data[2]}')
        continue

    # Save the Data
    elif menu_choice == "3":
        print("\nStored the Following Data:")
        file = open(FILE_NAME, "w")  # Opens CSV file for writing
        for data in students:  # Writes and displays all registered students
            file.write(f'{data[0]},{data[1]},{data[2]}\n')
            print(f'\t{data[0]}, {data[1]}, {data[2]}')
        file.close()
        continue

    # Stop the Loop
    elif menu_choice == "4":
        print("\n-----------------------------------")
        print("*** Exiting Program. Thank you! ***")
        print("-----------------------------------")
        break   # Exit the loop

    # Input Error Processing
    else:
        print("\n----------------------------------------------------")
        print("!!! Please choose a menu option (1, 2, 3, or 4). !!!")
        print("----------------------------------------------------")
        continue