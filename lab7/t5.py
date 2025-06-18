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
                  Exercise(5, 2020, 5, 12),
                  Exercise(6, 2022, 4, 4),
                  Exercise(7, 2023, 2, 10),
                  Exercise(8, 2025, 4, 4),
                  Exercise(9, 2019, 1, 3),
                  Exercise(10, 2023, 4, 1)]

year_duration_sums = {}
for exercise in fitness_center:
    if exercise.year in year_duration_sums.keys():
        year_duration_sums[exercise.year] += exercise.duration
    else:
        year_duration_sums[exercise.year] = exercise.duration

max_duration_sum = 0
max_duration_sum_year = 0
for year, duration_sum in year_duration_sums.items():
    if duration_sum > max_duration_sum or (duration_sum == max_duration_sum and year < max_duration_sum_year):
        max_duration_sum = duration_sum
        max_duration_sum_year = year

print(f"{max_duration_sum_year} had the longest exercises in sum ({max_duration_sum})")