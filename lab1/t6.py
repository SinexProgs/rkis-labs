months_names = ["Январе", "Феврале", "Марте",
                "Апреле", "Мае", "Июне",
                "Июле", "Августе", "Сентябре",
                "Октябре", "Ноябре", "Декабре"]


def season_events(number_of_month: int):
    month_name = months_names[number_of_month - 1]
    if number_of_month <= 2 or number_of_month >= 12:
        event_text = "За окном падал белый снег"
    elif 3 <= number_of_month <= 5:
        event_text = "Птицы пели прекрасные песни"
    elif 6 <= number_of_month <= 8:
        event_text = "Солнце светило ярче чем когда-либо"
    else:
        event_text = "Урожай был невероятным"
    print(f"Вы родились в {month_name}. {event_text}")


season_events(int(input("Введите номер месяца своего рождения: ")))