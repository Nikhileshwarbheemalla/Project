# Personal Fitness Tracker

# Dictionary to store fitness data
# Format: {user_name: [workout_tuples]}
# Each workout tuple: (exercise, duration_minutes, calories_burned)
fitness_data = {}

# Function to log a new workout
def log_workout(user_name, exercise, duration, calories):
    workout = (exercise, duration, calories)
    fitness_data.setdefault(user_name, []).append(workout)
    print(f"Logged workout: {exercise} for {user_name}.")

# Function to display workout history
def display_workout_history(user_name):
    if user_name not in fitness_data or not fitness_data[user_name]:
        print(f"No workouts found for {user_name}.")
    else:
        print(f"\nWorkout History for {user_name}:")
        for idx, (exercise, duration, calories) in enumerate(fitness_data[user_name], 1):
            print(f"{idx}. Exercise: {exercise}, Duration: {duration} mins, Calories Burned: {calories} kcal")

# Function to calculate total calories burned
def total_calories(user_name):
    if user_name not in fitness_data or not fitness_data[user_name]:
        print(f"No workouts logged for {user_name}.")
        return 0
    total = sum(workout[2] for workout in fitness_data[user_name])
    print(f"Total calories burned by {user_name}: {total} kcal")
    return total

# Recursive function to search for a specific workout
def search_workout(user_name, exercise_name, idx=0):
    if user_name not in fitness_data or idx >= len(fitness_data[user_name]):
        return None
    if fitness_data[user_name][idx][0].lower() == exercise_name.lower():
        return fitness_data[user_name][idx]
    return search_workout(user_name, exercise_name, idx + 1)

# Main menu loop
def main():
    while True:
        print("\nPersonal Fitness Tracker Menu:")
        print("1. Log Workout")
        print("2. View Workout History")
        print("3. Calculate Total Calories")
        print("4. Search for a Workout")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            user_name = input("Enter your name: ")
            exercise = input("Enter exercise name: ")
            duration = int(input("Enter duration (in minutes): "))
            calories = int(input("Enter calories burned: "))
            log_workout(user_name, exercise, duration, calories)
        elif choice == '2':
            user_name = input("Enter your name: ")
            display_workout_history(user_name)
        elif choice == '3':
            user_name = input("Enter your name: ")
            total_calories(user_name)
        elif choice == '4':
            user_name = input("Enter your name: ")
            exercise_name = input("Enter exercise name to search: ")
            result = search_workout(user_name, exercise_name)
            if result:
                print(f"Workout Found: Exercise: {result[0]}, Duration: {result[1]} mins, Calories: {result[2]} kcal")
            else:
                print(f"No workout found for {exercise_name}.")
        elif choice == '5':
            print("Exiting Fitness Tracker. Stay healthy!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the application
if __name__ == "__main__":
    main()