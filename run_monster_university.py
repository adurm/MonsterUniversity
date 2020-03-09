from monsters_university.monster_workshop import MonsterWorkshop
from monsters_university.student import Student
from monsters_university.teacher import Teacher

class RunUniversity:

    def __init__(self):
        self.students = []
        self.teachers = []
        self.workshops = []
        self.student_id = 0
        self.teacher_id = 0

    def start(self):
        print("===================================")
        print("MONSTERS UNIVERSITY DATABASE SYSTEM")
        print("Please sign in to have access.")

    def log_in(self):
        username = input("Username\n> ")
        password = input("Password\n> ")
        if username != 'celia':
            print("HUMAN DETECTED. ABORT! ABORT!")
            exit(0)

    def new_studentID(self):
        self.student_id += 1
        return self.student_id

    def new_teacherID(self):
        self.teacher_id += 1
        return self.teacher_id

    def run(self):
        print("Welcome back Celia. What would you like to do?")

        command = ''
        while command != 'quit':

            print("Enter relevant command, or type 'help' to see available commands")
            command = input("> ")

            if command == 'help':
                print("== COMMAND LIST ==")
                print("1. create_student")
                print("2. create_teacher")
                print("3. create_workshop")
                print("4. view_workshops")
                print("5. add_student_skills")
                print("6. list_student_skills")
                print("7. quit")
                print("Enter the command you would like to do.")
            elif command == 'create_student':
                first_name = input("Enter student first name\n> ")
                last_name = input("Enter student last name\n> ")
                self.students.append(Student(first_name, last_name, self.new_studentID()))
                print(f"Student {first_name} {last_name} created!")
            elif command == 'create_teacher':
                first_name = input("Enter teacher first name\n> ")
                last_name = input("Enter teacher last name\n> ")
                self.teachers.append(Teacher(first_name, last_name, self.new_teacherID()))
                print(f"Teacher {first_name} {last_name} created!")
            elif command == 'create_workshop':
                subject_name = input("Enter subject name\n> ")
                attendees = input("Enter attendees\n> ")
                teacher = input("Enter teacher name\n> ")
                self.workshops.append(MonsterWorkshop(subject_name, attendees, teacher))
            elif command == 'view_workshops':
                print("Current workshops: ")
                for workshop in self.workshops:
                    print("Workshop subject: " + workshop.subject_name + ". Teacher: " + workshop.teacher)
            elif command == 'add_student_skills':
                student_first_name = input("First name of student you would like to add a skill to?\n> ")
                skill = input("Enter the skill you would like to add\n> ")
                for student in self.students:
                    if student_first_name == student.first_name:
                        student.add_skill(skill)
                print(f"{student_first_name} now has the skill {skill}.")
            elif command == 'list_student_skills':
                student_first_name = input("First name of student you would like to view skills?\n> ")
                for student in self.students:
                    if student_first_name == student.first_name:
                        print(student.skills)
            elif command == 'quit':
                print("System shutting down.")
            else:
                print("Invalid command.")

    def main(self):
        program = RunUniversity()
        program.start()
        program.log_in()
        program.run()

