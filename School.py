class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        avg_grade = self._calculate_average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def _calculate_average_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_count = sum(len(grades) for grades in self.grades.values())
        return round(total_grades / total_count, 2) if total_count != 0 else 0

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_average_grade() < other._calculate_average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_average_grade() <= other._calculate_average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_average_grade() > other._calculate_average_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_average_grade() >= other._calculate_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_average_grade() == other._calculate_average_grade()

    def __ne__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_average_grade() != other._calculate_average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = self._calculate_average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade}")

    def _calculate_average_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_count = sum(len(grades) for grades in self.grades.values())
        return round(total_grades / total_count, 2) if total_count != 0 else 0

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_average_grade() < other._calculate_average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_average_grade() <= other._calculate_average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_average_grade() > other._calculate_average_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_average_grade() >= other._calculate_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_average_grade() == other._calculate_average_grade()

    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_average_grade() != other._calculate_average_grade()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")

def average_grade_students(students, course):
    total_grades = 0
    total_count = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            total_count += len(student.grades[course])
    return round(total_grades / total_count, 2) if total_count != 0 else 0

def average_grade_lecturers(lecturers, course):
    total_grades = 0
    total_count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades += sum(lecturer.grades[course])
            total_count += len(lecturer.grades[course])
    return round(total_grades / total_count, 2) if total_count != 0 else 0

# Примеры использования
best_student_1 = Student('Ruoy', 'Eman', 'your_gender')
best_student_1.courses_in_progress += ['Python']
best_student_1.finished_courses += ['Введение в программирование']

best_student_2 = Student('Alex', 'Smith', 'male')
best_student_2.courses_in_progress += ['Python']

best_student_3 = Student('Jane', 'Doe', 'female')
best_student_3.courses_in_progress += ['Python']

best_student_4 = Student('John', 'Doe', 'male')
best_student_4.courses_in_progress += ['Python']

best_student_5 = Student('Alice', 'Johnson', 'female')
best_student_5.courses_in_progress += ['Python']

cool_Lecturer_1 = Lecturer('John', 'Doe')
cool_Lecturer_1.courses_attached += ['Python']

cool_Lecturer_2 = Lecturer('Jane', 'Smith')
cool_Lecturer_2.courses_attached += ['Python']

cool_Lecturer_3 = Lecturer('Alice', 'Johnson')
cool_Lecturer_3.courses_attached += ['Python']

cool_Reviewer_1 = Reviewer('Bob', 'Brown')
cool_Reviewer_1.courses_attached += ['Python']

cool_Reviewer_2 = Reviewer('Charlie', 'Davis')
cool_Reviewer_2.courses_attached += ['Python']

cool_Reviewer_3 = Reviewer('Eve', 'Wilson')
cool_Reviewer_3.courses_attached += ['Python']


cool_Reviewer_1.rate_hw(best_student_1, 'Python', 10)
cool_Reviewer_2.rate_hw(best_student_1, 'Python', 5)
cool_Reviewer_3.rate_hw(best_student_1, 'Python', 8)
cool_Reviewer_1.rate_hw(best_student_2, 'Python', 2)
cool_Reviewer_2.rate_hw(best_student_2, 'Python', 4)
cool_Reviewer_3.rate_hw(best_student_2, 'Python', 6)
cool_Reviewer_1.rate_hw(best_student_3, 'Python', 1)
cool_Reviewer_2.rate_hw(best_student_3, 'Python', 3)
cool_Reviewer_3.rate_hw(best_student_3, 'Python', 5)
best_student_1.rate_lecturer(cool_Lecturer_1, 'Python', 10)
best_student_2.rate_lecturer(cool_Lecturer_1, 'Python', 1)
best_student_3.rate_lecturer(cool_Lecturer_1, 'Python', 8)
best_student_1.rate_lecturer(cool_Lecturer_2, 'Python', 3)
best_student_2.rate_lecturer(cool_Lecturer_2, 'Python', 7)
best_student_3.rate_lecturer(cool_Lecturer_2, 'Python', 9)
best_student_1.rate_lecturer(cool_Lecturer_3, 'Python', 6)
best_student_2.rate_lecturer(cool_Lecturer_3, 'Python', 4)
best_student_3.rate_lecturer(cool_Lecturer_3, 'Python', 2)
print(f'Рейтинг студента: '
      f'\n{best_student_1}')
print(f'Рейтинг студента: '
      f'\n{best_student_2}')
print(f'Рейтинг студента: '
      f'\n{best_student_3}')
print(f'Рейтинг Лектора: '
      f'\n{cool_Lecturer_1}')
print(f'Рейтинг Лектора: '
      f'\n{cool_Lecturer_2}')
print(f'Рейтинг Лектора: '
      f'\n{cool_Lecturer_3}')
print(f'Проверяющий: '
      f'\n{cool_Reviewer_1}')
print(f'Проверяющий: '
      f'\n{cool_Reviewer_2}')
print(f'Проверяющий: '
      f'\n{cool_Reviewer_3}')
print(best_student_1 > best_student_3)
print(cool_Lecturer_1 < cool_Lecturer_2)

students = [best_student_1, best_student_2, best_student_3, best_student_4, best_student_5]
lecturers = [cool_Lecturer_1, cool_Lecturer_2, cool_Lecturer_3]
print(f"Средняя оценка за домашние задания по курсу 'Python': {average_grade_students(students, 'Python')}")
print(f"Средняя оценка за лекции по курсу 'Python': {average_grade_lecturers(lecturers, 'Python')}")

