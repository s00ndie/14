class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.gender}, {self.age}, {self.first_name}, {self.last_name}'

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()}, Record book: {self.record_book}'
class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group)>=10:
            raise OverflowError()
        self.group.add(student)

    def delete_student(self, last_name):
        to_delete = None
        for student in self.group:
            if student.last_name == last_name:
                to_delete = student
                break
        if to_delete:
            self.group.remove(to_delete)


    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student

        return None

    def __str__(self):
        all_students = '\n'.join(str(student)for student in self.group)
        return f'Number:{self.number}\n{all_students} '
try:
    gr = Group('PD1')
    for i in range(10):
        gr.add_student(Student('Male', 20, f'Student{i + 1}', f'Surname{i + 1}', f'AN{i + 1}'))
    gr.add_student(Student('Female', 22, 'Student11', 'Surname11', 'AN11'))
except OverflowError as e:
    print(f'Виникла поилка: {e}')

# st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
# st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# st3 = Student('Male', 123, 'b', 'Job', 'AN142')
# st4 = Student('Female', 15, 'c', 'Taylo', 'AN145')
# st5 = Student('Male', 3, 'S', 'Jo', 'AN142')
# st6 = Student('Female', 5, 'L', 'Tayl', 'AN145')
# st7 = Student('Male', 304, 'a', 'J', 'AN142')
# st8 = Student('Female', 215, 'f', 'Tay', 'AN145')
# st9 = Student('Male', 301, 'q', 'q', 'AN142')
# st10 = Student('Female', 525, 'k', 'Talk', 'AN145')
# st11 = Student('Male', 301, 'Sw', 'Jobsl', 'AN142')
# st12 = Student('Female', 225, 'Lk', 'Tayjjlor', 'AN145')
# gr = Group('PD1')
#
# gr.add_student(st1)
# gr.add_student(st2)
# gr.add_student(st3)
# gr.add_student(st4)
# gr.add_student(st5)
# gr.add_student(st6)
# gr.add_student(st7)
# gr.add_student(st8)
# gr.add_student(st9)
# gr.add_student(st11)
# gr.add_student(st12)
print(gr)
# assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
# assert gr.find_student('Jobs2') is None, 'Test2'
# assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student
