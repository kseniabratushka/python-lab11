import pandas as pd
import numpy as np

students = {
    "Prikhodko_Vitaliy": {"surname": "Приходько", "name": "Віталій", "birthdate": (2006, 10, 8)},
    "Kropyvnytskyi_Dmytro": {"surname": "Кропивницький", "name": "Дмитро", "birthdate": (2007, 12, 24)},
    "Romanenko_Mikhailo": {"surname": "Романенко", "name": "Михайло", "birthdate": (2006, 3, 15)},
    "Shevchenko_Maxim": {"surname": "Шевченко", "name": "Максим", "birthdate": (2008, 1, 20)},
    "Zhuk_Victoria": {"surname": "Жук", "name": "Вікторія", "birthdate": (2007, 10, 8)},
    "Petrivnyi_Andriy": {"surname": "Петрівний", "name": "Андрій", "birthdate": (2005, 4, 2)},
    "Dubovets_Oksana": {"surname": "Дубовець", "name": "Оксана", "birthdate": (2006, 8, 11)},
    "Stroganov_Nikita": {"surname": "Строганов", "name": "Нікіта", "birthdate": (2007, 5, 30)},
    "Nikolaenko_Karina": {"surname": "Ніколаєнко", "name": "Каріна", "birthdate": (2005, 10, 9)},
    "Tkachenko_Evgenia": {"surname": "Ткаченко", "name": "Євгенія", "birthdate": (2007, 2, 17)}
}

import random

for student_key in students.keys():
    students[student_key]["course"] = random.randint(1, 4)
    students[student_key]["average_grade"] = round(random.uniform(60, 100), 2)
    students[student_key]["tuition_fee"] = random.randint(8000, 15000)

new_students = {
    "Ivanenko_Anna": {"surname": "Іваненко", "name": "Анна", "birthdate": (2006, 7, 14), "course": 2, "average_grade": 92.5, "tuition_fee": 12000},
    "Kovalenko_Oleg": {"surname": "Коваленко", "name": "Олег", "birthdate": (2007, 9, 3), "course": 1, "average_grade": 78.3, "tuition_fee": 9500},
    "Melnyk_Sofia": {"surname": "Мельник", "name": "Софія", "birthdate": (2005, 11, 28), "course": 3, "average_grade": 88.9, "tuition_fee": 11000}
}

students.update(new_students)

df = pd.DataFrame.from_dict(students, orient='index')

print("Повний DataFrame:")
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(df)
print("\n" + "="*80 + "\n")

print("1. Перші 3 рядки DataFrame:")
print(df.head(3))
print("\n" + "-"*40 + "\n")

print("2. Типи даних:")
print(df.dtypes)
print("\n" + "-"*40 + "\n")

print("3. Розмірність DataFrame:")
print(f"Кількість рядків: {df.shape[0]}, стовпців: {df.shape[1]}")
print("\n" + "-"*40 + "\n")

print("4. Описова статистика для числових стовпців:")
print(df.describe())
print("\n" + "-"*40 + "\n")

df['total_tuition_cost'] = df['tuition_fee'] * 4
print("5. DataFrame з новим стовпцем 'total_tuition_cost':")
print(df[['surname', 'name', 'course', 'tuition_fee', 'total_tuition_cost']].head(13))
print("\n" + "-"*40 + "\n")

expensive_students = df[df['tuition_fee'] > 10000]
print("6. Студенти з вартістю навчання понад 10,000 грн:")
print(expensive_students[['surname', 'name', 'course', 'tuition_fee']])
print("\n" + "-"*40 + "\n")

sorted_by_grade = df.sort_values('average_grade', ascending=False)
print("7. Студенти, відсортовані за середнім балом (спадання):")
print(sorted_by_grade[['surname', 'name', 'course', 'average_grade']].head(13))
print("\n" + "-"*40 + "\n")

average_by_course = df.groupby('course')['average_grade'].mean()
print("8. Середній бал по курсах:")
print(average_by_course)
print("\n" + "-"*40 + "\n")

max_tuition_by_course = df.groupby('course')['tuition_fee'].max()
print("9. Максимальна вартість навчання по курсах:")
print(max_tuition_by_course)
print("\n" + "-"*40 + "\n")

print("Остаточний DataFrame:")
print(df[['surname', 'name', 'course', 'average_grade', 'tuition_fee']])