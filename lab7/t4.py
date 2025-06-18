class Exercise:
    _client_id = 0
    _year = 0
    _month = 0
    _duration = 0

    def __init__(self, client_id, year, month, duration):
        self._client_id = client_id
        self._year = year
        self._month = month
        self._duration = duration

    @property
    def client_id(self):
        return self._client_id

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    @property
    def duration(self):
        return self._duration

    def __str__(self):
        return f"Client ID: {self._client_id}, Year: {self._year}, Month: {self._month}, Duration: {self._duration}"


fitness_center = [Exercise(1, 2019, 3, 5),
                  Exercise(2, 2022, 8, 9),
                  Exercise(3, 2023, 2, 1),
                  Exercise(4, 2025, 4, 3),
                  Exercise(5, 2020, 5, 12)]

shortest_exercise = fitness_center[0]
longest_exercise = fitness_center[0]
for exercise in fitness_center:
    if exercise.duration < shortest_exercise.duration:
        shortest_exercise = exercise
    elif exercise.duration > longest_exercise.duration:
        longest_exercise = exercise

print(f"Shortest exercise: {shortest_exercise}")
print(f"Longest exercise: {longest_exercise}")