from datetime import date


class Task:
    _date_start: date
    _date_finish: date
    _description: str

    def __init__(self, date_start, date_finish, description):
        self._date_start = date_start
        self._date_finish = date_finish
        self._description = description

    @property
    def date_start(self):
        return self._date_start

    @property
    def date_finish(self):
        return self._date_finish

    @property
    def description(self):
        return self._description

    def __str__(self):
        return f"{self._date_start} - {self._date_finish}: {self._description}"


tasks = [Task(date(2025, 6, 18), date(2025, 6, 19), "Task 1"),
         Task(date(2025, 2, 20), date(2025, 2, 25), "Task 2"),
         Task(date(2023, 12, 2), date(2024, 4, 25), "Task 3"),
         Task(date(2025, 12, 6), date(2026, 2, 21), "Task 4"),
         Task(date(2025, 1, 22), date(2025, 1, 30), "Task 5")]

last_task = tasks[0]
for task in tasks:
    if task.date_finish > last_task.date_finish:
        last_task = task

print(last_task)