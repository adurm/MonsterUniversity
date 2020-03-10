from monster import Monster
from student import Student


class Teacher(Monster):

    def __init__(self, first_name, last_name, staff_id):
        super(Teacher, self).__init__(first_name=first_name, last_name=last_name)
        self.__staff_id = staff_id