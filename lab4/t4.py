import datetime

weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
months = ["Январь",  "Февраль", "Март",
          "Апрель",  "Май",     "Июнь",
          "Июль",    "Август",  "Сентябрь",
          "Октябрь", "Ноябрь",  "Декабрь"]

def text_to_date(text):
    split_date = text.split('.')
    date = datetime.date(int(split_date[2]), int(split_date[1]), int(split_date[0]))
    return f"{weekdays[date.weekday()]}, {date.day} {months[date.month - 1]}, {date.year} год"

text_date = input("Enter date (DD.MM.YYYY): ")
print(text_to_date(text_date))