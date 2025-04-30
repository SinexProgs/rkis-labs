date = input("Enter date (in format YYYY-MM-DD): ")
split_date = date.split("-")
date_dict = { "year": split_date[0], "month": split_date[1], "day": split_date[2] }
print(date_dict)