# coding: utf-8

groupmates = [
    {
        "name": "Василий",
        "group": "912-2",
        "age": 19,
        "marks": [4, 3, 5, 5, 4]
    },
    {
        "name": "Анна",
        "group": "912-1",
        "age": 18,
        "marks": [3, 2, 3, 4, 3]
    },
    {
        "name": "Георгий",
        "group": "912-2",
        "age": 19,
        "marks": [3, 5, 4, 3, 5]
    },
    {
        "name": "Валентина",
        "group": "912-1",
        "age": 18,
        "marks": [5, 5, 5, 4, 5]
    }
]


def print_students(students):
    # Заголовок таблицы с выравниванием по левому краю
    print("Имя студента".ljust(15), "Группа".ljust(8), "Возраст".ljust(8), "Оценки".ljust(20))

    for student in students:
        # Вывод данных каждого студента [cite: 90-91, 100]
        print(
            student["name"].ljust(15),
            student["group"].ljust(8),
            str(student["age"]).ljust(8),
            str(student["marks"]).ljust(20)
        )
    print("\n")


# ЗАДАНИЕ: Функция фильтрации по среднему баллу
def filter_students(students, threshold):
    filtered_list = []
    for student in students:
        # Считаем среднюю оценку [cite: 143]
        avg_mark = sum(student["marks"]) / len(student["marks"])
        if avg_mark > threshold:
            filtered_list.append(student)
    return filtered_list


# Выводим всех
print_students(groupmates)

# Выводим только тех, у кого средний балл выше 4.0
print("Студенты со средним баллом выше 4.0:")
print_students(filter_students(groupmates, 4.0))