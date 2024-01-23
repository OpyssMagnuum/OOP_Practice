class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    @property
    def avgGrade(self):
        avgGrades = []
        for key, item in self.grades.items():
            avgGrades.append(sum(item) / float(len(item)))
        return sum(avgGrades) / float(len(avgGrades))

    def __str__(self):
        avgGrades = []
        for key, item in self.grades.items():
            avgGrades.append(sum(item) / float(len(item)))
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: '
                f'{self.avgGrade}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}'
                f'\nЗавершенные курсы: {", ".join(self.finished_courses)}')

    def __lt__(self, other):
        return self.avgGrade < other.avgGrade

    def __eq__(self, other):
        return self.avgGrade == other.avgGrade

    def __gt__(self, other):
        return self.avgGrade > other.avgGrade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.grades = {}
        super().__init__(name, surname)

    def rate_lec(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in self.grades:
                self.grades[course] += [grade]
            else:
                self.grades[course] = [grade]
        else:
            return 'Ошибка'

    @property
    def avgGrade(self):
        avgGrades = []
        for key, item in self.grades.items():
            avgGrades.append(sum(item) / float(len(item)))
        return sum(avgGrades) / float(len(avgGrades))

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avgGrade}'

    def __lt__(self, other):
        return self.avgGrade < other.avgGrade

    def __eq__(self, other):
        return self.avgGrade == other.avgGrade

    def __gt__(self, other):
        return self.avgGrade > other.avgGrade


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
        return f'Имя: {self.name}\nФамилия: {self.surname}'


# Студент 1
student1 = Student('Иван', 'Иванов', 'М')
student1.courses_in_progress += ['Python', 'GIT']
student1.finished_courses += ['Введение в программирование']

# Студент 2
student2 = Student('Мария', 'Кузнецова', 'Ж')
student2.courses_in_progress += ['Python', 'GIT']
student2.finished_courses += ['Введение в программирование']

# Оценщики
review1 = Reviewer('Тарас', 'Тарасов')
review1.courses_attached += ['Python', 'GIT']
review2 = Reviewer('Андрей', 'Андреев')
review2.courses_attached += ['Python', 'GIT']
print(f'Оценщики: \n{review1}\n{review2} \n')

# Оценка по курсам
review1.rate_hw(student1, 'Python', 10)
review1.rate_hw(student2, 'Python', 7)

review1.rate_hw(student1, 'GIT', 8)
review1.rate_hw(student2, 'GIT', 6)

review2.rate_hw(student1, 'Python', 9)
review2.rate_hw(student2, 'Python', 5)

review2.rate_hw(student1, 'GIT', 7)
review2.rate_hw(student2, 'GIT', 6)

# Сравнение студентов
print(f'Студент 1: \n{student1}\n\nСтудент 2: \n{student2}\n')
if student1 > student2:
    print('Студент 1 лучше')
elif student1 < student2:
    print('Студент 2 лучше')
else:
    print('Оба хороши')

# Лекторы
lecture1 = Lecturer('Николай', 'Николаев')
lecture1.courses_attached += ['Python', 'GIT']
lecture2 = Lecturer('Михаил', 'Михайлов')
lecture2.courses_attached += ['Python', 'GIT']

# Оценка
lecture1.rate_lec(student1, 'Python', 7)
lecture1.rate_lec(student2, 'Python', 6)

lecture1.rate_lec(student1, 'GIT', 7)
lecture1.rate_lec(student2, 'GIT', 7)

lecture2.rate_lec(student1, 'Python', 9)
lecture2.rate_lec(student2, 'Python', 5)

lecture2.rate_lec(student1, 'GIT', 4)
lecture2.rate_lec(student2, 'GIT', 8)

print(f'\nЛекторы: \n{lecture1}\n\n{lecture2}\n')

if lecture1 > lecture2:
    print('Лектор 1 лучше')
elif lecture1 < lecture2:
    print('Лектор 2 лучше')
else:
    print('Оба хороши')


def avg_DZ_Students(course, *students):
    allValues = []
    for stud in students:
        if course in stud.grades.keys():
            allValues += stud.grades[course]
    return sum(allValues) / float(len(allValues))


print(f"\nСредняя оценка за все ДЗ по Python: {avg_DZ_Students('Python', student1, student2)}")


def avg_LC_Lectures(course, *lecturers):
    allValues = []
    for lect in lecturers:
        if course in lect.grades.keys():
            allValues += lect.grades[course]
    return sum(allValues) / float(len(allValues))


print(f"\nСредняя оценка за все лекции по Python: {avg_LC_Lectures('Python', lecture1, lecture2)}")
