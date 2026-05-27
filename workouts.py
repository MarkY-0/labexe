def get_longest_workout(workouts):


    if not workouts:
        return None
    
    longest = workouts[0]
    for workout in workouts:
        if workout['duration'] > longest['duration']:
            longest = workout
        return longest

    return longest

def total_duration(workouts):
    
    total = 0
    for workout in workouts:
        total += workout['duration']
    return total

def average_duration(workouts):
    if not workouts:
        return 0
    return total_duration(workouts) / len(workouts)
    