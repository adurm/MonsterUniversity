from monster_workshop import MonsterWorkshop
from student import Student
from teacher import Teacher

class RunUniversity:

    # Initialise empty "database" to hold information entered by receptionist
    def __init__(self):
        self.students = []
        self.teachers = []
        self.workshops = []
        self.student_id = 0
        self.teacher_id = 0

    # Starting message when loading program
    def start(self):
        print("===================================")
        print("MONSTERS UNIVERSITY DATABASE SYSTEM")
        print("Please sign in to have access.")

    # Log in method to check for correct username and password
    def log_in(self):
        username = input("Username\n> ")
        password = input("Password\n> ")
        # Only allow Celia to log in
        if username != 'celia':
            print("HUMAN DETECTED. ABORT! ABORT!")
            exit(0)
        # ilovemikey must be her password
        if password != 'ilovemikey':
            print("HUMAN DETECTED. ABORT! ABORT!")
            exit(0)

    # Create new studentID with every new entry
    def new_studentID(self):
        self.student_id += 1
        return self.student_id

    # Create new teacherID with every new entry
    def new_teacherID(self):
        self.teacher_id += 1
        return self.teacher_id

    # Help command
    def help_command(self):
        return'''
        == COMMAND LIST ==
        1. create_student
        2. create_teacher
        3. create_workshop
        4. view_workshops
        5. add_student_skills
        6. list_student_skills
        7. quit
        '''

    # Create student command
    def create_student_command(self):
        first_name = input("Enter student first name\n> ")
        last_name = input("Enter student last name\n> ")
        self.students.append(Student(first_name, last_name, self.new_studentID()))
        return(f"Student {first_name} {last_name} created!")

    # Create teacher command
    def create_teacher_command(self):
        first_name = input("Enter teacher first name\n> ")
        last_name = input("Enter teacher last name\n> ")
        self.teachers.append(Teacher(first_name, last_name, self.new_teacherID()))
        return(f"Teacher {first_name} {last_name} created!")

    # Create workshop command
    def create_workshop_command(self):
        subject_name = input("Enter subject name\n> ")
        attendees = input("Enter attendees\n> ")
        teacher = input("Enter teacher name\n> ")
        self.workshops.append(MonsterWorkshop(subject_name, attendees, teacher))
        return(f"Workshop {subject_name} with teacher {teacher} created!")

    # View workshops command
    def view_workshops_command(self):
        print("Current workshops: ")
        for workshop in self.workshops:
            print("Workshop subject: " + workshop.subject_name + ". Teacher: " + workshop.teacher)

    # Add student skills command
    def add_student_skills_command(self):
        student_first_name = input("First name of student you would like to add a skill to?\n> ")
        skill = input("Enter the skill you would like to add\n> ")
        for student in self.students:
            if student_first_name == student.first_name:
                student.add_skill(skill)
        print(f"{student_first_name} now has the skill {skill}.")
        if student not in self.students:
            return "Student not found."

    # List student skills command
    def list_student_skills_command(self):
        student_first_name = input("First name of student you would like to view skills?\n> ")
        for student in self.students:
            if student_first_name == student.first_name:
                print(student.skills)
        if student not in self.students:
            return("Student not found.")

    # Main method to run program
    def run(self):
        print("Welcome back Celia. What would you like to do?")
        command = ''

        while command != 'quit':
            print("Enter relevant command, or type 'help' to see available commands")
            command = input("> ")

            if command == 'help':
                print(self.help_command())
            elif command == 'create_student':
                print(self.create_student_command())
            elif command == 'create_teacher':
                print(self.create_teacher_command())
            elif command == 'create_workshop':
               print(self.create_workshop_command())
            elif command == 'view_workshops':
                print(self.view_workshops_command())
            elif command == 'add_student_skills':
                print(self.add_student_skills_command())
            elif command == 'list_student_skills':
                print(self.list_student_skills_command())
            elif command == 'quit':
                print("System shutting down.")
            else:
                print("Invalid command.")


program = RunUniversity()
program.start()
program.log_in()
program.run()
