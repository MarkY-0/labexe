import workouts
def test_get_longest_workout():

    workouts = [
        "activity": "Running",
        "duration": 30
        "activity": "Cycling",
        "duration": 45
        "activity": "Swimming",
        "duration": 60

    ]

result = workouts.get_longest_workout(workouts)
assert(result['activity'] == "Swimming")

result_empty = workouts.get_longest_workout([])
assert(result_empty == None)

def test_total_duration():

    workouts = [
        "activity": "Running",
        "duration": 30
        "activity": "Cycling",
        "duration": 45
        "activity": "Swimming",
        "duration": 60

    ]

result = workouts.total_duration(workouts)
assert(result == 135)

def test_average_duration():

    workouts = [
        "activity": "Running",
        "duration": 30
        "activity": "Cycling",
        "duration": 45
        "activity": "Swimming",
        "duration": 60

    ]
result = workouts.average_duration(workouts)
assert(result == 45)

