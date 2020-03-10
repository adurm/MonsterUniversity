from monster_workshop import MonsterWorkshop
from student import Student
from teacher import Teacher


# As a Receptionist of the University, I should be able to create a Student with only first and last name

# Create empty list called students
list_of_students = []
# create a student_id_counter
student_id = 0
# With every iteration of the while loop:
while False:
    # increment the student_id_counter
    student_id += 1
    # ask for user input (names)
    first_name = input("Enter first name")
    last_name = input("Enter last name")
    # create a student from those inputs
    student = Student(first_name, last_name, student_id)
    # add that student to the list of students
    list_of_students.append(student)

    print(f"Student name: {first_name} {last_name} {student_id}")
    #print(list_of_students)
    print("Number of students in list: " + str(len(list_of_students)))


#  As a Receptionist of the University, I should be able to create a Teacher

# declare a list of teachers
list_of_teachers = []
# teacher_id_count variable
teacher_id = 0
# create the while loop:
while True:
    # increment the counter
    teacher_id += 1
    # ask for first name
    first_name = input("Enter first name: ")
    # ask for second name
    last_name = input("Enter last name: ")

    # if user input = quit,

    if first_name == 'quit' or last_name == 'quit':
        # quit the loop
        break


    # create teacher object from inputs
    teacher = Teacher(first_name, last_name, teacher_id)
    # add teacher to list
    list_of_teachers.append(teacher)

    print(f"Teacher name: {first_name} {last_name} {teacher_id}")
    # print(list_of_students)
    print("Number of teachers in list: " + str(len(list_of_teachers)))



# As a Receptionist of the University, I should be able to create a workshop

# create a list for workshops
# while loop
    # ask for subject
    # ask for list of attendants
    # ask for teacher name
# adding workshop to list of workshops


# declare a list of workshops
# create the while loop:
    # ask for subject name
    # ask for teacher
    # add list of students (predefined)
    # add workshop to list
    # print list of workshops
