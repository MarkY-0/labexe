def get_longest_workout(workouts):


    if not workouts:
        return None
    
    longest = workouts[0]
    for workout in workouts:
        if workout['duration'] > longest['duration']:
            longest = workout
        return longest

    return longest