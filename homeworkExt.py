# Дополнительное практическое задание по модулю: "Базовые структуры данных"
# Задание "Средний балл"

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]      # исходный список оценок
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}                            # исходное множество студентов
grades_upd = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]),             # определяем средние оцнки
              sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]),
              sum(grades[4])/len(grades[4])]

students_list = sorted(list(students))                   # создаем отсортированый по алфавиту список студентов
students_dict = dict(zip(students_list, grades_upd))     # создаем словарь в формате; "студент:средняя оценка"
print(students_dict)                                     # и выводим его в консоль
