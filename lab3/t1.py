from datetime import datetime


weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
months = ["Январь",  "Февраль", "Март",
          "Апрель",  "Май",     "Июнь",
          "Июль",    "Август",  "Сентябрь",
          "Октябрь", "Ноябрь",  "Декабрь"]


date = datetime.now()
print(weekdays[datetime.now().weekday()])
print(months[datetime.now().month - 1])
print("Михаил")
