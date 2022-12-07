class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def av_score(self):
        if not self.grades:
            return 0
        list_gr = []
        for i in self.grades.values():
            list_gr.extend(i)
        return round(sum(list_gr) / len(list_gr), 2)

    def __str__(self):
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.av_score()}\n' \
              f'Курсы в процессе изучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.av_score() > other.av_score()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def av_score(self):
        if not self.grades:
            return 0
        list_gr = []
        for i in self.grades.values():
            list_gr.extend(i)
        return round(sum(list_gr) / len(list_gr), 2)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.av_score()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.av_score() < other.av_score()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


student1 = Student('Шура', 'Балаганов')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Михаил', 'Паниковский')
student2.courses_in_progress += ['Git']
student2.finished_courses += ['Введение в программирование']

student3 = Student('Адам', 'Козлевич')
student3.courses_in_progress += ['Python']
student3.finished_courses += ['Введение в программирование']

best_lecturer1 = Lecturer('Лектор', 'Ганнибал')
best_lecturer1.courses_attached += ['Python']

best_lecturer2 = Lecturer('Джон', 'Траволта')
best_lecturer2.courses_attached += ['Git']

best_lecturer3 = Lecturer('Рабиндранат', 'Тагор')
best_lecturer3.courses_attached += ['Python']

cool_rewiewer1 = Reviewer('Some', 'Buddy')
cool_rewiewer1.courses_attached += ['Python']
cool_rewiewer1.courses_attached += ['Git']

cool_rewiewer2 = Reviewer('Евгений', 'Петросян')
cool_rewiewer2.courses_attached += ['Python']
cool_rewiewer2.courses_attached += ['Git']

student1.rate_lect(best_lecturer1, 'Python', 4)
student1.rate_lect(best_lecturer1, 'Python', 5)
student1.rate_lect(best_lecturer1, 'Python', 5)

student1.rate_lect(best_lecturer2, 'Git', 7)
student1.rate_lect(best_lecturer2, 'Git', 5)
student1.rate_lect(best_lecturer2, 'Git', 9)

student1.rate_lect(best_lecturer1, 'Python', 7)
student1.rate_lect(best_lecturer1, 'Python', 8)
student1.rate_lect(best_lecturer1, 'Python', 5)

student2.rate_lect(best_lecturer2, 'Git', 7)
student2.rate_lect(best_lecturer2, 'Git', 7)
student2.rate_lect(best_lecturer2, 'Git', 9)

student3.rate_lect(best_lecturer3, 'Python', 8)
student3.rate_lect(best_lecturer3, 'Python', 9)
student3.rate_lect(best_lecturer3, 'Python', 9)

cool_rewiewer1.rate_hw(student1, 'Python', 8)
cool_rewiewer1.rate_hw(student1, 'Python', 9)
cool_rewiewer1.rate_hw(student1, 'Python', 7)

cool_rewiewer2.rate_hw(student2, 'Git', 9)
cool_rewiewer2.rate_hw(student2, 'Git', 6)
cool_rewiewer2.rate_hw(student2, 'Git', 6)

cool_rewiewer2.rate_hw(student3, 'Python', 5)
cool_rewiewer2.rate_hw(student3, 'Python', 5)
cool_rewiewer2.rate_hw(student3, 'Python', 9)
cool_rewiewer2.rate_hw(student3, 'Python', 6)
cool_rewiewer2.rate_hw(student3, 'Python', 5)
cool_rewiewer2.rate_hw(student3, 'Python', 8)

print(f'Студенты :\n\n{student1}\n\n{student2}\n\n{student3}')
print()

print(f'Лекторы :\n\n{best_lecturer1}\n\n{best_lecturer2}\n\n{best_lecturer3}')
print()

print(f'Результат сравнения студентов(по средним оценкам за ДЗ): '
      f' {student1.name} {student1.surname} > {student2.name} {student2.surname} = {student1 > student2}')
print()

print(f'Результат сравнения лекторов (по средним оценкам за лекции): '

      f'{best_lecturer1.name} {best_lecturer1.surname} > {best_lecturer2.name} {best_lecturer2.surname} = {best_lecturer1 > best_lecturer2}')
print()

students = [student1, student2, student3]
lecturers = [best_lecturer1, best_lecturer2, best_lecturer3]


def student_rating(students, course_name):
    all_stud = []
    for stud in students:
        all_stud.extend(stud.grades.get(course_name, []))
    if not all_stud:
        return 'По такому курсу нет оценок'
    return round(sum(all_stud) / len(all_stud), 2)


def lecturer_rating(lecturers, course_name):
    all_lect = []
    for lectur in lecturers:
        all_lect.extend(lectur.grades.get(course_name, []))
    if not all_lect:
        return 'По такому курсу нет оценок'
    return round(sum(all_lect) / len(all_lect), 2)


print(f"Средний балл для всех студентов по курсу {'Git'}: {student_rating(students, 'Git')}")
print(f"Средний балл для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturers, 'Python')}")
print()

