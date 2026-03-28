# Stephen Garcia Perez
# MO2_LAB
# This program does the following, it will ask a student its last name and then store
# it in a variable, if the value entered is NOT "ZZZ", then it will go ahead and ask the student for its name
# then it will ask for their GPA and store them in variables. Then we check if their GPA is greater than 3.25
# to print if they enter the Honor roll and if its greater than 3.5 then it prints a message telling them they
# have entered Dean's List

students_last_name = ""

while students_last_name != "ZZZ":
    students_last_name = input("\nPlease enter your last name or enter ZZZ to quit: \n")
    if students_last_name == "ZZZ":
        break
     
    students_first_name = input("\nEnter your first name: \n")
    students_GPA = float(input("\nEnter your GPA: \n"))
    
    
    if students_GPA >= 3.5:
        print(f"{students_first_name} {students_last_name} you have made it to the Dean's List")
    elif students_GPA >= 3.25:
        print(f"{students_first_name} {students_last_name} you have made it to the Honor Roll")
    else:
        print(f"{students_first_name} {students_last_name} sorry but your GPA is under 3.25")

    
print("The program has ended")
