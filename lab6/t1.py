names = ["Сергей", "Антон", "Андрей", "Олег", "Влад", "Артём", "Арсений", "Стас", "Кирилл", "Амрах"]
print(f"Names: {names}")
for name in names:
    if name.lower().startswith('а'):
        print(name)