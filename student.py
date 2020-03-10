from monster import Monster


class Student(Monster):

    def __init__(self, first_name, last_name, student_id):
        super(Student, self).__init__(first_name, last_name)
        self.student_id = student_id
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)

    def get_skills(self):
        return self.skills