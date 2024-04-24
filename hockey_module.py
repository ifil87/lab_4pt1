import random
import string
N = int(input("Введите количество паролей: "))
K = int(input("Введите длину пароля: "))
for _ in range(N):
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=K))
    print(password)
#1



import random

# Ввожу количество экзаменов
num_exams = int(input("Введите количество экзаменов: "))

# Ввожу наименования дисциплин
disciplines = input("Введите наименования дисциплин через запятую и пробел: ").split(", ")

# Дни недели и время для экзаменов
days = ["понедельник", "вторник", "среда", "четверг", "пятница"]
times = list(range(9, 15, 1))

for exam in range(num_exams):
    discipline = random.choice(disciplines)
    day = random.choice(days)
    time = random.choice(times)
    ticket_number = random.randint(1, 20)

    print(f"Экзамен по дисциплине «{discipline}» состоится в {day} время {time}. Ваш счастливый билет N {ticket_number}.")
#2



import datetime

# Ввожу количества дней до экзамена
days_until_exam = int(input("Введите количество дней до экзамена: "))

# Получая текущую дату
current_date = datetime.datetime.now()

# Вычисляю дату экзамена
exam_date = current_date + datetime.timedelta(days=days_until_exam)

# Получаю название месяца для даты экзамена
month_name = exam_date.strftime("%B")

# Вывожу результат
print(f"Экзамен состоится {exam_date.day} {month_name}.")
#3




from datetime import datetime, timedelta

def is_lucky_exam_date(date):
    day_of_week = date.strftime("%A")
    day = int(date.strftime("%d"))
    return (day % 4 != 0 and day_of_week != "Monday")

def predict_lucky_exam_dates(start_date, n):
    current_date = datetime.strptime(start_date, "%Y/%m/%d")
    lucky_dates = []

    while len(lucky_dates) < 3:
        current_date += timedelta(days=n)
        if is_lucky_exam_date(current_date):
            lucky_dates.append(current_date)

    for date in lucky_dates:
        print(f"{date.strftime('%d %B, %A')}")

start_date = input("Введите дату в формате YYYY/MM/DD: ")
n = int(input("Введите число n: "))

predict_lucky_exam_dates(start_date, n)
#4



def description():
    print("Модуль для симуляции игры в хоккей. Включает функции для управления игроками и счетом.")

def power_shot(player):
    print(f"{player} совершает мощный бросок на ворота!")

def check_goal(scored):
    if scored:
        print("Гол! Счет увеличивается!")
    else:
        print("Промах! Жаль, мяч не попал в ворота.")

import hockey_module

# Выводим описание модуля
hockey_module.description()

# Симуляция игры
player1 = "Игрок 1"
player2 = "Игрок 2"
score = 0

hockey_module.power_shot(player1)
score += 1
hockey_module.check_goal(True)

hockey_module.power_shot(player2)
hockey_module.check_goal(False)
#5
